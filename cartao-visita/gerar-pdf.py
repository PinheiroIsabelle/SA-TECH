#!/usr/bin/env python3
"""
Gera o PDF de impressão dos cartões de visita SA·TECH a partir de cartao-visita.html.

Por que este script existe em vez de um simples "imprimir para PDF":

  1. O Chromium arredonda a área imprimível para baixo (95,927 mm quando se pede
     96 mm), o que deixaria uma faixa branca comendo a sangria. Por isso o HTML
     usa uma página 1 mm maior e desenha o cartão no tamanho exato no canto
     superior esquerdo.
  2. Aqui a página é recortada para os 96 × 56 mm do cartão mexendo apenas na
     MediaBox/CropBox. O conteúdo não é reescalado de propósito: aplicar uma
     transformação no fluxo de conteúdo desloca os padrões de gradiente do
     Chromium e cria artefatos visíveis na arte.

No fim o script confere página por página se a medida bate e se o fundo chega às
quatro bordas, e regenera preview.png.

Uso:
    python3 gerar-pdf.py

Dependências:
    pip install pypdf pypdfium2 pillow
"""

import shutil
import subprocess
import sys
from pathlib import Path

from PIL import Image
from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject
import pypdfium2 as pdfium

BASE = Path(__file__).resolve().parent
SOURCE = BASE / "cartao-visita.html"
OUTPUT = BASE / "sa-tech-cartoes-visita.pdf"
PREVIEW = BASE / "preview.png"

MM = 72 / 25.4
TRIM_W, TRIM_H = 90.0, 50.0          # formato final do cartão
BLEED = 3.0                           # sangria por lado
PAGE_W = (TRIM_W + BLEED * 2) * MM    # 96 mm
PAGE_H = (TRIM_H + BLEED * 2) * MM    # 56 mm

TOLERANCE_MM = 0.1
BLEED_TOLERANCE = 4      # diferença de cor aceitável entre canto e miolo (0-255)
PREVIEW_DPI = 300

CHROME_CANDIDATES = [
    "chromium",
    "chromium-browser",
    "google-chrome",
    "/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
]


def find_chrome() -> str:
    for candidate in CHROME_CANDIDATES:
        resolved = shutil.which(candidate) or (candidate if Path(candidate).exists() else None)
        if resolved:
            return resolved
    sys.exit("Chromium/Chrome não encontrado. Ajuste CHROME_CANDIDATES.")


def render_raw(chrome: str, raw_pdf: Path) -> None:
    subprocess.run(
        [
            chrome,
            "--headless",
            "--no-sandbox",
            "--disable-gpu",
            "--virtual-time-budget=8000",
            "--no-pdf-header-footer",
            f"--print-to-pdf={raw_pdf}",
            SOURCE.as_uri(),
        ],
        check=True,
        capture_output=True,
    )


def crop_to_card(raw_pdf: Path) -> None:
    """Recorta cada página para o cartão, ancorado no canto superior esquerdo."""
    reader = PdfReader(str(raw_pdf))
    writer = PdfWriter()

    for page in reader.pages:
        page_h = float(page.mediabox.height)
        page_w = float(page.mediabox.width)
        if page_w < PAGE_W - 0.01 or page_h < PAGE_H - 0.01:
            sys.exit(
                f"Página menor que o cartão ({page_w / MM:.3f} × {page_h / MM:.3f} mm). "
                "Aumente o 'size' do @page no HTML."
            )
        # a origem do PDF é o canto inferior esquerdo; o cartão fica no topo
        box = RectangleObject((0, page_h - PAGE_H, PAGE_W, page_h))
        page.mediabox = box
        page.cropbox = box
        writer.add_page(page)

    writer.add_metadata(
        {
            "/Title": f"SA-TECH - Cartoes de visita {TRIM_W:.0f}x{TRIM_H:.0f}mm (sangria {BLEED:.0f}mm)",
            "/Creator": "SA TECH",
            "/Subject": "Frente e verso - Isabelle, Marcelo, Iohana",
        }
    )
    writer.write(str(OUTPUT))


def bleed_gap(img: Image.Image) -> int:
    """Maior diferença entre a cor de cada canto e a do fundo 4 mm adentro.

    Se o fundo chega à borda, o canto tem a mesma cor que o miolo ao lado dele.
    Se faltar sangria, o canto vira o branco do papel e a diferença aparece.

    Usa a mediana de uma mancha de 2 mm, não a média: a malha de fundo é feita de
    linhas de 0,16 mm, e a média de uma mancha pequena oscila conforme as linhas
    caem dentro ou fora dela. A mediana devolve a cor do fundo e ignora as linhas.

    Vale um aviso: num cartão de fundo branco este teste não prova nada, porque a
    falta de sangria é da mesma cor do papel. Ele existe para os fundos com cor —
    aqui, o verso.
    """
    w, h = img.size
    patch = max(2, round(2.0 / 25.4 * PREVIEW_DPI))    # 2 mm
    inset = round(4.0 / 25.4 * PREVIEW_DPI)            # 4 mm, além da sangria

    def mediana(x: int, y: int) -> tuple[int, ...]:
        px = list(img.crop((x, y, x + patch, y + patch)).getdata())
        return tuple(sorted(c[i] for c in px)[len(px) // 2] for i in range(3))

    pior = 0
    for cx, cy, dx, dy in ((0, 0, 1, 1), (w - patch, 0, -1, 1),
                           (0, h - patch, 1, -1), (w - patch, h - patch, -1, -1)):
        canto = mediana(cx, cy)
        dentro = mediana(cx + dx * inset, cy + dy * inset)
        pior = max(pior, max(abs(a - b) for a, b in zip(canto, dentro)))
    return pior


def verify_and_preview() -> None:
    reader = PdfReader(str(OUTPUT))
    pdf = pdfium.PdfDocument(str(OUTPUT))
    pages, problems = [], []

    for i, (meta, page) in enumerate(zip(reader.pages, pdf), 1):
        w_mm = float(meta.mediabox.width) / MM
        h_mm = float(meta.mediabox.height) / MM
        if abs(w_mm - 96) > TOLERANCE_MM or abs(h_mm - 56) > TOLERANCE_MM:
            problems.append(f"p{i}: página {w_mm:.3f} × {h_mm:.3f} mm (esperado 96 × 56)")

        img = page.render(scale=PREVIEW_DPI / 72).to_pil().convert("RGB")
        pages.append(img)
        desvio = bleed_gap(img)
        if desvio > BLEED_TOLERANCE:
            problems.append(
                f"p{i}: sangria incompleta — a cor do canto difere do fundo em {desvio} "
                "(o fundo não chega à borda da página)"
            )
        print(f"  p{i}: {w_mm:.3f} × {h_mm:.3f} mm · desvio de sangria {desvio}")

    if problems:
        sys.exit("FALHOU:\n  " + "\n  ".join(problems))

    w, h = pages[0].size
    margin, gap = 70, 60
    canvas = Image.new("RGB", (w + margin * 2, h * 2 + gap + margin * 2), (236, 238, 244))
    canvas.paste(pages[0], (margin, margin))
    canvas.paste(pages[1], (margin, margin + h + gap))
    canvas.save(PREVIEW, optimize=True)
    print(f"\nOK · {len(pages)} páginas · {OUTPUT.name} · {PREVIEW.name}")


def main() -> None:
    raw_pdf = BASE / ".raw.pdf"
    try:
        chrome = find_chrome()
        print(f"Chromium: {chrome}")
        render_raw(chrome, raw_pdf)
        crop_to_card(raw_pdf)
        verify_and_preview()
    finally:
        raw_pdf.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
