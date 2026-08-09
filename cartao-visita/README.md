# Cartões de visita SA·TECH

Cartões de frente e verso para Isabelle, Marcelo e Iohana, no mesmo sistema visual
da landing page e do pôster do evento (gradiente `#8b3ffb → #3b7bfb`, fundo
`#0d0e15`, wordmark `SA·TECH`).

![Frente e verso](preview.png)

## Arquivos

| Arquivo | Para que serve |
| --- | --- |
| `sa-tech-cartoes-visita.pdf` | **É o que vai para a gráfica.** 6 páginas, pronto para impressão. |
| `cartao-visita.html` | Fonte editável. Fontes embutidas — abre igual em qualquer máquina, sem internet. |
| `gerar-pdf.py` | Regera o PDF e o `preview.png` a partir do HTML. |
| `preview.png` | Prévia da frente e do verso em 300 dpi. |

## Especificação para a gráfica

| Item | Valor |
| --- | --- |
| Formato final (corte) | 90 × 50 mm |
| Sangria | 3 mm por lado |
| Página do PDF | 96 × 56 mm (já com a sangria) |
| Área de segurança | 5 mm a partir da linha de corte |
| Páginas | 6 — pares frente/verso: 1‑2 Isabelle, 3‑4 Marcelo, 5‑6 Iohana |
| Cores | RGB (converter para CMYK no fluxo da gráfica) |
| Marcas de corte | Não incluídas — a arte já vem com sangria, a gráfica aplica o corte |

O verso é idêntico nos três cartões, então dá para fechar como **um verso único**
para toda a tiragem, se a gráfica cobrar por face.

### Dois pontos que valem avisar na hora do orçamento

- **Muita cobertura de tinta.** As duas faces são chapadas: frente escura e verso
  em gradiente vivo. Em impressão digital barata isso costuma dar marcas de
  rolete e banding no gradiente. Peça uma **prova impressa** antes de fechar a
  tiragem.
- **Acabamento.** Laminação fosca disfarça marcas de dedo no fundo escuro e é a
  escolha mais segura aqui. Verniz localizado no wordmark do verso fica muito
  bom, mas encarece.

Papel sugerido: couché fosco 300 g ou 350 g.

## Como editar

Abra `cartao-visita.html` num editor de texto. Cada cartão é um bloco
`<section class="card front">` comentado com o nome da pessoa. O que costuma mudar:

- **Nome** — `<div class="name">Isabelle</div>`
- **Telefone** — dentro de `<div class="contact wa">`
- **Cargo** — vem comentado. Descomente e escreva:
  ```html
  <div class="role">Cargo aqui</div>
  ```

Para adicionar uma quarta pessoa, copie um par frente/verso inteiro e troque nome
e telefone.

Abrir o HTML no navegador mostra a prévia com o tracejado de corte e de área
segura. **Não imprima direto do navegador para a gráfica** — a página do HTML tem
1 mm de folga proposital (o navegador arredonda a área imprimível para baixo e
comeria a sangria); quem tira essa folga é o `gerar-pdf.py`.

## Fontes

Inter (nomes e contatos) e IBM Plex Mono (as linhas em caixa alta), ambas sob a
SIL Open Font License — uso comercial e incorporação liberados. Vão embutidas em
base64 no HTML, então o arquivo abre igual em qualquer máquina e o PDF não
depende de nenhuma fonte instalada na gráfica.

## Regerar o PDF

```bash
pip install pypdf pypdfium2 pillow
python3 gerar-pdf.py
```

O script imprime o HTML pelo Chromium, recorta a página para 96 × 56 mm exatos e
confere, página por página, se a medida bate e se a sangria chega aos quatro
cantos. Se algo sair fora do esperado, ele falha com o motivo em vez de gerar um
PDF silenciosamente errado.
