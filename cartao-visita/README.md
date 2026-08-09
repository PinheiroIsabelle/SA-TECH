# Cartões de visita SA·TECH

Cartões de frente e verso para Isabelle, Marcelo e Iohana, seguindo o manual de
marca (`../SA-Tech-Design-System.docx`).

- **Frente**: fundo em Azul SA Tech `#071C89` com texto branco e acento em Magenta
  `#B910C3` — a aplicação que o manual descreve na seção 7 para peças de destaque.
  O magenta entra como brilho no canto superior e na régua sob o nome, ficando na
  faixa de 10% da regra 60‑30‑10.
- **Verso**: gradiente de marca `#0B1B72 → #A31DBF` na diagonal de 45°, com a logo
  sozinha no centro.
- **Tipografia**: Poppins Bold nos nomes e Inter nos contatos e legendas, como
  manda a seção 4.

A logo usada é a **versão reversa (branca)** do logotipo oficial — a mesma que o
manual de marca (`../SA-Tech-Design-System.docx`, seção 2) prevê para fundos
escuros. Ela foi extraída da arte colorida do manual: o fundo claro virou
transparente e a tinta virou branca, preservando o traçado de circuito do símbolo,
a órbita e os pontos. O arquivo está em `logo-sa-tech-branca.png` (PNG com
transparência, 1054 × 483 px).

Regras do manual aplicadas:

- **Tamanho mínimo em impresso: 3 cm de largura.** Frente com 30 mm, verso com 46 mm.
- **Área de proteção** equivalente à altura da caixa alta do wordmark (4,1 mm na
  frente, 6,2 mm no verso): nenhum elemento nem a linha de corte invade essa folga.
- Reversa branca sobre fundo escuro/saturado — o manual proíbe a versão colorida
  sobre o gradiente saturado, que é o caso do verso.
- Sem sombra, contorno, distorção ou recolorização do gradiente do símbolo.

![Frente e verso](preview.png)

## Arquivos

| Arquivo | Para que serve |
| --- | --- |
| `sa-tech-cartoes-visita.pdf` | **É o que vai para a gráfica.** 6 páginas, pronto para impressão. |
| `cartao-visita.html` | Fonte editável. Fontes embutidas — abre igual em qualquer máquina, sem internet. |
| `gerar-pdf.py` | Regera o PDF e o `preview.png` a partir do HTML. |
| `preview.png` | Prévia da frente e do verso em 300 dpi. |
| `logo-sa-tech-branca.png` | Logo oficial na versão reversa (branca), com transparência. |

## Especificação para a gráfica

| Item | Valor |
| --- | --- |
| Formato final (corte) | 90 × 50 mm |
| Sangria | 3 mm por lado |
| Página do PDF | 96 × 56 mm (já com a sangria) |
| Área de segurança | 5 mm a partir da linha de corte |
| Páginas | 6 — pares frente/verso: 1‑2 Isabelle, 3‑4 Marcelo, 5‑6 Iohana |
| Cores | RGB (converter para CMYK no fluxo da gráfica) — ver a nota sobre o azul abaixo |
| Marcas de corte | Não incluídas — a arte já vem com sangria, a gráfica aplica o corte |

O verso é idêntico nos três cartões, então dá para fechar como **um verso único**
para toda a tiragem, se a gráfica cobrar por face.

### O que vale avisar na hora do orçamento

- **Muita cobertura de tinta.** As duas faces são chapadas: frente em azul sólido
  e verso em gradiente vivo. Em impressão digital barata isso costuma dar marcas
  de rolete e banding no gradiente. Peça uma **prova impressa** antes de fechar a
  tiragem.
- **Azul e magenta são cores RGB saturadas.** Azul SA Tech `#071C89` e Magenta
  `#B910C3` ficam fora do gamut CMYK: na conversão o azul tende a fechar e o
  magenta a perder brilho. É o motivo mais forte para pedir a prova impressa — e,
  se o resultado não agradar, vale perguntar à gráfica sobre uma cor especial
  (Pantone) para o azul.
- **Acabamento.** Laminação fosca disfarça marcas de dedo no fundo escuro e é a
  escolha mais segura aqui. Verniz localizado sobre a logo do verso fica muito
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

Poppins Bold (nomes) e Inter (contatos e legendas), as duas do manual, ambas sob
a SIL Open Font License — uso comercial e incorporação liberados. Vão embutidas em
base64 no HTML, então o arquivo abre igual em qualquer máquina e o PDF não
depende de nenhuma fonte instalada na gráfica.

Uma observação: os ícones de contato são brancos, inclusive o do WhatsApp. O verde
da plataforma não existe na paleta, e sobre o azul sólido o branco é o equivalente
ao "Azul SA Tech como padrão" que o manual define para fundos claros.

## Regerar o PDF

```bash
pip install pypdf pypdfium2 pillow
python3 gerar-pdf.py
```

O script imprime o HTML pelo Chromium, recorta a página para 96 × 56 mm exatos e
confere, página por página, se a medida bate e se a sangria chega aos quatro
cantos. Se algo sair fora do esperado, ele falha com o motivo em vez de gerar um
PDF silenciosamente errado.
