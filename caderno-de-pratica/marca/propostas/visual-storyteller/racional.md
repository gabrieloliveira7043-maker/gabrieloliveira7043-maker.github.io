# Caderno de Prática: conceitos de símbolo C e D

Proposta de Visual Storyteller. Os dois partem de uma regra só: o teclado não aparece como enfeite ao lado da ideia. Ele já é a ideia. Nenhum dos dois usa caderno, página, argola ou ✓, e nenhum transforma teclas em onda sonora.

Paleta: pistache `#99AB59`, creme `#FBF7EA`, grafite esverdeado `#1F2619`. Tudo em cor chapada. Os arquivos usam só `rect` e `path`, com fundo de 512×512 e `rx="116"`.

---

## Conceito C: Dueto

**A história.** Num teclado, as duas teclas pretas juntas (dó♯ e ré♯) se alongam para cima e se ligam numa barra, e assim viram duas colcheias ligadas: a professora e o aluno tocando a mesma frase. A segunda nota fica um degrau acima da primeira, porque é isso que a aula faz: a professora dá o tom e o aluno sobe.

**Como junta teclado, canto e aula.**
- Teclado: três teclas brancas e o par de teclas pretas que todo mundo reconhece, na posição em que ficam num piano de verdade, sobre os vãos entre as brancas.
- Canto: duas notas ligadas formam uma frase melódica. É o "pergunta e resposta" da aula de canto: a professora canta, o aluno repete.
- Aula: são duas figuras unidas por uma barra (a ligação entre as duas), e a nota do aluno sobe. Isso mostra progresso sem precisar de seta nem de gráfico.

**Por que funciona pequeno.** Em 16 px sobram três massas: um bloco claro embaixo, uma forma escura em "Π" com duas cabeças ovais e o fundo pistache. A silhueta da colcheia dupla é um dos sinais musicais mais conhecidos, então ainda se lê mesmo com os vãos das teclas sumindo. Hastes e barra têm 44 unidades de espessura, e os vãos entre as teclas têm 14.

**Notas de construção.** Simétrico em torno de x = 256: teclas em 95, 207 e 319, com 98 de largura, e hastes centradas nos vãos (x = 200 e x = 312). As duas hastes medem 220 e a barra sobe 40, o mesmo desnível entre as cabeças de nota (centros em y = 344 e y = 304). As cabeças são elipses de 46 × 35 inclinadas a −24°, com a haste encostada à direita, como na notação. Área ocupada: x 95–417, y 76–436.
No tema escuro o fundo é grafite, as teclas são pistache e as notas creme.

---

## Conceito D: Voz Amparada

**A história.** Um microfone de estúdio clássico cuja grade é, na verdade, um teclado deitado: as faixas da grade são teclas brancas, e as duas teclas pretas saem da borda. Quem segura o microfone é o suporte em "U" que o envolve sem encostar, e esse suporte é a professora, que dá apoio à voz do aluno até ela ficar firme.

**Como junta teclado, canto e aula.**
- Canto: o microfone é o símbolo mais direto da voz, e a cápsula com fundo redondo lembra os microfones de estúdio.
- Teclado: girado 90°, o teclado vira a grade do microfone. Faixas horizontais com duas teclas pretas na lateral são lidas ao mesmo tempo como grade e como teclas.
- Aula: o suporte em "U" é concêntrico à cápsula e fica sempre a 16 unidades de distância dela. Ele acompanha e protege sem apertar, como a professora acompanha a evolução de cada aluno.

**Por que funciona pequeno.** A silhueta (cápsula, berço, haste e base) é reconhecível em qualquer tamanho e não depende de detalhe interno. Em 32 px as faixas e as teclas pretas aparecem. Em 16 px fica um microfone claro sobre o berço escuro, e isso basta. O traço mais fino tem 28 unidades (berço e haste), e as teclas pretas têm 40 de altura.

**Notas de construção.** Simétrico em torno de x = 256 (as teclas pretas, de propósito, só à esquerda). A cápsula vai de x 168 a 344 e de y 72 a 328, com cantos de cima em raio 52 e fundo em semicírculo de raio 88 centrado em (256, 240). O berço é um arco de raio 118 com o mesmo centro e traço 28, o que dá raio interno 104 e externo 132. As teclas pretas ficam no trecho reto da borda (y 124–244) para não vazar da curva. Área ocupada: x 124–388, y 72–440.
No tema escuro o fundo é grafite, a cápsula fica creme, os vãos e as teclas pretas viram recortes em grafite, e o berço, a haste e a base ficam em pistache.

---

## Em uma linha

- **C, Dueto**: as duas teclas pretas do piano viram duas colcheias ligadas, a professora e o aluno, e a nota do aluno sobe.
- **D, Voz Amparada**: a voz do aluno, num microfone feito de teclas, segura pelo berço da professora.
