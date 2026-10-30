"""Conteúdo do material didático do módulo Teclado 2 (um tópico por PDF)."""
from gerar import teclado, figura, pauta
from teclado1 import linha_tempo

MODULO = "Teclado 2"
PASTA = "teclado-2"

ESCALA_DO = teclado({"C0": ("1", "d"), "D0": ("2", "d"), "E0": ("3", "d"), "F0": ("1", "d"), "G0": ("2", "d"),
                     "A0": ("3", "d"), "B0": ("4", "d"), "C1": ("5", "d")}, letras=True,
                    legenda="Escala de Dó maior com a digitação da mão direita: 1-2-3, passa o polegar, 1-2-3-4-5")


def tabela(cab, linhas):
    h = "<table><tr>" + "".join(f"<th>{c}</th>" for c in cab) + "</tr>"
    for l in linhas:
        h += "<tr>" + "".join(f"<td>{c}</td>" for c in l) + "</tr>"
    return h + "</table>"


TOPICOS = [
    {
        "slug": "regra-t-t-st",
        "titulo": "Regra do T T ST T T T ST",
        "sub": "A fórmula que monta qualquer escala maior.",
        "objetivos": ["Entender o que é tom e semitom", "Decorar a fórmula da escala maior",
                      "Montar a escala maior a partir de qualquer nota", "Conferir a escala pelo som"],
        "p1": """
<h2>Tom e semitom</h2>
<p><b>Semitom (ST)</b> é a menor distância entre duas teclas: de uma tecla para a vizinha, contando brancas e pretas. <b>Tom (T)</b> são dois semitons, ou seja, pula uma tecla no meio.</p>
<p>Entre as teclas brancas, quase sempre há uma preta no meio (distância de um tom). As exceções são <b>Mi–Fá</b> e <b>Si–Dó</b>: não há tecla preta entre elas, então a distância é de um semitom.</p>
<h2>A fórmula da escala maior</h2>
<p>Toda escala maior segue a mesma sequência de distâncias entre uma nota e a próxima:</p>
<div class="call"><b class="t" style="font-size:16pt;letter-spacing:.06em">T · T · ST · T · T · T · ST</b>Tom, tom, semitom, tom, tom, tom, semitom. São 7 passos que levam da tônica até a mesma nota uma oitava acima.</div>
""" + figura(teclado({"C0": ("1", "n"), "D0": ("2", "n"), "E0": ("3", "n"), "F0": ("4", "n"), "G0": ("5", "n"), "A0": ("6", "n"), "B0": ("7", "n"), "C1": ("8", "n")}, letras=True),
             "Dó maior usa só teclas brancas: Dó T Ré T Mi ST Fá T Sol T Lá T Si ST Dó.") + """
<p>Em Dó, os semitons caem exatamente em Mi–Fá e Si–Dó, por isso a escala sai toda em teclas brancas. Começando de outra nota, a fórmula obriga a usar teclas pretas.</p>
""",
        "passos": ["Escolha a tônica, por exemplo Sol.", "Dê um tom (pule uma tecla): Sol → Lá. Mais um tom: Lá → Si.",
                   "Semitom (tecla vizinha): Si → Dó.", "Três tons seguidos: Dó → Ré → Mi → Fá♯.",
                   "Último semitom: Fá♯ → Sol. Escala de Sol maior: Sol Lá Si Dó Ré Mi Fá♯ Sol."],
        "exercicios": [("Contar no teclado", "Aponte tom e semitom entre várias notas, falando em voz alta.", "3 min"),
                       ("Dó maior falando a fórmula", "Toque a escala dizendo T, T, ST… a cada passo.", "3 min · 60 BPM"),
                       ("Montar Sol e Ré maior", "Use a fórmula para descobrir as teclas pretas de cada uma.", "5 min"),
                       ("Montar Fá maior", "Descubra por que aparece o Si♭ (e não o Si).", "4 min")],
        "erros": [("Contar Mi–Fá como um tom", "Entre Mi e Fá não há tecla preta: é semitom."),
                  ("Pular a tecla preta na contagem", "Semitom é sempre a tecla vizinha, branca ou preta."),
                  ("Esquecer o último ST", "A escala tem 7 passos e termina na tônica, uma oitava acima."),
                  ("Decorar sem ouvir", "Toque a escala devagar: se alguma nota soar “estranha”, confira a fórmula.")],
        "resumo": ["Semitom = tecla vizinha; tom = dois semitons.", "Mi–Fá e Si–Dó são semitons naturais.",
                   "Escala maior: T T ST T T T ST.", "A fórmula vale a partir de qualquer nota."],
    },
    {
        "slug": "escalas-maiores",
        "titulo": "Escalas maiores",
        "sub": "Tocar as escalas com a digitação certa, nas duas mãos.",
        "objetivos": ["Tocar Dó maior com a passagem do polegar", "Tocar Sol, Ré e Fá maior",
                      "Usar a digitação da mão esquerda", "Treinar escalas com o metrônomo"],
        "p1": """
<h2>Por que estudar escalas</h2>
<p>As escalas treinam agilidade, independência dos dedos e o ouvido para cada tonalidade. Quase todas as melodias e acordes de uma música saem da escala do tom em que ela está.</p>
<h2>A digitação de Dó maior</h2>
<p>Como a mão só tem 5 dedos e a escala tem 8 notas, usamos a <b>passagem do polegar</b>: na mão direita, toque Dó–Ré–Mi com 1-2-3 e passe o polegar por baixo da mão para tocar o Fá. Continue com 1-2-3-4-5 até o Dó.</p>
""" + figura(ESCALA_DO, "Subindo: 1-2-3-1-2-3-4-5. Descendo, o dedo 3 cruza por cima do polegar.") + tabela(
            ["Escala", "Notas", "Mão direita", "Mão esquerda"],
            [["Dó maior", "Dó Ré Mi Fá Sol Lá Si Dó", "1 2 3 1 2 3 4 5", "5 4 3 2 1 3 2 1"],
             ["Sol maior", "Sol Lá Si Dó Ré Mi Fá♯ Sol", "1 2 3 1 2 3 4 5", "5 4 3 2 1 3 2 1"],
             ["Ré maior", "Ré Mi Fá♯ Sol Lá Si Dó♯ Ré", "1 2 3 1 2 3 4 5", "5 4 3 2 1 3 2 1"],
             ["Fá maior", "Fá Sol Lá Si♭ Dó Ré Mi Fá", "1 2 3 4 1 2 3 4", "5 4 3 2 1 3 2 1"]]),
        "passos": ["Toque Dó maior só com a mão direita, bem devagar, subindo e descendo.",
                   "Na passagem do polegar, mantenha o punho reto: o polegar passa por baixo, sem a mão “pular”.",
                   "Faça a mão esquerda: 5-4-3-2-1, o dedo 3 cruza por cima, e 3-2-1.",
                   "Junte as duas mãos numa oitava, devagar.", "Repita com Sol, Ré e Fá maior."],
        "exercicios": [("Passagem do polegar", "Só Mi–Fá (3 → 1) e volta, 10 vezes, sem ruído.", "3 min"),
                       ("Dó maior, mãos separadas", "Uma nota por batida, subindo e descendo.", "5 min · 60 BPM"),
                       ("Dó maior, mãos juntas", "Uma oitava, depois duas.", "5 min · 60 BPM"),
                       ("Sol, Ré e Fá", "Mãos separadas, com atenção às teclas pretas.", "6 min · 60 BPM")],
        "erros": [("Mão pula na passagem do polegar", "Prepare o polegar embaixo da mão enquanto toca o dedo 3."),
                  ("Esquecer o Fá♯ em Sol maior", "Antes de tocar, diga as notas em voz alta."),
                  ("Notas com volumes diferentes", "Mais devagar: cada nota igual à anterior."),
                  ("Acelerar na descida", "Use o metrônomo do começo ao fim.")],
        "resumo": ["Escalas treinam agilidade, dedos e ouvido.", "Passagem do polegar: 1-2-3, polegar por baixo, 1-2-3-4-5.",
                   "Mão esquerda: 5-4-3-2-1, o 3 cruza por cima, 3-2-1.", "Fá maior tem Si♭; Sol tem Fá♯; Ré tem Fá♯ e Dó♯."],
    },
    {
        "slug": "campo-harmonico",
        "titulo": "Campo harmônico",
        "sub": "Os acordes que “combinam” em cada tom e como usá-los nas músicas.",
        "objetivos": ["Entender o que é campo harmônico", "Montar o campo harmônico de Dó",
                      "Conhecer os campos dos tons mais usados", "Tocar progressões comuns"],
        "p1": """
<h2>Acordes que moram na escala</h2>
<p><b>Campo harmônico</b> é o conjunto de acordes formados usando só as notas de uma escala. Em cada nota da escala montamos uma tríade (pulando uma nota da escala), e o resultado são 7 acordes que soam bem juntos naquele tom.</p>
<p>A escala de cada tom também é a base: Dó (C D E F G A B), Ré (D E F♯ G A B C♯), Mi (E F♯ G♯ A B C♯ D♯), Fá (F G A B♭ C D E), Sol (G A B C D E F♯), Lá (A B C♯ D E F♯ G♯) e Si (B C♯ D♯ E F♯ G♯ A♯).</p>
""" + tabela(["Tom", "I", "II", "III", "IV", "V", "VI", "VII"],
             [["<b>C</b>", "C", "Dm", "Em", "F", "G", "Am", "B°"],
              ["<b>D</b>", "D", "Em", "F♯m", "G", "A", "Bm", "C♯°"],
              ["<b>E</b>", "E", "F♯m", "G♯m", "A", "B", "C♯m", "D♯°"],
              ["<b>F</b>", "F", "Gm", "Am", "B♭", "C", "Dm", "E°"],
              ["<b>G</b>", "G", "Am", "Bm", "C", "D", "Em", "F♯°"],
              ["<b>A</b>", "A", "Bm", "C♯m", "D", "E", "F♯m", "G♯°"]]) + """
<div class="call"><b class="t">Para que serve na prática</b>Se você sabe o tom da música, já sabe quais acordes devem aparecer. Isso ajuda a ler cifras, tirar músicas de ouvido e improvisar. O símbolo ° indica acorde diminuto.</div>
""",
        "passos": ["Escreva a escala de Dó: C D E F G A B.", "Em cada nota, monte uma tríade pulando uma nota: C-E-G, D-F-A, E-G-B…",
                   "Veja se cada acorde ficou maior, menor ou diminuto (conte os semitons).",
                   "Toque os 7 acordes em sequência, subindo.", "Toque a progressão I – V – VI – IV (C – G – Am – F)."],
        "exercicios": [("Campo de Dó subindo", "C Dm Em F G Am B°, um acorde por tempo.", "4 min · 60 BPM"),
                       ("I – IV – V – I", "Em C, G e D. Uma das progressões mais comuns.", "5 min · 60 BPM"),
                       ("I – V – VI – IV", "C – G – Am – F e depois em G: G – D – Em – C.", "5 min · 70 BPM"),
                       ("Descubra o campo", "Monte o campo de Fá sozinho e confira com a tabela.", "4 min")],
        "erros": [("Achar que todo acorde do tom é maior", "Segundo, terceiro e sexto graus são menores."),
                  ("Usar Si maior no campo de Dó", "O sétimo grau é diminuto: B° (Si – Ré – Fá)."),
                  ("Esquecer os sustenidos do tom", "Os acordes usam só notas da escala daquele tom."),
                  ("Decorar a tabela sem tocar", "Toque cada campo; o ouvido ajuda a memória.")],
        "resumo": ["Campo harmônico = 7 acordes feitos com as notas da escala.", "Graus I, IV e V são maiores; II, III e VI menores; VII diminuto.",
                   "Sabendo o tom, você sabe quais acordes esperar.", "Progressões comuns: I–IV–V–I e I–V–VI–IV."],
    },
    {
        "slug": "tons-musicais",
        "titulo": "Tons musicais",
        "sub": "O que é o “tom” de uma música e como descobrir em qual tom ela está.",
        "objetivos": ["Diferenciar tom (distância) de tom (tonalidade)", "Entender o que é a tônica de uma música",
                      "Descobrir o tom de uma música pela cifra", "Perceber o tom pelo ouvido"],
        "p1": """
<h2>Duas palavras iguais, dois sentidos</h2>
<p>Na música, “tom” tem dois significados. Um é a <b>distância</b> de dois semitons, que você já usou na fórmula T T ST. O outro é a <b>tonalidade</b>: o centro da música, a nota e o acorde para onde tudo “volta”. Quando alguém diz “essa música está em Sol”, está falando da tonalidade.</p>
<p>A nota principal da tonalidade é a <b>tônica</b>. O acorde da tônica dá a sensação de chegada e repouso; os outros acordes criam movimento e voltam para ele.</p>
""" + tabela(["Pista", "O que observar"],
             [["Último acorde", "Quase sempre a música termina no acorde da tônica."],
              ["Primeiro acorde", "Muitas músicas começam na tônica."],
              ["Acordes da cifra", "Compare com os campos harmônicos: o tom é aquele que contém todos (ou quase todos) os acordes."],
              ["Sensação de repouso", "Cante a última nota da melodia: geralmente é a tônica."]]) + """
<div class="call"><b class="t">Tom de homem e tom de mulher</b>Mudar o tom de uma música (transpor) ajuda a encaixá-la na voz de quem canta. A melodia é a mesma, só mais grave ou mais aguda.</div>
""",
        "passos": ["Pegue a cifra de uma música que você conhece.", "Anote o primeiro e o último acorde.",
                   "Liste todos os acordes que aparecem.", "Procure na tabela de campo harmônico qual tom contém esses acordes.",
                   "Toque o acorde da tônica no fim da música e sinta o repouso."],
        "exercicios": [("Tom pela cifra", "Descubra o tom de 3 cifras diferentes.", "6 min"),
                       ("Repouso", "Toque C – F – G e pare no G; depois termine no C. Qual soa “resolvido”?", "3 min"),
                       ("Cantar a tônica", "Com uma música tocando, cante a nota que parece o “chão”.", "4 min"),
                       ("Mesma música em dois tons", "Toque I – IV – V – I em C e em G.", "4 min · 60 BPM")],
        "erros": [("Confundir tom (distância) com tom (tonalidade)", "Pergunte: é distância entre notas ou o centro da música?"),
                  ("Achar que o tom é sempre o primeiro acorde", "Confira o último acorde e o campo harmônico."),
                  ("Ignorar acordes menores", "Am pode estar em C; Em pode estar em G. Compare com a tabela."),
                  ("Escolher um tom que não cabe na voz", "Teste a parte mais aguda da música antes de fechar o tom.")],
        "resumo": ["“Tom” pode ser distância (2 semitons) ou tonalidade (o centro da música).",
                   "Tônica = nota e acorde de repouso.", "Pistas: último acorde, primeiro acorde e campo harmônico.",
                   "Transpor muda o tom para caber na voz."],
    },
    {
        "slug": "tempo-musical",
        "titulo": "Tempo musical: 4/4, 3/4 e 6/8",
        "sub": "Como contar os compassos mais comuns e sentir onde cai o tempo forte.",
        "objetivos": ["Entender a fórmula de compasso", "Contar 4/4, 3/4 e 6/8",
                      "Sentir o tempo forte de cada compasso", "Tocar acordes no ritmo certo"],
        "p1": """
<h2>A fórmula de compasso</h2>
<p>No início da partitura aparece uma fração, como 4/4. O número de cima diz <b>quantos tempos</b> tem cada compasso; o de baixo diz <b>qual figura vale um tempo</b> (4 = semínima, 8 = colcheia).</p>
""" + tabela(["Compasso", "Como contar", "Tempo forte", "Sensação"],
             [["<b>4/4</b>", "1 – 2 – 3 – 4", "1 (e o 3, mais leve)", "O mais comum: pop, louvor, rock"],
              ["<b>3/4</b>", "1 – 2 – 3", "1", "Valsa, balanço de “um-dois-três”"],
              ["<b>6/8</b>", "1 2 3 – 4 5 6", "1 e 4", "Balanço em dois grupos de três, mais embalado"]]) + figura(
            linha_tempo(4, ["C", "G", "Am", "F"]), "Em 4/4, cada compasso tem 4 tempos; o acorde muda no 1.") + """
<div class="call"><b class="t">Como sentir o 6/8</b>Conte “<b>1</b> 2 3 <b>4</b> 5 6” acentuando o 1 e o 4. Parece que há dois pulsos grandes, cada um dividido em três.</div>
""",
        "passos": ["Ligue o metrônomo em 70 BPM e conte 4/4 em voz alta, batendo o pé no 1.",
                   "Toque o acorde de Dó no 1 e repita nos tempos 2, 3 e 4.", "Mude para 3/4: conte 1-2-3, acorde no 1 e nos tempos 2 e 3 mais leves.",
                   "Para o 6/8, conte 1 a 6 acentuando 1 e 4.", "Toque C – G – Am – F em cada compasso."],
        "exercicios": [("Palmas no 4/4", "Palma forte no 1, fraca no 2, 3 e 4.", "2 min · 70 BPM"),
                       ("Valsa em 3/4", "Mão esquerda no 1, mão direita no 2 e 3: C – F – G – C.", "5 min · 80 BPM"),
                       ("Balanço em 6/8", "Acorde no 1 e no 4, contando em voz alta.", "5 min · 60 BPM"),
                       ("Qual é o compasso?", "Ouça 3 músicas e descubra se estão em 4/4, 3/4 ou 6/8.", "4 min")],
        "erros": [("Perder a conta no meio do compasso", "Conte em voz alta até ficar automático."),
                  ("Tratar 6/8 como 3/4", "No 6/8 há dois pulsos fortes (1 e 4)."),
                  ("Todos os tempos com a mesma força", "Acentue o tempo 1 para o ritmo “respirar”."),
                  ("Trocar de acorde fora do 1", "Prepare a mão no último tempo do compasso.")],
        "resumo": ["Número de cima = tempos por compasso; de baixo = figura que vale um tempo.",
                   "4/4: 1-2-3-4. 3/4: 1-2-3. 6/8: 1 2 3 4 5 6, com acento no 1 e no 4.",
                   "O tempo 1 é o mais forte.", "Conte em voz alta com o metrônomo."],
    },
    {
        "slug": "regra-das-escalas",
        "titulo": "Regra das escalas: maior, menor, menor, maior, maior, menor, diminuto",
        "sub": "A sequência que se repete em todo campo harmônico maior.",
        "objetivos": ["Decorar a sequência de tipos de acorde", "Aplicar a regra em qualquer tom",
                      "Montar o campo harmônico sem tabela", "Reconhecer os graus nas músicas"],
        "p1": """
<h2>A regra que não muda</h2>
<p>Em qualquer escala maior, os acordes formados em cada grau seguem sempre a mesma ordem de tipos:</p>
<div class="call"><b class="t" style="font-size:14pt">Maior · menor · menor · Maior · Maior · menor · diminuto</b>I · ii · iii · IV · V · vi · vii°. Muda o tom, muda o nome das notas, mas a ordem é a mesma.</div>
""" + tabela(["Grau", "I", "ii", "iii", "IV", "V", "vi", "vii°"],
             [["Tipo", "Maior", "menor", "menor", "Maior", "Maior", "menor", "diminuto"],
              ["Em C", "C", "Dm", "Em", "F", "G", "Am", "B°"],
              ["Em G", "G", "Am", "Bm", "C", "D", "Em", "F♯°"],
              ["Em D", "D", "Em", "F♯m", "G", "A", "Bm", "C♯°"]]) + """
<h2>Como usar sem decorar tabela</h2>
<p>Basta saber a escala do tom e aplicar a regra: coloque o nome de cada nota da escala e acrescente “m” no 2º, 3º e 6º, e “°” no 7º. Pronto: você tem o campo harmônico.</p>
<p>Os números romanos também ajudam a conversar com outros músicos: “vai para o quarto grau” significa ir para o acorde IV do tom, qualquer que seja ele.</p>
""",
        "passos": ["Escreva a escala de Lá maior: A B C♯ D E F♯ G♯.", "Aplique a regra: A, Bm, C♯m, D, E, F♯m, G♯°.",
                   "Toque os 7 acordes subindo.", "Toque I – vi – IV – V nesse tom (A – F♯m – D – E).",
                   "Repita a regra com Mi maior."],
        "exercicios": [("Falar a regra", "Diga “maior, menor, menor, maior, maior, menor, diminuto” 5 vezes, tocando os graus em C.", "2 min"),
                       ("Campo de Lá", "Monte e toque o campo de A usando a regra.", "5 min · 60 BPM"),
                       ("Campo de Mi", "Monte e toque o campo de E.", "5 min · 60 BPM"),
                       ("Graus em música", "Numa cifra conhecida, escreva o grau de cada acorde.", "5 min")],
        "erros": [("Inverter a ordem (menor no IV)", "Repita a frase da regra antes de montar."),
                  ("Esquecer os acidentes da escala", "Monte a escala primeiro, com a fórmula T T ST T T T ST."),
                  ("Trocar diminuto por menor no 7º grau", "vii° tem terça menor e quinta diminuta (3 + 3 semitons)."),
                  ("Confundir grau com nota", "Grau é a posição na escala, não o nome da nota.")],
        "resumo": ["Regra: Maior, menor, menor, Maior, Maior, menor, diminuto.", "Vale para todas as escalas maiores.",
                   "Monte a escala e aplique a regra para ter o campo harmônico.", "Graus em romanos: I, ii, iii, IV, V, vi, vii°."],
    },
    {
        "slug": "leitura-da-partitura",
        "titulo": "Leitura da partitura",
        "sub": "Pentagrama, claves e o nome das notas nas linhas e espaços.",
        "objetivos": ["Conhecer o pentagrama", "Ler notas na clave de Sol", "Ler notas na clave de Fá",
                      "Achar no teclado a nota escrita"],
        "p1": """
<h2>O pentagrama</h2>
<p>A partitura usa cinco linhas, o <b>pentagrama</b>. As notas ficam nas linhas ou nos espaços entre elas; quanto mais alto no pentagrama, mais agudo o som. A <b>clave</b> no começo diz qual nota é qual: no teclado, a mão direita costuma ler a <b>clave de Sol</b> e a mão esquerda a <b>clave de Fá</b>.</p>
""" + figura(pauta([(0, "Mi"), (1, "Fá"), (2, "Sol"), (3, "Lá"), (4, "Si"), (5, "Dó"), (6, "Ré"), (7, "Mi"), (8, "Fá")], "Clave de Sol (mão direita)"),
             "Linhas da clave de Sol, de baixo para cima: Mi, Sol, Si, Ré, Fá. Espaços: Fá, Lá, Dó, Mi.") + figura(
            pauta([(0, "Sol"), (1, "Lá"), (2, "Si"), (3, "Dó"), (4, "Ré"), (5, "Mi"), (6, "Fá"), (7, "Sol"), (8, "Lá")], "Clave de Fá (mão esquerda)"),
            "Linhas da clave de Fá: Sol, Si, Ré, Fá, Lá. Espaços: Lá, Dó, Mi, Sol.") + """
<div class="call"><b class="t">Dó central</b>O Dó do meio do teclado fica numa linha suplementar logo abaixo do pentagrama da clave de Sol, e logo acima do da clave de Fá. É o ponto de encontro das duas mãos.</div>
""",
        "passos": ["Leia as linhas da clave de Sol de baixo para cima: Mi, Sol, Si, Ré, Fá.", "Leia os espaços: Fá, Lá, Dó, Mi.",
                   "Ache no teclado o Dó central e, a partir dele, as notas da clave de Sol.",
                   "Faça o mesmo com a clave de Fá, abaixo do Dó central.", "Leia uma melodia simples nota por nota, devagar."],
        "exercicios": [("Linhas e espaços", "Diga o nome das notas em voz alta, sem tocar.", "3 min"),
                       ("Da partitura para o teclado", "Leia 10 notas e toque cada uma no lugar certo.", "5 min"),
                       ("Clave de Fá", "Repita o exercício com a mão esquerda.", "5 min"),
                       ("Melodia curta", "Leia e toque uma melodia de 8 notas sem parar.", "4 min · 50 BPM")],
        "erros": [("Ler a clave de Fá como se fosse de Sol", "Confira a clave antes de ler: as notas mudam."),
                  ("Contar as linhas de cima para baixo", "Sempre de baixo para cima."),
                  ("Procurar a nota na oitava errada", "Comece pelo Dó central e conte a partir dele."),
                  ("Ler rápido e errar", "Leia devagar: precisão primeiro, velocidade depois.")],
        "resumo": ["Pentagrama = 5 linhas; mais alto = mais agudo.", "Clave de Sol: linhas Mi Sol Si Ré Fá; espaços Fá Lá Dó Mi.",
                   "Clave de Fá: linhas Sol Si Ré Fá Lá; espaços Lá Dó Mi Sol.", "Dó central liga as duas claves."],
    },
    {
        "slug": "metronomo-com-a-musica",
        "titulo": "Uso do metrônomo com a música",
        "sub": "Estudar com o metrônomo para tocar no tempo, do jeito que a música pede.",
        "objetivos": ["Saber o que é BPM", "Descobrir o andamento de uma música", "Estudar uma música devagar e ir acelerando",
                      "Tocar junto com a gravação"],
        "p1": """
<h2>BPM: batidas por minuto</h2>
<p>O metrônomo marca o pulso em <b>BPM</b> (batidas por minuto). 60 BPM é uma batida por segundo; 120 BPM, duas por segundo. Cada música tem um andamento: baladas ficam perto de 60–80 BPM, músicas animadas passam de 110 BPM.</p>
""" + tabela(["Andamento", "BPM aproximado", "Exemplo de uso"],
             [["Lento", "50 – 70", "Baladas, momentos de oração"],
              ["Moderado", "70 – 100", "A maioria das músicas de louvor e pop"],
              ["Rápido", "100 – 140", "Músicas de celebração, animadas"]]) + """
<h2>Devagar primeiro, depois no tempo real</h2>
<p>A regra de ouro: se você erra, está rápido demais. Diminua o BPM até tocar sem erro, e só então suba de 5 em 5. Assim a música entra certa na memória das mãos.</p>
<div class="call"><b class="t">Descobrir o BPM da música</b>Use a função “tap” do metrônomo (toque no ritmo da música) ou procure o andamento da canção na internet. Muitos aplicativos de metrônomo gratuitos têm essa função.</div>
""",
        "passos": ["Descubra o BPM original da música.", "Comece em uns 60% desse valor (ex.: música em 100 → estude em 60).",
                   "Toque a música inteira sem parar nesse andamento.", "Suba 5 BPM por vez, só quando tocar sem erros.",
                   "No andamento original, toque junto com a gravação."],
        "exercicios": [("Contar com o metrônomo", "Em 60 BPM, conte 1-2-3-4 em voz alta por 2 minutos.", "2 min"),
                       ("Progressão em 3 andamentos", "C – G – Am – F em 60, 70 e 80 BPM.", "6 min"),
                       ("Escada de BPM", "Uma música do repertório: de 60% até o original, de 5 em 5.", "10 min"),
                       ("Junto com a gravação", "Toque a música inteira com o áudio original.", "5 min")],
        "erros": [("Ligar o metrônomo e ignorar o clique", "Pare, escute 4 cliques e só então comece."),
                  ("Subir o BPM rápido demais", "Suba de 5 em 5, só sem erros."),
                  ("Desacelerar nas partes difíceis", "Estude a parte difícil separada, mais lenta."),
                  ("Nunca tocar com a gravação", "A gravação mostra a “sensação” real da música.")],
        "resumo": ["BPM = batidas por minuto.", "Comece devagar (≈ 60% do original) e suba de 5 em 5.",
                   "Errou? Está rápido demais.", "Termine tocando junto com a gravação."],
    },
    {
        "slug": "bemol-e-sustenido",
        "titulo": "Diferença entre bemol e sustenido",
        "sub": "Os sinais que sobem ou descem uma nota em meio-tom, e como chamamos as teclas pretas.",
        "objetivos": ["Entender o sustenido (♯) e o bemol (♭)", "Dar nome às teclas pretas",
                      "Saber o que são notas enarmônicas", "Conhecer a convenção usada nas cifras"],
        "p1": """
<h2>Subir e descer meio-tom</h2>
<p>O <b>sustenido (♯)</b> eleva uma nota em meio-tom, para a direita (mais agudo). O <b>bemol (♭)</b> abaixa uma nota em meio-tom, para a esquerda (mais grave). Por isso cada tecla preta tem dois nomes: ela é o sustenido da branca da esquerda e o bemol da branca da direita.</p>
""" + figura(teclado({"C#0": ("♯", "d"), "D#0": ("♯", "d"), "F#0": ("♯", "d"), "G#0": ("♯", "d"), "A#0": ("♯", "d")}, oitavas=1, ww=40, letras=True),
             "Teclas pretas: C♯/D♭, D♯/E♭, F♯/G♭, G♯/A♭, A♯/B♭.") + tabela(
            ["Tecla preta", "Como sustenido", "Como bemol", "Como escrevemos na cifra"],
            [["entre Dó e Ré", "C♯", "D♭", "C♯"], ["entre Ré e Mi", "D♯", "E♭", "<b>E♭</b>"], ["entre Fá e Sol", "F♯", "G♭", "F♯"],
             ["entre Sol e Lá", "G♯", "A♭", "G♯ (às vezes A♭)"], ["entre Lá e Si", "A♯", "B♭", "<b>B♭</b>"]]) + """
<div class="call"><b class="t">A convenção da nossa apostila</b>Na prática das cifras, costumamos chamar as teclas pretas de sustenido, com duas exceções muito usadas: <b>E♭ (Mi bemol)</b> e <b>B♭ (Si bemol)</b>. As duas formas estão certas, porque são a mesma tecla (notas <b>enarmônicas</b>); o nome escolhido depende do tom da música.</div>
""",
        "passos": ["Toque Dó e depois a tecla preta à direita: isso é Dó sustenido (C♯).", "Toque Ré e depois a preta à esquerda: Ré bemol (D♭). É a mesma tecla!",
                   "Dê os dois nomes a cada tecla preta da oitava.", "Note que Mi♯ cai na tecla Fá e Si♯ na tecla Dó (não há preta entre elas).",
                   "Leia uma cifra com E♭ e B♭ e encontre as teclas."],
        "exercicios": [("Dois nomes por tecla", "Aponte cada tecla preta e diga o nome em ♯ e em ♭.", "3 min"),
                       ("Subir e descer meio-tom", "A partir de várias notas, toque o ♯ e o ♭ de cada uma.", "4 min"),
                       ("Acordes com bemol", "Toque B♭ (B♭ – D – F) e E♭ (E♭ – G – B♭).", "5 min · 60 BPM"),
                       ("Caça às enarmônicas", "Encontre 5 pares de notas com nomes diferentes e mesma tecla.", "3 min")],
        "erros": [("Achar que sustenido é sempre tecla preta", "Mi♯ = tecla Fá; Si♯ = tecla Dó."),
                  ("Confundir a direção", "Sustenido sobe (direita); bemol desce (esquerda)."),
                  ("Achar que C♯ e D♭ são teclas diferentes", "Mesma tecla, nomes diferentes (enarmonia)."),
                  ("Estranhar E♭ e B♭ nas cifras", "É a convenção mais usada para essas duas teclas.")],
        "resumo": ["♯ sobe meio-tom; ♭ desce meio-tom.", "Cada tecla preta tem dois nomes (enarmonia).",
                   "Nas cifras: sustenidos na maioria das pretas, E♭ e B♭ como bemóis.", "Mi♯ = Fá e Si♯ = Dó no teclado."],
    },
]
