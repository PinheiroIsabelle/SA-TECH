# Cartões de visita SA·TECH

Cartões de frente e verso para Isabelle, Marcelo e Iohana, seguindo o manual de
marca (`../SA-Tech-Design-System.docx`).

- **Frente**: fundo em Azul SA Tech com texto branco e acento em Magenta — a
  aplicação que o manual descreve na seção 7 para peças de destaque. O magenta
  entra como brilho no canto superior e na régua sob o nome, ficando na faixa de
  10% da regra 60‑30‑10.
- **Verso**: gradiente de marca na diagonal de 45°, com a logo sozinha no centro.
- **Tipografia**: Poppins Bold nos nomes e Inter nos contatos e legendas, como
  manda a seção 4.
- **Cores**: convertidas para os equivalentes mais próximos que a impressão em
  CMYK alcança — veja a seção *Cores* abaixo.

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
- **As cores já estão dentro do gamut CMYK.** Não há surpresa na conversão: a
  arte inteira foi provada contra o PSO Coated v3 e o desvio máximo é ΔE 2.8
  (detalhes na seção *Cores*). Ainda assim, peça a prova — ela serve para conferir
  o gradiente e a cobertura, não a cor.
- **Acabamento.** Laminação fosca disfarça marcas de dedo no fundo escuro e é a
  escolha mais segura aqui. Verniz localizado sobre a logo do verso fica muito
  bom, mas encarece.

Papel sugerido: couché fosco 300 g ou 350 g.

## Cores

O manual define Azul SA Tech `#071C89` e Magenta SA Tech `#B910C3`. As duas são
cores de tela e **não existem em CMYK** — nenhuma combinação de tinta chega nelas.
Mandar esses valores para a gráfica significa deixar a conversão por conta dela e
receber algo que ninguém escolheu.

Então o cartão usa, para cada cor da marca, a cor imprimível mais próxima. A
escolha foi feita por medição: busca no espaço CMYK pelo menor ΔE contra a cor do
manual, usando o perfil **PSO Coated v3 (FOGRA51)**, que é o padrão para papel
couché. O ISO Coated v2 300% (FOGRA39) dá praticamente o mesmo resultado.

| Cor do manual | Receita de tinta | Fica | Tinta | ΔE |
| --- | --- | --- | --- | --- |
| Azul SA Tech `#071C89` | **C100 M100 Y0 K0** | `#3A3586` | 200% | 21,7 |
| Magenta SA Tech `#B910C3` | **C40 M100 Y0 K0** | `#A42783` | 140% | 34,4 |
| Gradiente, início `#0B1B72` | **C100 M100 Y0 K0** | `#3A3586` | 200% | 13,5 |
| Gradiente, fim `#A31DBF` | **C55 M100 Y0 K0** | `#8B2C84` | 155% | 32,1 |

Tons auxiliares, derivados do azul: escurecimento das bordas **C100 M100 Y0 K40**
(`#312D63`) e o topo do gradiente do fundo **C90 M90 Y0 K0** (`#473E8D`).

O ΔE alto do magenta é inevitável: `#B910C3` é um roxo-magenta muito saturado, e
CMYK simplesmente não chega lá. Se esse magenta exato for inegociável, o caminho
é uma **cor especial (Pantone)** como quinta tinta — o que muda o orçamento.

**A régua sob o nome é a exceção.** O magenta imprimível (`#A42783`) tem contraste
de só 1,6:1 contra o azul de fundo: impresso, o traço sumiria. Ela usa
**C20 M80 Y0 K0** (`#C85398`), um magenta mais claro, que sobe o contraste para
2,5:1 e deixa o traço visível. É uma escolha de legibilidade, não de fidelidade.

### Verificações

- **Gamut**: prova da arte inteira contra o PSO Coated v3 — desvio médio ΔE 1,4 e
  máximo 2,8 na frente; 0,8 e 1,9 no verso. Na prática, o que está na tela é o que
  sai impresso.
- **Cobertura de tinta**: máximo de 218% na frente e 202% no verso, com folga
  larga para o limite de 300% do couché.
- **Contraste**, medido sobre o fundo já composto: nome em branco a 10,2:1,
  contatos a 7,4:1, legendas a 5,4:1 — todos acima do mínimo de acessibilidade
  para texto pequeno. A régua magenta fica em 2,5:1, suficiente para um traço
  cheio.

### Sobre entregar em CMYK

O PDF sai em RGB de propósito. A conversão para CMYK é melhor feita pela gráfica,
com o perfil da máquina e do papel dela. Como as cores já estão dentro do gamut,
essa conversão é praticamente sem perda — e a tabela acima diz exatamente que
tinta cada cor deve virar, então dá para conferir o resultado.

Se a gráfica exigir o arquivo já em CMYK, peça — não converta com ferramenta
genérica. O Ghostscript, por exemplo, ignora o perfil informado e contamina o azul
com 11% de amarelo, sujando a cor.

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
