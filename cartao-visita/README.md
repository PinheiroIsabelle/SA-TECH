# Cartões de visita SA·TECH

Cartões de frente e verso para Isabelle, Marcelo e Iohana, em **preto e branco**,
seguindo o manual de marca (`../SA-Tech-Design-System.docx`).

- **Frente**: papel branco, logo e nome em tinta escura, contatos e legendas em
  cinza, malha discreta ao fundo.
- **Verso**: fundo cinza-branco com o **QR code** da landing page à esquerda e a
  logo com uma chamada curta à direita.
- **Tipografia**: Poppins Bold nos nomes e Inter nos contatos e legendas, como
  manda a seção 4 do manual.
- **Uma tinta só**: todos os tons são cinzas neutros, então o cartão imprime em
  preto puro — o caminho mais barato. Detalhes na seção *Cores*.

Esta é a **versão monocromática** que o manual prevê na seção 2 ("100% tinta
escura, para aplicações de baixo custo"). A versão colorida, com o azul e o
magenta da marca, está no histórico do repositório (commit `9bfca26`) e pode ser
retomada.

![Frente e verso](preview.png)

## Logo

A logo é o logotipo oficial extraído da arte do manual: o fundo claro virou
transparente e a tinta virou cinza neutro, preservando o traçado de circuito do
símbolo, a órbita e os pontos. Há duas versões no repositório:

- `logo-sa-tech-tinta.png` — cinza escuro, usada nestes cartões.
- `logo-sa-tech-branca.png` — reversa branca, para fundos escuros.

Regras do manual aplicadas:

- **Tamanho mínimo em impresso: 3 cm de largura.** Frente com 30 mm, verso com 36 mm.
- **Área de proteção** equivalente à altura da caixa alta do wordmark (4,1 mm na
  frente, 4,8 mm no verso): nenhum elemento nem a linha de corte invade essa folga.
- Sem sombra, contorno, distorção ou recolorização.

## QR code

Aponta para `https://sa-tech-welcome.vercel.app/` — a landing page do repositório,
que já oferece WhatsApp de cada pessoa, site e LinkedIn. É a mesma URL do QR do
pôster (`../qrcode-evento/gen_qr.py`).

| Item | Valor |
| --- | --- |
| Correção de erro | Q (25%) — versão 4, 33 × 33 módulos |
| Tamanho do código | 17,7 mm |
| Módulo | 0,54 mm — bem acima do mínimo prático de 0,4 mm |
| Zona de silêncio | 4,0 mm, contra os 2,2 mm (4 módulos) que a norma pede |
| Formato | vetorial (SVG inline), não imagem — imprime nítido em qualquer escala |

O QR fica dentro de um bloco branco com borda em cinza-linha — o componente "card"
da seção 6 do manual. O bloco também garante a zona de silêncio: nada de escuro
entra na área clara em volta do código.

**Foi testado lendo o PDF final**, não o arquivo de origem: decodifica correto a
300, 600 e 1200 dpi.

> Se a landing page mudar de endereço, o QR precisa ser regerado — ele carrega a
> URL, não um redirecionador. Vale considerar um encurtador próprio se o endereço
> não for definitivo.

## Arquivos

| Arquivo | Para que serve |
| --- | --- |
| `sa-tech-cartoes-visita.pdf` | **É o que vai para a gráfica.** 6 páginas, pronto para impressão. |
| `cartao-visita.html` | Fonte editável. Fontes e logo embutidos — abre igual em qualquer máquina, sem internet. |
| `gerar-pdf.py` | Regera o PDF e o `preview.png` a partir do HTML, com conferências. |
| `preview.png` | Prévia da frente e do verso em 300 dpi. |
| `logo-sa-tech-tinta.png` | Logo em cinza escuro, com transparência. |
| `logo-sa-tech-branca.png` | Logo reversa branca, para fundos escuros. |
| `qr-code.svg` | O QR code em vetor, avulso, para reuso em outras peças. |

## Especificação para a gráfica

| Item | Valor |
| --- | --- |
| Formato final (corte) | 90 × 50 mm |
| Sangria | 3 mm por lado |
| Página do PDF | 96 × 56 mm (já com a sangria) |
| Área de segurança | 5 mm a partir da linha de corte |
| Páginas | 6 — pares frente/verso: 1‑2 Isabelle, 3‑4 Marcelo, 5‑6 Iohana |
| Cores | **1 cor (preto)** — arquivo em escala de cinza, R=G=B em todos os pixels |
| Marcas de corte | Não incluídas — a arte já vem com sangria, a gráfica aplica o corte |

O verso é idêntico nos três cartões, então dá para fechar como **um verso único**
para toda a tiragem, se a gráfica cobrar por face.

### O que vale avisar na hora do orçamento

- **É um trabalho de uma cor.** Peça orçamento de 1×0 ou 1×1 (preto), não de
  4×4 — a diferença de preço é grande. Se a gráfica só trabalhar em 4 cores, peça
  que o preto saia **em K puro**, sem preto rico (sem apoio de ciano, magenta e
  amarelo): em texto de 6–7 pt, o preto rico exige registro perfeito e qualquer
  desvio borra as letras.
- **Cobertura de tinta baixíssima.** Sem chapado escuro, sem gradiente. Não há o
  risco de banding nem de marca de rolete que a versão colorida tinha, e a prova
  impressa deixa de ser indispensável.
- **Acabamento.** Sem fundo escuro, marca de dedo deixa de ser problema — laminação
  passa a ser escolha estética, não necessidade. Se quiser um toque de acabamento,
  relevo seco (baixo-relevo) na logo funciona bem em cartão monocromático.

Papel sugerido: couché fosco 300 g ou 350 g. Como o cartão é claro, papel de alta
alvura ajuda o contraste.

## Cores

Todos os tons são **cinzas neutros** (R=G=B), de propósito: é isso que permite
imprimir com uma tinta só. Os valores vêm dos neutros da seção 3 do manual,
convertidos para o cinza de mesma luminosidade, e a porcentagem é a de tinta preta
que os reproduz em couché (perfil PSO Coated v3 / FOGRA51).

| Uso | Neutro do manual | Cinza usado | Tinta |
| --- | --- | --- | --- |
| Tinta — logo, nome, régua, ícones | `#191C21` | `#1C1C1C` | **K 100%** |
| Cinza secundário — contatos e legendas | `#5B6472` | `#646464` | **K 77%** |
| Cinza linha — malha e borda do bloco | `#D9DCE3` | `#DCDCDC` | **K 19%** |
| Cinza-branco — fundo do verso | `#F5F4F9` | `#F4F4F4` | **K 6%** |
| Papel — fundo da frente | `#FFFFFF` | `#FFFFFF` | K 0% |

Uma coisa que vale saber antes de ver o cartão impresso: **K 100% em couché tem
L\* 17,5**, o que na tela equivale a mais ou menos `#2B2B2B`. Ou seja, o "preto" do
cartão vai parecer um grafite bem escuro, não o preto absoluto de um monitor. Isso é
o limite de uma tinta preta sobre papel, não um problema do arquivo — a tinta do
manual (`#191C21`, L\* 10,2) é mais escura do que uma tinta só alcança. Preto rico
chegaria mais fundo, mas custa o registro do texto pequeno.

### Verificações

Todas medidas no PDF final, não no arquivo de origem:

- **Neutralidade**: desvio máximo de R=G=B igual a **zero** em todos os pixels das
  duas faces. O arquivo é genuinamente escala de cinza.
- **Contraste**: tinta sobre branco a 17,0:1; cinza secundário sobre branco a
  5,9:1; cinza secundário sobre o cinza-branco do verso a 5,4:1. Todos acima do
  mínimo de acessibilidade para texto pequeno.
- **Margens**: o conteúdo da frente fica a 4,9 mm da linha de corte; o do verso, a
  11 mm.
- **QR**: decodifica a 300, 600 e 1200 dpi, com zona de silêncio de 4,0 mm.

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

Os ícones de contato são monocromáticos, inclusive o do WhatsApp — em um cartão de
uma cor não há verde, e a forma do ícone já é reconhecível.

## Regerar o PDF

```bash
pip install pypdf pypdfium2 pillow
python3 gerar-pdf.py
```

O script imprime o HTML pelo Chromium, recorta a página para 96 × 56 mm exatos e
confere, página por página, se a medida bate e se o fundo chega às quatro bordas.
Se algo sair fora do esperado, ele falha com o motivo em vez de gerar um PDF
silenciosamente errado.
