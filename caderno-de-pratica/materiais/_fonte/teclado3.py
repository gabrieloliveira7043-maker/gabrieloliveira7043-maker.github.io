"""Conteúdo do material didático do módulo Teclado 3 (um tópico por PDF)."""
from gerar import teclado, figura
from teclado2 import tabela

MODULO = "Teclado 3"
PASTA = "teclado-3"


def acorde(marcas, legenda, oit=1, ww=30):
    return figura(teclado(marcas, oitavas=oit, ww=ww, letras=True), legenda)


TOPICOS = [
    {
        "slug": "acordes-sustenidos",
        "titulo": "Formação de acordes sustenidos",
        "sub": "Montar os acordes maiores que começam numa tecla preta.",
        "objetivos": ["Aplicar a regra 4 + 3 semitons nas teclas pretas", "Montar C♯, D♯, F♯, G♯ e A♯",
                      "Entender por que algumas notas “caem” em teclas brancas", "Trocar entre acordes naturais e sustenidos"],
        "p1": """
<h2>A mesma receita, outra tônica</h2>
<p>O acorde maior é sempre <b>tônica + 4 semitons + 3 semitons</b>. Nos acordes sustenidos, a tônica é uma tecla preta e o formato da mão muda: às vezes as outras notas caem em teclas brancas.</p>
<div class="two">""" + acorde({"C#0": ("T", "d"), "F0": ("3", "d"), "G#0": ("5", "d")}, "C♯: C♯ – E♯ (tecla Fá) – G♯") + acorde({"F#0": ("T", "d"), "A#0": ("3", "d"), "C#1": ("5", "d")}, "F♯: F♯ – A♯ – C♯ (só pretas)", oit=2, ww=22) + "</div>" + tabela(
            ["Acorde", "Notas (no teclado)", "Formato da mão"],
            [["C♯", "C♯ – F – G♯", "preta – branca – preta"], ["D♯ (= E♭)", "D♯ – G – A♯", "preta – branca – preta"],
             ["F♯", "F♯ – A♯ – C♯", "três pretas"], ["G♯ (= A♭)", "G♯ – C – D♯", "preta – branca – preta"],
             ["A♯ (= B♭)", "A♯ – D – F", "preta – branca – branca"]]) + """
<div class="call"><b class="t">Nome teórico e tecla</b>Em C♯, a terça é Mi♯, que no teclado é a tecla Fá. Para tocar, pense na tecla; para escrever, o nome teórico é Mi♯.</div>
""",
        "passos": ["Coloque o dedo 1 da mão direita no C♯.", "Conte 4 semitons: C♯ → D → D♯ → E → F. A terça é a tecla Fá (Mi♯).",
                   "Conte mais 3: F → F♯ → G → G♯. A quinta é G♯.", "Toque C♯ – F – G♯ com 1-3-5, com os dedos mais para dentro das teclas.",
                   "Repita com F♯, G♯, D♯ e A♯."],
        "exercicios": [("Os cinco sustenidos", "C♯, D♯, F♯, G♯, A♯: 4 tempos cada.", "5 min · 60 BPM"),
                       ("Natural e sustenido", "C → C♯, F → F♯, G → G♯: ouça a mudança.", "4 min · 60 BPM"),
                       ("Mão esquerda", "Os mesmos acordes com 5-3-1.", "5 min · 60 BPM"),
                       ("Progressão em E", "E – B – C♯m – A (vai aparecer no próximo tópico).", "4 min · 70 BPM")],
        "erros": [("Tocar a terça na tecla preta errada", "Conte os 4 semitons em voz alta."),
                  ("Dedos na beirada das teclas pretas", "Avance a mão um pouco para dentro do teclado."),
                  ("Achar que E♯ não existe", "Existe na teoria; no teclado é a tecla Fá."),
                  ("Confundir D♯ com E♭", "Mesma tecla e mesmo som; o nome depende do tom.")],
        "resumo": ["Acorde maior = 4 + 3 semitons, mesmo começando na tecla preta.", "C♯: C♯ F G♯; F♯: F♯ A♯ C♯; G♯: G♯ C D♯.",
                   "Algumas notas teóricas caem em teclas brancas (E♯ = Fá, B♯ = Dó).", "Mão mais para dentro do teclado."],
    },
    {
        "slug": "acordes-sustenidos-menores",
        "titulo": "Formação de acordes sustenidos menores",
        "sub": "Os acordes menores que começam nas teclas pretas.",
        "objetivos": ["Aplicar a regra 3 + 4 semitons nas teclas pretas", "Montar C♯m, D♯m, F♯m, G♯m e A♯m",
                      "Trocar entre maior e menor sustenido", "Usar esses acordes em progressões reais"],
        "p1": """
<h2>Abaixe a terça</h2>
<p>O acorde menor é <b>tônica + 3 semitons + 4 semitons</b>. A forma mais rápida de achar é montar o maior e abaixar a terça um semitom.</p>
<div class="two">""" + acorde({"C#0": ("T", "d"), "E0": ("3", "e"), "G#0": ("5", "d")}, "C♯m: C♯ – E – G♯") + acorde({"F#0": ("T", "d"), "A0": ("3", "e"), "C#1": ("5", "d")}, "F♯m: F♯ – A – C♯", oit=2, ww=22) + "</div>" + tabela(
            ["Acorde", "Notas", "Aparece muito em"],
            [["C♯m", "C♯ – E – G♯", "tom de E (6º grau) e de A (3º grau)"], ["D♯m", "D♯ – F♯ – A♯", "tom de B (3º grau)"],
             ["F♯m", "F♯ – A – C♯", "tom de A (6º) e de D (3º)"], ["G♯m", "G♯ – B – D♯", "tom de E (3º) e de B (6º)"],
             ["A♯m (= B♭m)", "A♯ – C♯ – F", "tom de F♯ e de C♯"]]) + """
<div class="call"><b class="t">Por que isso importa</b>F♯m, C♯m e G♯m aparecem o tempo todo nos tons de A, D e E, que são muito usados em músicas de louvor e pop.</div>
""",
        "passos": ["Monte C♯ maior: C♯ – F – G♯.", "Abaixe a terça um semitom: F → E. Pronto: C♯m (C♯ – E – G♯).",
                   "Faça o mesmo para F♯m: A♯ desce para A.", "Monte G♯m (G♯ – B – D♯) e D♯m (D♯ – F♯ – A♯).",
                   "Toque a progressão A – C♯m – F♯m – D."],
        "exercicios": [("Maior → menor", "C♯/C♯m, F♯/F♯m, G♯/G♯m: alterne e ouça.", "5 min · 60 BPM"),
                       ("Progressão em A", "A – C♯m – F♯m – D.", "5 min · 70 BPM"),
                       ("Progressão em E", "E – G♯m – C♯m – A.", "5 min · 70 BPM"),
                       ("Mão esquerda", "Toque as fundamentais em oitava junto com a direita.", "4 min · 60 BPM")],
        "erros": [("Abaixar a quinta junto", "Só a terça desce um semitom."), ("Errar D♯m", "D♯ – F♯ – A♯: três teclas pretas."),
                  ("Dedo escorregando da preta", "Toque com a ponta e o dedo mais esticado para dentro."),
                  ("Confundir A♯m com B♭m", "Mesmas teclas; o nome depende do tom.")],
        "resumo": ["Menor = 3 + 4 semitons (abaixe a terça do maior).", "C♯m: C♯ E G♯; F♯m: F♯ A C♯; G♯m: G♯ B D♯.",
                   "São muito usados nos tons de A, D e E.", "Treine alternando maior e menor."],
    },
    {
        "slug": "figuras-de-tempo",
        "titulo": "Leitura da partitura com as figuras de tempo",
        "sub": "Quanto tempo dura cada nota: da semibreve à semifusa.",
        "objetivos": ["Conhecer as figuras e suas durações", "Contar figuras em compasso 4/4",
                      "Conhecer as pausas", "Ler ritmos simples com o metrônomo"],
        "p1": """
<h2>Cada figura, uma duração</h2>
<p>Na partitura, o formato da nota mostra <b>quanto tempo</b> ela dura. Cada figura vale metade da anterior. Em 4/4, a semínima vale 1 tempo:</p>
""" + tabela(["Figura", "Duração em 4/4", "Quantas cabem num compasso 4/4", "Como contar"],
             [["Semibreve", "4 tempos", "1", "1 – 2 – 3 – 4"], ["Mínima", "2 tempos", "2", "1 – 2"],
              ["Semínima", "1 tempo", "4", "1"], ["Colcheia", "1/2 tempo", "8", "1 e"],
              ["Semicolcheia", "1/4 de tempo", "16", "1 e e e (1-e-&-a)"], ["Fusa", "1/8 de tempo", "32", "muito rápida"],
              ["Semifusa", "1/16 de tempo", "64", "raríssima"]]) + """
<h2>Pausas</h2>
<p>Cada figura tem uma <b>pausa</b> com a mesma duração: é o tempo de silêncio. Pausa de semínima = 1 tempo de silêncio; pausa de mínima = 2 tempos. Silêncio também é música, e precisa ser contado.</p>
<div class="call"><b class="t">Ponto de aumento</b>Um ponto depois da nota soma metade do valor dela: mínima pontuada = 2 + 1 = 3 tempos; semínima pontuada = 1 + ½ = 1 tempo e meio.</div>
""",
        "passos": ["Ligue o metrônomo em 60 BPM.", "Toque um Dó em semibreves: 1 nota a cada 4 cliques.",
                   "Agora mínimas (2 cliques), semínimas (1 clique) e colcheias (2 notas por clique).",
                   "Conte em voz alta: “1 e 2 e 3 e 4 e” para colcheias.", "Leia um ritmo misturando figuras e pausas."],
        "exercicios": [("Escada de figuras", "Semibreve, mínimas, semínimas, colcheias no mesmo Dó.", "4 min · 60 BPM"),
                       ("Pausas contadas", "Toque no 1 e no 3, silêncio no 2 e no 4.", "3 min · 60 BPM"),
                       ("Ponto de aumento", "Mínima pontuada + semínima em cada compasso.", "4 min · 60 BPM"),
                       ("Ritmo com acordes", "Acorde de C em semínimas, depois colcheias.", "4 min · 70 BPM")],
        "erros": [("Soltar a semibreve antes do 4", "Conte até o fim e só solte no próximo 1."),
                  ("Encurtar as pausas", "Pausa também se conta em voz alta."),
                  ("Colcheias desiguais", "Use “1 e 2 e”: o “e” fica exatamente no meio."),
                  ("Esquecer o ponto", "Ponto = soma metade do valor.")],
        "resumo": ["Semibreve 4 · mínima 2 · semínima 1 · colcheia ½ · semicolcheia ¼ · fusa ⅛ · semifusa 1/16.",
                   "Cada figura vale metade da anterior.", "Pausas têm a mesma duração das figuras.", "Ponto soma metade do valor."],
    },
    {
        "slug": "cinco-musicas-inteiras",
        "titulo": "Saber tocar 5 músicas inteiras",
        "sub": "Um método para aprender, organizar e manter um repertório do começo ao fim.",
        "objetivos": ["Escolher bem as 5 músicas", "Dividir a música em partes", "Estudar parte por parte e juntar",
                      "Manter as músicas prontas com revisão"],
        "p1": """
<h2>Tocar inteira é diferente de saber os acordes</h2>
<p>Saber uma música inteira significa tocar do começo ao fim, no tempo, sem parar, sabendo a ordem das partes e as passagens entre elas. Para chegar lá, divida a música em partes:</p>
""" + tabela(["Parte", "O que é", "Dica"],
             [["Introdução", "O começo instrumental", "Muitas vezes repete os acordes do refrão"],
              ["Verso (estrofe)", "Parte que conta a história, mais calma", "Normalmente mais suave"],
              ["Pré-refrão", "Ponte curta que prepara o refrão", "Costuma crescer em intensidade"],
              ["Refrão", "A parte principal, que se repete", "Mais forte e cheio"],
              ["Ponte", "Parte diferente, aparece uma vez", "Muda a harmonia ou o clima"],
              ["Final", "O encerramento", "Termina no acorde da tônica"]]) + """
<div class="call"><b class="t">Como escolher as 5</b>Misture: 2 músicas lentas, 2 moderadas e 1 animada, em tons diferentes. Comece por músicas com poucos acordes (3 ou 4) e vá aumentando.</div>
""",
        "passos": ["Escolha a música e descubra o tom e o BPM.", "Escreva o mapa: Intro – Verso – Refrão – Verso – Refrão – Ponte – Refrão – Final.",
                   "Estude uma parte por vez, devagar, com metrônomo.", "Junte as partes, treinando as passagens (o fim de uma e o começo da outra).",
                   "Toque a música inteira com a gravação, sem parar."],
        "exercicios": [("Mapa da música", "Escreva a estrutura de cada uma das 5 músicas.", "10 min"),
                       ("Parte por parte", "Uma parte por dia, até ficar limpa.", "15 min · BPM lento"),
                       ("Passagens", "Só os 2 compassos entre verso e refrão, 10 vezes.", "5 min"),
                       ("Ensaio geral", "As 5 músicas seguidas, sem parar, uma vez por semana.", "25 min")],
        "erros": [("Começar sempre do início", "Estude a parte mais difícil primeiro."),
                  ("Parar no erro", "No ensaio geral, continue: o público não espera."),
                  ("Esquecer a ordem das partes", "Tenha o mapa da música à vista."),
                  ("Aprender e abandonar", "Revise cada música pelo menos uma vez por semana.")],
        "resumo": ["Tocar inteira = do começo ao fim, no tempo, sem parar.", "Divida em partes e faça o mapa da música.",
                   "Estude parte por parte e treine as passagens.", "Revise toda semana para não esquecer."],
    },
    {
        "slug": "transposicao-de-tom",
        "titulo": "Transposição de tom",
        "sub": "Mudar a música de tom sem mudar a música.",
        "objetivos": ["Entender quando e por que transpor", "Transpor contando semitons", "Transpor usando os graus",
                      "Transpor uma música inteira de C para G"],
        "p1": """
<h2>Mesma música, outra altura</h2>
<p>Transpor é tocar a música num tom mais grave ou mais agudo, mantendo tudo igual: todos os acordes andam a mesma distância. Usamos para encaixar a música na voz de quem canta ou para facilitar a digitação.</p>
<h2>Dois jeitos de transpor</h2>
<p><b>Por semitons:</b> conte quantos semitons separam o tom original do novo e mova todos os acordes essa mesma quantidade, mantendo maior/menor. <b>Por graus:</b> descubra o grau de cada acorde (I, IV, V, vi…) e troque pelo acorde do mesmo grau no novo tom.</p>
""" + tabela(["Grau", "I", "ii", "iii", "IV", "V", "vi"],
             [["Tom de C", "C", "Dm", "Em", "F", "G", "Am"], ["Tom de G", "G", "Am", "Bm", "C", "D", "Em"],
              ["Tom de D", "D", "Em", "F♯m", "G", "A", "Bm"], ["Tom de A", "A", "Bm", "C♯m", "D", "E", "F♯m"]]) + """
<div class="call"><b class="t">Exemplo: de C para G</b>C – G – Am – F vira G – D – Em – C. Cada acorde subiu 7 semitons (ou desceu 5): é a mesma progressão I – V – vi – IV.</div>
""",
        "passos": ["Descubra o tom original da música.", "Escolha o novo tom (teste se a parte mais aguda cabe na voz).",
                   "Escreva o grau de cada acorde no tom original.", "Troque cada grau pelo acorde correspondente no novo tom.",
                   "Toque a música inteira no novo tom e confira com a voz."],
        "exercicios": [("C → G", "Transponha C – F – G – C e C – Am – F – G.", "5 min"),
                       ("C → D", "Transponha a mesma progressão para D.", "5 min"),
                       ("Música real", "Transponha uma música do repertório para um tom 2 semitons abaixo.", "10 min"),
                       ("Com cantor", "Teste 3 tons com quem canta e escolham o melhor.", "5 min")],
        "erros": [("Mudar alguns acordes e esquecer outros", "Transponha tudo, inclusive acordes com baixo (C/E)."),
                  ("Trocar menor por maior", "O tipo do acorde não muda: Am vira Em, nunca E."),
                  ("Escolher tom só pelo começo da música", "Teste a parte mais aguda (geralmente o refrão)."),
                  ("Contar semitons errado", "Use a tabela de graus para conferir.")],
        "resumo": ["Transpor = mudar o tom mantendo a música.", "Todos os acordes andam a mesma distância.",
                   "Pelos graus é mais rápido: I, ii, iii, IV, V, vi.", "Teste o tom na parte mais aguda da música."],
    },
    {
        "slug": "inversao-de-acordes",
        "titulo": "Inversão de acordes",
        "sub": "Trocar a ordem das notas para tocar com menos movimento e mais suavidade.",
        "objetivos": ["Conhecer o estado fundamental e as duas inversões", "Montar as inversões de C, F e G",
                      "Trocar de acorde movendo pouco a mão", "Ler acordes com baixo invertido (C/E)"],
        "p1": """
<h2>As mesmas notas em outra ordem</h2>
<p>Um acorde pode ser tocado em três posições. No <b>estado fundamental</b>, a tônica é a nota mais grave (C–E–G). Na <b>1ª inversão</b>, a terça vai para baixo (E–G–C). Na <b>2ª inversão</b>, a quinta vai para baixo (G–C–E).</p>
""" + figura(teclado({"C0": ("F", "d"), "E0": ("F", "d"), "G0": ("F", "d"), "E1": ("1", "e"), "G1": ("1", "e"), "C2": ("1", "e")}, oitavas=2, ww=26, letras=True,
                     legenda='<i style="background:#99AB59"></i>Fundamental (C–E–G) <i style="background:#E7A64A"></i>1ª inversão (E–G–C)'),
             "O acorde de Dó em estado fundamental e na 1ª inversão. A 2ª inversão é G–C–E.") + tabela(
            ["Progressão", "Sem inversões", "Com inversões (mão quase parada)"],
            [["C → F", "C–E–G → F–A–C", "C–E–G → C–F–A"], ["C → G", "C–E–G → G–B–D", "C–E–G → B–D–G"],
             ["C → Am", "C–E–G → A–C–E", "C–E–G → C–E–A"]]) + """
<div class="call"><b class="t">Por que usar</b>Com inversões, a mão direita se move pouco e as notas passam de um acorde ao outro de forma suave. É assim que pianistas fazem acompanhamentos que soam “ligados”.</div>
""",
        "passos": ["Toque C–E–G (fundamental).", "Passe o Dó para cima: E–G–C (1ª inversão).", "Passe o Mi para cima: G–C–E (2ª inversão).",
                   "Toque C → F mantendo o Dó: C–E–G → C–F–A.", "Toque C → G com B–D–G e volte ao C."],
        "exercicios": [("Subir pelas inversões", "C: fundamental, 1ª, 2ª, fundamental na oitava de cima.", "4 min · 60 BPM"),
                       ("Mesmo exercício com F e G", "Mãos separadas, depois juntas.", "5 min · 60 BPM"),
                       ("I – IV – V – I suave", "C–E–G → C–F–A → B–D–G → C–E–G.", "5 min · 70 BPM"),
                       ("Baixo invertido", "Mão esquerda toca Mi enquanto a direita toca Dó: C/E.", "4 min")],
        "erros": [("Mão pulando entre acordes", "Procure a inversão mais próxima do acorde anterior."),
                  ("Dedilhado sempre 1-3-5", "Nas inversões use o que for confortável (ex.: 1-2-5)."),
                  ("Confundir C/E com inversão da mão direita", "C/E = baixo Mi na mão esquerda."),
                  ("Notas de baixo muito fortes", "Equilibre: a melodia de cima deve aparecer.")],
        "resumo": ["Fundamental: tônica embaixo. 1ª inversão: terça embaixo. 2ª: quinta embaixo.",
                   "Inversões reduzem o movimento da mão.", "Mantenha as notas em comum entre os acordes.",
                   "C/E indica o baixo Mi na mão esquerda."],
    },
    {
        "slug": "dominio-do-metronomo",
        "titulo": "Domínio do metrônomo: 70 e 140 BPM",
        "sub": "Manter o tempo firme no lento e no rápido.",
        "objetivos": ["Tocar com firmeza em 70 BPM", "Entender a relação entre 70 e 140 BPM",
                      "Usar subdivisões", "Tocar com o clique nos tempos 2 e 4"],
        "p1": """
<h2>70 e 140: o dobro</h2>
<p>140 BPM é exatamente o dobro de 70. Tocar colcheias em 70 BPM tem a mesma velocidade de notas que semínimas em 140. Treinar os dois andamentos mostra se o seu tempo é firme mesmo quando a música “corre”.</p>
""" + tabela(["Exercício", "Em 70 BPM", "Em 140 BPM"],
             [["Semínimas (1 por clique)", "lento, controle", "rápido, energia"],
              ["Colcheias (2 por clique)", "= semínimas em 140", "muito rápido"],
              ["Clique só no 2 e 4", "sensação de groove", "rock/pop animado"]]) + """
<h2>Subdivisão: o segredo do tempo firme</h2>
<p>Em andamentos lentos, o maior erro é correr. Para evitar, pense nas subdivisões: conte “1 e 2 e 3 e 4 e” mesmo tocando só no 1. Em andamentos rápidos, relaxe a mão e pense em grupos (1–2, 3–4).</p>
<div class="call"><b class="t">Clique no 2 e 4</b>Configure o metrônomo a 70 BPM e imagine que cada clique é o tempo 2 e o 4 de um compasso em 140. É como tocar com a caixa da bateria: excelente para groove.</div>
""",
        "passos": ["Em 70 BPM, toque acordes em semínimas por 2 minutos sem acelerar.", "Ainda em 70, toque colcheias (2 por clique).",
                   "Mude para 140 BPM e toque semínimas: compare com as colcheias de 70.",
                   "Em 70, imagine o clique como 2 e 4 e toque no 1 e 3 “entre” os cliques.", "Grave-se e confira se o tempo ficou estável."],
        "exercicios": [("Lento sem correr", "C – G – Am – F em semínimas.", "4 min · 70 BPM"),
                       ("Colcheias", "Mesma progressão em colcheias.", "4 min · 70 BPM"),
                       ("Rápido e relaxado", "Semínimas com a mão solta.", "4 min · 140 BPM"),
                       ("Groove no 2 e 4", "Clique como caixa da bateria.", "5 min · 70 BPM")],
        "erros": [("Correr no lento", "Conte a subdivisão em voz alta."), ("Tensionar no rápido", "Ombros e punhos soltos; toque mais leve."),
                  ("Perder o clique e continuar", "Pare, escute 4 cliques e recomece."), ("Nunca se gravar", "A gravação mostra o que o ouvido não percebe.")],
        "resumo": ["140 BPM = o dobro de 70.", "Subdivida para não correr no lento.", "Relaxe para não travar no rápido.",
                   "Clique no 2 e 4 desenvolve o groove."],
    },
    {
        "slug": "dinamica-musical",
        "titulo": "Domínio de dinâmica musical",
        "sub": "Saber a hora de crescer e de abaixar a intensidade da música.",
        "objetivos": ["Conhecer os sinais de dinâmica", "Controlar a força do toque", "Fazer crescendo e decrescendo",
                      "Aplicar a dinâmica nas partes da música"],
        "p1": """
<h2>Dinâmica é a intensidade do som</h2>
<p>Uma música não fica no mesmo volume o tempo todo. A <b>dinâmica</b> é a variação entre o suave e o forte, e é ela que faz a música respirar e emocionar.</p>
""" + tabela(["Sinal", "Nome", "Significado"],
             [["pp", "pianíssimo", "muito suave"], ["p", "piano", "suave"], ["mp", "mezzo piano", "meio suave"],
              ["mf", "mezzo forte", "meio forte"], ["f", "forte", "forte"], ["ff", "fortíssimo", "muito forte"],
              ["&lt;", "crescendo", "aumentar aos poucos"], ["&gt;", "decrescendo", "diminuir aos poucos"]]) + """
<h2>Como controlar no teclado</h2>
<p>Com o teclado sensitivo ligado, o volume depende da <b>velocidade</b> com que a tecla desce, não de apertar mais. Também dá para mudar a intensidade tocando mais ou menos notas: no suave, poucas notas e acordes longos; no forte, oitavas, ritmo e mais notas.</p>
<div class="call"><b class="t">Na música</b>Verso suave (p–mp), pré-refrão crescendo, refrão forte (f), ponte variando e final voltando ao suave. Observe a banda e quem conduz.</div>
""",
        "passos": ["Ligue a função sensitiva (TOUCH) do teclado.", "Toque o acorde de C em p, mp, mf e f, sentindo a diferença.",
                   "Faça um crescendo: 8 acordes, cada um um pouco mais forte.", "Faça o decrescendo voltando ao suave.",
                   "Toque uma música aplicando a dinâmica: verso p, refrão f."],
        "exercicios": [("Escada de volume", "pp → ff em 6 acordes e volta.", "4 min · 60 BPM"),
                       ("Crescendo de 4 compassos", "C – G – Am – F crescendo do p ao f.", "4 min · 70 BPM"),
                       ("Mais e menos notas", "Verso com acordes simples, refrão com oitavas na esquerda.", "5 min"),
                       ("Música com dinâmica", "Uma música inteira com um mapa de dinâmica escrito.", "8 min")],
        "erros": [("Tudo no mesmo volume", "Escreva p, mf e f no mapa da música."), ("Forte = apertar e tensionar", "Forte vem da velocidade, com o braço solto."),
                  ("Crescendo repentino", "Cresça aos poucos, ao longo de vários compassos."), ("Cobrir a voz", "O teclado acompanha: no verso, deixe espaço para quem canta.")],
        "resumo": ["Dinâmica = variação de intensidade.", "pp p mp mf f ff; &lt; crescendo, &gt; decrescendo.",
                   "Volume vem da velocidade do toque e da quantidade de notas.", "Verso suave, refrão forte, final suave."],
    },
    {
        "slug": "leitura-de-cifra",
        "titulo": "Leitura de cifra",
        "sub": "Entender todos os símbolos que aparecem numa cifra.",
        "objetivos": ["Ler acordes maiores, menores e com sétima", "Entender acordes com baixo (C/E)",
                      "Reconhecer sus, dim, 9 e outros símbolos", "Seguir uma cifra completa sem se perder"],
        "p1": """
<h2>O que cada símbolo quer dizer</h2>
""" + tabela(["Cifra", "Nome", "Notas (exemplo em C)"],
             [["C", "Dó maior", "C – E – G"], ["Cm", "Dó menor", "C – E♭ – G"], ["C7", "Dó com sétima (menor)", "C – E – G – B♭"],
              ["C7M (Cmaj7)", "Dó com sétima maior", "C – E – G – B"], ["Cm7", "Dó menor com sétima", "C – E♭ – G – B♭"],
              ["C9 / Cadd9", "Dó com nona", "C – E – G – D"], ["Csus4", "Dó com quarta suspensa", "C – F – G"],
              ["C°", "Dó diminuto", "C – E♭ – G♭"], ["C/E", "Dó com baixo em Mi", "baixo E, acorde C"]]) + """
<h2>Lendo a cifra de uma música</h2>
<p>Na cifra, o acorde aparece <b>em cima da sílaba</b> onde ele muda. Quando há uma introdução ou parte instrumental, os acordes vêm em sequência, às vezes com “x2” (repetir duas vezes).</p>
<div class="call"><b class="t">A barra é sobre o baixo</b>Em C/E, a letra antes da barra é o acorde da mão direita; a letra depois da barra é a nota grave da mão esquerda.</div>
""",
        "passos": ["Leia a cifra inteira antes de tocar e marque os acordes que você não conhece.", "Monte cada acorde novo com a tabela.",
                   "Toque só a sequência de acordes, sem cantar.", "Cante (ou ouça a música) e troque o acorde na sílaba indicada.",
                   "Toque a música inteira seguindo a cifra."],
        "exercicios": [("Sétimas", "C7, C7M, Cm7, G7: monte e ouça a diferença.", "5 min"),
                       ("Baixo invertido", "C – C/B – Am – Am/G (baixo descendo).", "5 min · 60 BPM"),
                       ("sus4 resolvendo", "Csus4 → C, Gsus4 → G.", "3 min"),
                       ("Cifra real", "Toque uma cifra inteira do repertório.", "8 min")],
        "erros": [("Ignorar o 7 ou o 9", "Ao menos toque a tríade; depois acrescente a nota."),
                  ("Confundir C/E com C e E", "A barra indica o baixo, não dois acordes."), ("Trocar o acorde atrasado", "Olhe a sílaba onde o acorde muda."),
                  ("Confundir 7 com 7M", "7 = sétima menor (B♭ em C); 7M = sétima maior (B em C).")],
        "resumo": ["m = menor; 7 = sétima menor; 7M = sétima maior.", "sus4 troca a terça pela quarta; ° = diminuto.",
                   "C/E = acorde C com baixo Mi.", "O acorde muda na sílaba onde está escrito."],
    },
    {
        "slug": "escolha-de-timbres",
        "titulo": "Escolha de timbres",
        "sub": "Usar o som certo para cada momento da música.",
        "objetivos": ["Conhecer os timbres mais usados", "Saber quando usar cada um", "Usar camadas (layer) e divisão (split)",
                      "Equilibrar o volume com a banda"],
        "p1": """
<h2>O timbre muda o clima</h2>
<p><b>Timbre</b> é a “cor” do som: o mesmo acorde soa diferente num piano, num órgão ou em cordas. Escolher bem o timbre é tão importante quanto tocar as notas certas.</p>
""" + tabela(["Timbre", "Quando usar", "Cuidado"],
             [["Piano acústico", "Base de quase tudo; verso, balada", "Pode ficar seco sozinho em momentos longos"],
              ["Piano elétrico (EP)", "Músicas suaves, groove, pop", "Volume baixo para não embolar"],
              ["Pad / cordas", "Fundo, sustentação, momentos de oração", "Toque acordes longos, poucas notas"],
              ["Órgão", "Músicas tradicionais, gospel, celebração", "Muito presente: controle o volume"],
              ["Synth / lead", "Introduções, solos, frases", "Use pouco, para destacar"]]) + """
<h2>Layer e split</h2>
<p><b>Layer</b> (camada) toca dois timbres ao mesmo tempo, como piano + pad. <b>Split</b> (divisão) separa o teclado: um timbre na mão esquerda e outro na direita, como baixo na esquerda e piano na direita.</p>
<div class="call"><b class="t">Menos é mais</b>Se a banda já tem violão e guitarra, o pad sustentando acordes longos costuma funcionar melhor do que piano cheio. Ouça o que falta no som do grupo.</div>
""",
        "passos": ["Escolha o piano como timbre base e salve num registro (memória) do teclado.", "Crie um layer piano + pad com o pad mais baixo.",
                   "Crie um split com baixo na mão esquerda.", "Toque a mesma progressão em 3 timbres e compare o clima.",
                   "Defina os timbres de cada parte de uma música do repertório."],
        "exercicios": [("Passeio de timbres", "C – Am – F – G em piano, EP, pad e órgão.", "5 min"),
                       ("Layer equilibrado", "Piano + pad: ajuste o volume até o pad ficar no fundo.", "4 min"),
                       ("Split com baixo", "Baixo na esquerda, acordes na direita.", "5 min · 70 BPM"),
                       ("Registros da música", "Salve os timbres de uma música nos registros do teclado.", "5 min")],
        "erros": [("Mudar de timbre a toda hora", "Escolha poucos timbres e mantenha."), ("Pad muito alto", "O pad é fundo: deve ser sentido, não destacado."),
                  ("Tocar muitas notas no pad", "Acordes longos e simples."), ("Esquecer de salvar os registros", "Salve para trocar rápido no meio da música.")],
        "resumo": ["Timbre é a cor do som e muda o clima.", "Piano é a base; pad sustenta; órgão celebra.",
                   "Layer = dois timbres juntos; split = divide o teclado.", "Equilibre com a banda: menos é mais."],
    },
    {
        "slug": "velocidade-e-agilidade",
        "titulo": "Velocidade e agilidade",
        "sub": "Ganhar velocidade sem perder precisão nem criar tensão.",
        "objetivos": ["Entender como a velocidade se desenvolve", "Treinar escalas e arpejos com metrônomo",
                      "Usar ritmos variados para acelerar", "Evitar tensão e lesões"],
        "p1": """
<h2>Velocidade é consequência</h2>
<p>A velocidade não vem de forçar: vem de movimentos <b>pequenos, relaxados e repetidos</b> com precisão. Primeiro a mão aprende o caminho devagar; depois, aos poucos, ela consegue fazer o mesmo caminho mais rápido.</p>
""" + tabela(["Exercício", "Como fazer", "Meta"],
             [["Escalas", "Dó, Sol, Ré e Fá, duas oitavas, mãos juntas", "semínimas a 60 → colcheias a 80"],
              ["Arpejos", "C–E–G–C subindo e descendo, 2 oitavas", "notas iguais e ligadas"],
              ["Ritmos pontuados", "Toque a escala em “longa-curta” e “curta-longa”", "dedos independentes"],
              ["Grupos rápidos", "4 notas rápidas e pausa, depois 8", "rapidez sem tensão"]]) + """
<div class="call"><b class="t">Regra dos 5 BPM</b>Quando tocar 3 vezes seguidas sem erro, suba 5 BPM. Se errar, volte 10. Anote o BPM do dia no caderno para ver a evolução.</div>
<div class="call warm"><b class="t">Atenção ao corpo</b>Dor no punho, no antebraço ou formigamento são sinais para parar. Faça pausas a cada 15 minutos e alongue.</div>
""",
        "passos": ["Aqueça as mãos por 2 minutos.", "Toque a escala de Dó em semínimas a 60 BPM, mãos juntas.",
                   "Toque a mesma escala em ritmo pontuado (longa-curta) e depois (curta-longa).", "Volte ao ritmo normal: ficou mais fácil.",
                   "Suba 5 BPM e repita. Anote o maior BPM sem erros."],
        "exercicios": [("Escala com metrônomo", "Dó maior, 2 oitavas, mãos juntas.", "5 min · 60 → 80 BPM"),
                       ("Arpejos", "C, F, G e Am, 2 oitavas.", "5 min · 60 BPM"),
                       ("Ritmos pontuados", "Escala de Sol em longa-curta e curta-longa.", "4 min · 60 BPM"),
                       ("Registro de evolução", "Anote o BPM máximo limpo de cada exercício.", "1 min")],
        "erros": [("Acelerar sem controle", "Use o metrônomo e a regra dos 5 BPM."), ("Levantar os dedos demais", "Dedos perto das teclas: movimentos pequenos."),
                  ("Tensionar ombros e punhos", "Pare, solte os braços e recomece mais devagar."), ("Treinar só o que já sabe", "Dedique tempo ao trecho mais difícil.")],
        "resumo": ["Velocidade vem de precisão e relaxamento.", "Escalas, arpejos e ritmos pontuados com metrônomo.",
                   "Suba 5 BPM após 3 vezes sem erro.", "Dor é sinal para parar."],
    },
]
