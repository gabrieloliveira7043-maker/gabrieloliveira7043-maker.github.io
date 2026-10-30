"""Conteúdo do material didático do módulo Teclado 4 (um tópico por PDF)."""
from gerar import teclado, figura
from teclado2 import tabela

MODULO = "Teclado 4"
PASTA = "teclado-4"

TOPICOS = [
    {
        "slug": "criatividade-musical",
        "titulo": "Criatividade musical",
        "sub": "Transformar a mesma sequência de acordes em acompanhamentos diferentes.",
        "objetivos": ["Variar ritmo, registro e textura", "Criar dedilhados a partir de um acorde",
                      "Usar notas de passagem no baixo", "Desenvolver um estilo próprio"],
        "p1": """
<h2>Criatividade tem ferramentas</h2>
<p>Ser criativo no teclado não é tocar notas aleatórias: é escolher, entre várias formas de tocar a mesma harmonia, a que serve melhor à música. Com uma única progressão (C – G – Am – F) dá para criar muitos acompanhamentos diferentes.</p>
""" + tabela(["Ferramenta", "O que mudar", "Exemplo"],
             [["Ritmo", "Quando o acorde é tocado", "Semínimas, colcheias, síncopes, acorde só no 1"],
              ["Registro", "Em que região do teclado", "Acordes graves no verso, agudos no refrão"],
              ["Textura", "Quantas notas ao mesmo tempo", "Notas soltas (arpejo) ou acorde cheio"],
              ["Inversões", "Ordem das notas", "Voz de cima formando uma melodia"],
              ["Baixo", "Nota da mão esquerda", "Baixo caminhando: C – B – A – G – F"],
              ["Notas extras", "Acrescentar 9ª, sus4, 7M", "C9, Gsus4 → G, Fmaj7"]]) + """
<div class="call"><b class="t">Ouça e copie, depois transforme</b>Escolha um tecladista que você admira, tente reproduzir um trecho e depois mude uma coisa: o ritmo, o registro ou as notas. É assim que um estilo próprio nasce.</div>
""",
        "passos": ["Toque C – G – Am – F com acordes simples em semínimas.", "Mude só o ritmo: acorde no 1 e no “e” do 2.",
                   "Mude a textura: arpeje cada acorde (1-5-8-10).", "Use inversões para a nota mais aguda descer suavemente.",
                   "Crie a sua versão juntando duas ideias e grave."],
        "exercicios": [("Uma progressão, 5 versões", "C – G – Am – F com 5 ideias diferentes da tabela.", "10 min · 70 BPM"),
                       ("Baixo caminhando", "C – C/B – Am – Am/G – F.", "5 min · 60 BPM"),
                       ("Notas extras", "Troque F por Fmaj7 e G por Gsus4 → G.", "4 min"),
                       ("Copiar e transformar", "Reproduza 4 compassos de uma gravação e mude o ritmo.", "8 min")],
        "erros": [("Encher demais", "Criatividade também é deixar espaço."), ("Mudar tudo ao mesmo tempo", "Mude uma coisa por vez."),
                  ("Fugir do estilo da música", "A ideia precisa combinar com o clima."), ("Não gravar as ideias", "Grave no celular para não esquecer.")],
        "resumo": ["Ritmo, registro, textura, inversões, baixo e notas extras são ferramentas.", "Mude uma coisa por vez.",
                   "Copie, entenda e transforme.", "Grave as ideias que funcionarem."],
    },
    {
        "slug": "improvisacao-e-composicao",
        "titulo": "Improvisação e composição",
        "sub": "Criar melodias na hora e transformá-las em música.",
        "objetivos": ["Improvisar sobre uma progressão simples", "Usar a escala pentatônica", "Criar frases com pergunta e resposta",
                      "Transformar uma ideia em 8 compassos"],
        "p1": """
<h2>Improvisar é conversar</h2>
<p>Improvisar é criar melodias na hora, em cima de uma harmonia. Para começar com segurança, use a <b>escala pentatônica maior</b>: 5 notas da escala maior sem as que costumam “bater” com os acordes. Em Dó: <b>C – D – E – G – A</b>.</p>
""" + figura(teclado({"C0": ("1", "d"), "D0": ("2", "d"), "E0": ("3", "d"), "G0": ("5", "d"), "A0": ("6", "d"), "C1": ("1", "d")}, oitavas=1, ww=40, letras=True),
             "Pentatônica de Dó maior: C D E G A. Sobre C – G – Am – F, quase nada soa errado.") + """
<h2>Pergunta e resposta</h2>
<p>Pense em frases curtas, como numa conversa: uma frase de 2 compassos que “pergunta” (termina numa nota que pede continuação, como Ré ou Sol) e outra que “responde” (termina no Dó). Repetir e variar uma ideia é melhor do que tocar muitas notas.</p>
<div class="call"><b class="t">De improviso a composição</b>Quando uma frase improvisada ficar boa, grave e escreva. Compor é organizar ideias: 4 compassos de verso, 4 de refrão, repetir, variar e criar um final.</div>
""",
        "passos": ["Mão esquerda segura C – G – Am – F (um acorde por compasso).", "Mão direita toca só 3 notas da pentatônica (C, D, E) em ritmo simples.",
                   "Aumente para as 5 notas e crie uma frase de 2 compassos.", "Responda com outra frase que termine no Dó.",
                   "Grave, escolha a melhor frase e repita com variações por 8 compassos."],
        "exercicios": [("Três notas", "Improvise só com C, D e E sobre a progressão.", "4 min · 70 BPM"),
                       ("Pentatônica completa", "C D E G A, frases curtas com pausas.", "6 min · 70 BPM"),
                       ("Pergunta e resposta", "4 pares de frases, termine sempre no Dó.", "5 min"),
                       ("8 compassos", "Escreva uma melodia de 8 compassos e dê um nome.", "10 min")],
        "erros": [("Tocar notas sem parar", "Use pausas: elas dão sentido às frases."), ("Medo de errar", "Na pentatônica, qualquer nota funciona; erre e siga."),
                  ("Ideias sem repetição", "Repita a frase e varie um detalhe."), ("Esquecer a ideia boa", "Grave tudo.")],
        "resumo": ["Improvisar = criar melodia sobre uma harmonia.", "Pentatônica maior de C: C D E G A.",
                   "Frases curtas, com pergunta e resposta.", "Compor é gravar, escolher e organizar as ideias."],
    },
    {
        "slug": "todas-as-escalas",
        "titulo": "Domínio de todas as escalas",
        "sub": "As 12 escalas maiores e o ciclo de quintas para organizar o estudo.",
        "objetivos": ["Conhecer as 12 escalas maiores", "Entender o ciclo de quintas", "Saber quantos acidentes tem cada tom",
                      "Criar uma rotina para dominar todas"],
        "p1": """
<h2>12 tons, uma regra</h2>
<p>Todas as escalas maiores seguem T T ST T T T ST. O que muda é a quantidade de sustenidos ou bemóis. O <b>ciclo de quintas</b> organiza os tons: subindo de quinta em quinta, cada tom ganha um sustenido; descendo, cada tom ganha um bemol.</p>
""" + tabela(["Tom", "Acidentes", "Notas da escala"],
             [["C", "nenhum", "C D E F G A B"], ["G", "1♯ (F♯)", "G A B C D E F♯"], ["D", "2♯", "D E F♯ G A B C♯"],
              ["A", "3♯", "A B C♯ D E F♯ G♯"], ["E", "4♯", "E F♯ G♯ A B C♯ D♯"], ["B", "5♯", "B C♯ D♯ E F♯ G♯ A♯"],
              ["F♯ / G♭", "6♯ / 6♭", "F♯ G♯ A♯ B C♯ D♯ E♯"], ["F", "1♭ (B♭)", "F G A B♭ C D E"], ["B♭", "2♭", "B♭ C D E♭ F G A"],
              ["E♭", "3♭", "E♭ F G A♭ B♭ C D"], ["A♭", "4♭", "A♭ B♭ C D♭ E♭ F G"], ["D♭", "5♭", "D♭ E♭ F G♭ A♭ B♭ C"]]) + """
<div class="call"><b class="t">Ordem dos acidentes</b>Sustenidos entram sempre nesta ordem: F♯ C♯ G♯ D♯ A♯ E♯. Bemóis, na ordem contrária: B♭ E♭ A♭ D♭ G♭ C♭.</div>
""",
        "passos": ["Toque Dó maior, depois Sol (1♯), Ré (2♯), Lá (3♯)… seguindo o ciclo.", "Antes de cada escala, diga os acidentes em voz alta.",
                   "Toque uma oitava com cada mão, depois duas oitavas com mãos juntas.", "Faça o caminho dos bemóis: F, B♭, E♭, A♭…",
                   "Escolha 3 escalas por dia e passe por todas em uma semana."],
        "exercicios": [("Ciclo dos sustenidos", "C, G, D, A, E, B: uma oitava, mãos separadas.", "8 min · 60 BPM"),
                       ("Ciclo dos bemóis", "F, B♭, E♭, A♭, D♭: uma oitava.", "8 min · 60 BPM"),
                       ("Ditado de acidentes", "Diga quantos acidentes tem um tom sorteado.", "3 min"),
                       ("3 escalas por dia", "Duas oitavas, mãos juntas.", "10 min · 70 BPM")],
        "erros": [("Esquecer um acidente no meio", "Diga os acidentes antes de tocar."), ("Digitação improvisada", "Use sempre a mesma digitação para cada escala."),
                  ("Estudar só os tons fáceis", "O ciclo garante que todos sejam treinados."), ("Velocidade antes da precisão", "Metrônomo lento até ficar limpo.")],
        "resumo": ["Todas as escalas maiores seguem T T ST T T T ST.", "Ciclo de quintas: cada tom ganha um ♯ (ou um ♭).",
                   "Sustenidos: F C G D A E; bemóis: B E A D G C.", "3 escalas por dia cobrem todas em uma semana."],
    },
    {
        "slug": "notas-e-acordes-da-musica",
        "titulo": "Domínio de notas e acordes tocados na música",
        "sub": "Entender o que está acontecendo na harmonia enquanto você toca.",
        "objetivos": ["Identificar a função de cada acorde", "Seguir o baixo e a melodia", "Reconhecer progressões comuns pelo ouvido",
                      "Tocar sabendo para onde a música vai"],
        "p1": """
<h2>Saber o porquê de cada acorde</h2>
<p>Dominar a música é saber não só <b>quais</b> acordes tocar, mas <b>qual papel</b> cada um tem. No campo harmônico, os acordes se agrupam em três funções:</p>
""" + tabela(["Função", "Graus", "Sensação", "Em C"],
             [["Tônica (repouso)", "I, vi, iii", "Casa, chegada", "C, Am, Em"],
              ["Subdominante (afastamento)", "IV, ii", "Saída, movimento", "F, Dm"],
              ["Dominante (tensão)", "V, vii°", "Pede para voltar", "G, G7, B°"]]) + """
<h2>Progressões que se repetem</h2>
<p>Algumas sequências aparecem em milhares de músicas. Reconhecendo-as pelo ouvido, você toca com segurança mesmo sem cifra: <b>I – IV – V – I</b>, <b>I – V – vi – IV</b>, <b>vi – IV – I – V</b> e <b>ii – V – I</b>.</p>
<div class="call"><b class="t">Ouça o baixo</b>A nota mais grave mostra o acorde. Cante a linha do baixo de uma música: se ela vai para o 4º grau, o acorde provavelmente é o IV.</div>
""",
        "passos": ["Escolha uma música e escreva os graus de cada acorde.", "Marque a função: tônica, subdominante ou dominante.",
                   "Toque prestando atenção na tensão do V e no repouso do I.", "Ouça a gravação cantando só o baixo.",
                   "Toque a música sem cifra, guiado pelas funções."],
        "exercicios": [("Funções em C", "Toque C (repouso) → F (saída) → G7 (tensão) → C.", "4 min"),
                       ("Quatro progressões", "Toque as 4 progressões da lista em C e em G.", "8 min · 70 BPM"),
                       ("Análise de cifra", "Escreva graus e funções de uma música.", "6 min"),
                       ("Ouvido", "Ouça 3 músicas e diga qual progressão usam.", "6 min")],
        "erros": [("Tocar sem saber o tom", "Comece sempre descobrindo o tom."), ("Decorar só a sequência de letras", "Pense em graus: funciona em qualquer tom."),
                  ("Ignorar o baixo", "O baixo revela o acorde."), ("Resolver o V em qualquer lugar", "O V costuma ir para o I (ou para o vi).")],
        "resumo": ["Funções: tônica (repouso), subdominante (saída), dominante (tensão).", "Pense em graus, não em letras.",
                   "Progressões comuns: I–IV–V–I, I–V–vi–IV, vi–IV–I–V, ii–V–I.", "O baixo mostra o acorde."],
    },
    {
        "slug": "emprestimo-modal",
        "titulo": "Empréstimo modal",
        "sub": "Pegar acordes “emprestados” do tom menor para dar cor à música.",
        "objetivos": ["Entender o que é empréstimo modal", "Conhecer os empréstimos mais usados em C", "Usar o iv menor e o ♭VII",
                      "Aplicar em progressões reais"],
        "p1": """
<h2>Um acorde de fora que soa bem</h2>
<p><b>Empréstimo modal</b> é usar, numa música em tom maior, um acorde que pertence ao <b>tom menor com a mesma tônica</b>. Em Dó maior, pegamos acordes de Dó menor. O resultado é uma cor diferente, às vezes nostálgica, às vezes grandiosa.</p>
""" + tabela(["Acorde emprestado", "Em C", "Notas", "Efeito"],
             [["iv (quarto grau menor)", "Fm", "F – A♭ – C", "Emoção, saudade (F → Fm → C)"],
              ["♭VII", "B♭", "B♭ – D – F", "Grandioso, muito usado em finais"],
              ["♭VI", "A♭", "A♭ – C – E♭", "Épico, dramático"],
              ["♭III", "E♭", "E♭ – G – B♭", "Surpresa, cor de rock"]]) + figura(
            teclado({"F0": ("1", "d"), "G#0": ("3", "e"), "C1": ("5", "d")}, oitavas=1, ww=40, letras=True), "Fm: a terça Lá desce para Lá♭ (A♭). É o empréstimo mais usado.") + """
<div class="call"><b class="t">Use com intenção</b>O empréstimo chama atenção. Funciona melhor em momentos especiais: o fim do refrão, uma ponte, um final.</div>
""",
        "passos": ["Toque C – F – C e ouça.", "Agora C – F – Fm – C: perceba a mudança de cor no Fm.",
                   "Toque C – B♭ – F – C (♭VII).", "Toque C – A♭ – B♭ – C, um final épico.",
                   "Escolha uma música e teste um empréstimo no fim do refrão."],
        "exercicios": [("IV → iv → I", "C – F – Fm – C.", "4 min · 60 BPM"),
                       ("♭VII", "C – B♭ – F – C.", "4 min · 70 BPM"),
                       ("Final épico", "F – G – A♭ – B♭ – C.", "4 min · 70 BPM"),
                       ("Em outro tom", "Em G: G – C – Cm – G e G – F – C – G.", "5 min")],
        "erros": [("Usar empréstimo em toda música", "Guarde para momentos especiais."), ("Errar a terça do iv", "Fm = F – A♭ – C (Lá bemol)."),
                  ("Esquecer de transpor", "Em G, o iv é Cm e o ♭VII é F."), ("Brigar com a melodia", "Confira se a nota da melodia combina com o acorde.")],
        "resumo": ["Empréstimo modal = usar acordes do tom menor paralelo.", "Em C: Fm (iv), B♭ (♭VII), A♭ (♭VI), E♭ (♭III).",
                   "IV → iv → I é o mais usado.", "Use em momentos especiais."],
    },
    {
        "slug": "acordes-diminutos",
        "titulo": "Domínio de notas diminutas dentro de cada escala",
        "sub": "O acorde diminuto do campo harmônico e o diminuto de passagem.",
        "objetivos": ["Montar o acorde diminuto", "Encontrar o vii° de cada tom", "Usar o diminuto de passagem",
                      "Conhecer o diminuto com sétima"],
        "p1": """
<h2>Terças menores empilhadas</h2>
<p>O acorde <b>diminuto</b> tem terça menor e quinta diminuta: <b>3 + 3 semitons</b>. Em Si: B – D – F. Ele soa tenso e instável, como se pedisse para ir a outro lugar. No campo harmônico maior, o diminuto é o <b>7º grau (vii°)</b>.</p>
""" + tabela(["Tom", "vii°", "Notas", "Resolve em"],
             [["C", "B°", "B – D – F", "C"], ["G", "F♯°", "F♯ – A – C", "G"], ["D", "C♯°", "C♯ – E – G", "D"],
              ["A", "G♯°", "G♯ – B – D", "A"], ["E", "D♯°", "D♯ – F♯ – A", "E"], ["F", "E°", "E – G – B♭", "F"]]) + """
<h2>Diminuto de passagem</h2>
<p>Um uso muito comum é ligar dois acordes que estão a um tom de distância com um diminuto no meio, subindo o baixo meio-tom de cada vez: <b>C – C♯° – Dm</b> ou <b>F – F♯° – C/G</b>. O baixo sobe cromaticamente e a harmonia ganha movimento.</p>
<div class="call"><b class="t">Diminuto com sétima (°7)</b>Acrescentando mais uma terça menor, temos 4 notas igualmente espaçadas: C♯°7 = C♯ – E – G – B♭. Só existem 3 desses acordes diferentes; os outros são inversões.</div>
""",
        "passos": ["Monte B°: B, mais 3 semitons (D), mais 3 (F).", "Toque B° → C e ouça a resolução.",
                   "Toque C – C♯° – Dm, com o baixo subindo C – C♯ – D.", "Monte o vii° de G e de D.",
                   "Acrescente a sétima: C♯°7 = C♯ – E – G – B♭."],
        "exercicios": [("vii° → I", "B° → C, F♯° → G, C♯° → D.", "5 min · 60 BPM"),
                       ("Passagem", "C – C♯° – Dm – G.", "5 min · 70 BPM"),
                       ("Passagem 2", "F – F♯° – C/G – G – C.", "5 min · 70 BPM"),
                       ("Três diminutos", "Toque C°7, C♯°7 e D°7 e veja que os outros se repetem.", "4 min")],
        "erros": [("Confundir diminuto com menor", "Menor = 3 + 4; diminuto = 3 + 3."), ("Deixar o diminuto parado", "Ele é passagem: resolva no acorde seguinte."),
                  ("Baixo pulando na passagem", "O baixo sobe meio-tom: C – C♯ – D."), ("Usar em excesso", "Um diminuto bem colocado vale mais do que vários.")],
        "resumo": ["Diminuto = 3 + 3 semitons; soa tenso.", "No campo maior é o vii° (em C: B°).",
                   "Diminuto de passagem liga acordes com o baixo cromático.", "°7 acrescenta mais uma terça menor."],
    },
    {
        "slug": "tirar-musicas-de-ouvido",
        "titulo": "Tirar músicas de ouvido e introduções",
        "sub": "Um método passo a passo para descobrir tom, acordes e a melodia da introdução.",
        "objetivos": ["Descobrir o tom pelo ouvido", "Achar os acordes pelo baixo", "Tirar a melodia da introdução",
                      "Organizar o que foi descoberto"],
        "p1": """
<h2>O método em 4 etapas</h2>
""" + tabela(["Etapa", "Como fazer", "Dica"],
             [["1. Tom", "Ache a nota que soa como “casa”, geralmente a última nota da música", "Cante a nota e procure no teclado"],
              ["2. Baixo", "Cante a nota mais grave de cada trecho e ache no teclado", "O baixo quase sempre é a tônica do acorde"],
              ["3. Acordes", "Teste maior e menor sobre cada nota de baixo", "Use o campo harmônico do tom para limitar as opções"],
              ["4. Introdução", "Tire a melodia nota por nota, em trechos curtos", "Use velocidade 0,75× no player"]]) + """
<h2>O campo harmônico é o seu mapa</h2>
<p>Descoberto o tom, os acordes mais prováveis são os 6 primeiros graus do campo harmônico. Se a nota do baixo é o 6º grau, teste primeiro o acorde menor (vi). Isso diminui muito as tentativas.</p>
<div class="call"><b class="t">Repetição curta</b>Repita 3 a 5 segundos da música várias vezes. Tentar tirar tudo de uma vez cansa o ouvido. Muitos players permitem repetir um trecho e diminuir a velocidade.</div>
""",
        "passos": ["Ouça a música inteira uma vez sem tocar.", "Descubra o tom cantando a nota de repouso.",
                   "Trecho por trecho, ache o baixo e teste o acorde do campo harmônico.", "Escreva a cifra enquanto descobre.",
                   "Tire a introdução em pedaços de 2 compassos, devagar."],
        "exercicios": [("Tom de 3 músicas", "Ache o tom só pelo ouvido.", "6 min"),
                       ("Baixo cantado", "Cante e toque o baixo de um refrão.", "6 min"),
                       ("Acordes do refrão", "Tire e escreva a cifra de um refrão.", "10 min"),
                       ("Introdução", "Tire 4 compassos de uma introdução, na velocidade 0,75×.", "10 min")],
        "erros": [("Tentar tirar a música inteira de uma vez", "Trechos curtos, repetidos."), ("Começar pelos acordes", "Primeiro o tom, depois o baixo."),
                  ("Ignorar o campo harmônico", "Ele mostra os acordes mais prováveis."), ("Não anotar", "Escreva cada descoberta na hora.")],
        "resumo": ["Ordem: tom → baixo → acordes → introdução.", "O campo harmônico limita as opções.",
                   "Trechos curtos e velocidade reduzida ajudam.", "Anote enquanto descobre."],
    },
    {
        "slug": "aumento-de-repertorio",
        "titulo": "Aumento de repertório musical",
        "sub": "Aprender mais músicas de forma organizada e sem esquecer as antigas.",
        "objetivos": ["Organizar o repertório", "Aprender músicas mais rápido", "Revisar sem perder tempo",
                      "Ter músicas prontas para cada ocasião"],
        "p1": """
<h2>Repertório é uma biblioteca</h2>
<p>Ter um repertório grande não é só saber muitas músicas: é conseguir tocá-las quando precisa. Para isso, organize as músicas como numa biblioteca, com as informações que você vai consultar na hora.</p>
""" + tabela(["Campo", "Exemplo", "Para que serve"],
             [["Nome", "Nome da música", "Encontrar rápido"], ["Tom original e tom usado", "G / E", "Adaptar à voz de quem canta"],
              ["BPM", "72", "Começar no andamento certo"], ["Estrutura", "Intro – V – R – V – R – P – R – F", "Não se perder"],
              ["Estado", "Aprendendo / Pronta / Revisar", "Saber o que estudar"], ["Clima", "Lenta, celebração, oração", "Montar listas para cada momento"]]) + """
<h2>O ciclo de estudo</h2>
<p>Divida o tempo de estudo em três partes: <b>aprender</b> uma música nova, <b>polir</b> as que estão quase prontas e <b>revisar</b> as antigas. A revisão pode ser rápida: tocar só a estrutura e as passagens difíceis.</p>
<div class="call"><b class="t">Reaproveite</b>Muitas músicas usam as mesmas progressões. Agrupe as que têm I – V – vi – IV, por exemplo: aprender uma ajuda a aprender as outras.</div>
""",
        "passos": ["Crie uma planilha ou caderno com os campos da tabela.", "Liste as músicas que você já sabe e marque o estado de cada uma.",
                   "Escolha 1 música nova por semana.", "Divida o estudo: 50% nova, 30% polir, 20% revisar.",
                   "A cada mês, monte uma lista de 10 músicas prontas para tocar."],
        "exercicios": [("Ficha das músicas", "Preencha a ficha de 5 músicas.", "10 min"),
                       ("Agrupar progressões", "Separe as músicas por progressão parecida.", "5 min"),
                       ("Revisão relâmpago", "Toque só a estrutura de 3 músicas antigas.", "6 min"),
                       ("Lista do mês", "Monte uma lista de 10 músicas prontas.", "5 min")],
        "erros": [("Aprender muitas ao mesmo tempo", "Uma nova por semana é o suficiente."), ("Nunca revisar", "Reserve parte de cada estudo para as antigas."),
                  ("Não anotar o tom usado", "Anote o tom em que você toca, não só o original."), ("Repertório só de um estilo", "Varie: lentas, moderadas e animadas.")],
        "resumo": ["Organize as músicas em fichas.", "Uma música nova por semana.", "Divida: aprender, polir e revisar.",
                   "Agrupe músicas com progressões parecidas."],
    },
    {
        "slug": "ministracao-com-o-instrumento",
        "titulo": "Ministração com o instrumento",
        "sub": "Usar o teclado para servir ao momento de adoração.",
        "objetivos": ["Entender o papel do teclado na ministração", "Criar fundos para oração e leitura", "Acompanhar momentos espontâneos",
                      "Seguir quem conduz o louvor"],
        "p1": """
<h2>O teclado a serviço do momento</h2>
<p>Na ministração, o objetivo não é aparecer, mas ajudar as pessoas a adorarem. O tecladista tem um papel especial: ele sustenta os momentos entre as músicas, acompanha orações e leituras e cria o ambiente para o que está acontecendo.</p>
""" + tabela(["Momento", "O que tocar", "Timbre sugerido"],
             [["Oração e leitura", "Acordes longos, poucas notas, dinâmica suave", "Pad ou piano suave"],
              ["Transição entre músicas", "Acordes do tom da próxima música", "Pad + piano"],
              ["Momento espontâneo", "Progressão simples e repetida (I – IV ou I – V – vi – IV)", "Piano + pad"],
              ["Clímax", "Mais notas, oitavas, dinâmica forte", "Piano cheio"]]) + """
<h2>Atenção total a quem conduz</h2>
<p>Combine sinais com quem lidera: mão para cima = subir a intensidade, mão para baixo = diminuir, dedo indicando = repetir a parte. Olhe para o líder com frequência e esteja pronto para mudar.</p>
<div class="call"><b class="t">Preparação também é ministração</b>Estudar as músicas, conhecer os tons e ensaiar com a equipe libera você para estar atento ao momento, em vez de preocupado com as notas.</div>
""",
        "passos": ["Escolha o tom da próxima música e toque um pad com a tônica e o V.", "Crie um fundo de 2 minutos com I – IV, bem suave.",
                   "Ensaie com quem conduz os sinais de subir, descer e repetir.", "Pratique transições: termine uma música e ligue com a próxima.",
                   "Grave um momento de oração e ouça se o teclado ajudou ou atrapalhou."],
        "exercicios": [("Fundo de oração", "Pad em C: C – F/C, acordes longos.", "5 min · livre"),
                       ("Transição", "Termine em G e leve para o tom de C pelo G7.", "5 min"),
                       ("Momento espontâneo", "Repita I – V – vi – IV variando a dinâmica.", "6 min · 70 BPM"),
                       ("Sinais", "Ensaie com alguém os 3 sinais combinados.", "5 min")],
        "erros": [("Tocar alto demais na oração", "No fundo, menos notas e volume baixo."), ("Não olhar para quem conduz", "Olhe a cada mudança de parte."),
                  ("Silêncio total nas transições", "Sustente com um pad no tom da próxima música."), ("Improvisar sem preparo", "Ensaie as transições antes.")],
        "resumo": ["O teclado serve ao momento de adoração.", "Oração: pad suave e acordes longos.", "Transições no tom da próxima música.",
                   "Combine sinais e olhe para quem conduz."],
    },
    {
        "slug": "escala-e-campo-na-pratica",
        "titulo": "Diferença entre escala e campo harmônico (na prática)",
        "sub": "Quando pensar em notas da escala e quando pensar em acordes do campo.",
        "objetivos": ["Diferenciar escala e campo harmônico", "Usar a escala para melodias e frases", "Usar o campo para harmonia",
                      "Aplicar os dois dentro de uma música"],
        "p1": """
<h2>Notas e acordes da mesma família</h2>
<p>A <b>escala</b> é o conjunto de notas do tom, tocadas uma depois da outra: é a matéria-prima das <b>melodias</b>, frases e improvisos. O <b>campo harmônico</b> são os acordes formados com essas notas: é a matéria-prima da <b>harmonia</b>.</p>
""" + tabela(["", "Escala", "Campo harmônico"],
             [["O que é", "7 notas do tom", "7 acordes formados com essas notas"],
              ["Em C", "C D E F G A B", "C Dm Em F G Am B°"],
              ["Usa para", "Melodia, frases, introduções, solos", "Acompanhamento, progressões"],
              ["Mão", "Normalmente a direita", "As duas (acorde + baixo)"]]) + """
<h2>Na prática, dentro da música</h2>
<p>Na introdução, use a escala para criar uma frase. No verso, use o campo para acompanhar. Num momento instrumental, faça os dois: mão esquerda com os acordes do campo e mão direita com uma melodia da escala, escolhendo notas do acorde nos tempos fortes.</p>
<div class="call"><b class="t">Notas do acorde nos tempos fortes</b>Ao criar melodias, coloque as notas do acorde (tônica, terça ou quinta) nos tempos 1 e 3. Entre elas, use as outras notas da escala como passagem.</div>
""",
        "passos": ["Toque a escala de C devagar.", "Toque o campo harmônico de C.", "Mão esquerda: C – Am – F – G. Mão direita: notas da escala.",
                   "Nos tempos 1 e 3, escolha uma nota do acorde; entre eles, notas de passagem.", "Crie uma introdução de 4 compassos para uma música do repertório."],
        "exercicios": [("Escala x campo", "Toque a escala e o campo de G, alternando.", "4 min"),
                       ("Melodia sobre acordes", "Notas do acorde nos tempos fortes.", "6 min · 60 BPM"),
                       ("Introdução", "Crie uma intro de 4 compassos com a escala.", "8 min"),
                       ("Música completa", "Intro com escala, verso com campo.", "8 min")],
        "erros": [("Achar que escala e campo são a mesma coisa", "Escala = notas; campo = acordes."), ("Melodia que briga com o acorde", "Notas do acorde nos tempos fortes."),
                  ("Usar notas fora do tom", "Fique na escala do tom (salvo efeitos intencionais)."), ("Esquecer a mão esquerda", "Ela segura a harmonia do campo.")],
        "resumo": ["Escala = notas do tom (melodia).", "Campo harmônico = acordes do tom (harmonia).",
                   "Melodia: notas do acorde nos tempos fortes.", "Use os dois juntos dentro da música."],
    },
    {
        "slug": "precisao-ritmica",
        "titulo": "Precisão rítmica",
        "sub": "Tocar exatamente no tempo, com subdivisão e groove.",
        "objetivos": ["Entender subdivisão", "Tocar colcheias e semicolcheias regulares", "Encaixar com a bateria",
                      "Avaliar a precisão gravando"],
        "p1": """
<h2>O tempo dentro do tempo</h2>
<p>Precisão rítmica é colocar cada nota exatamente onde ela deve estar. O segredo é sentir as <b>subdivisões</b>: entre um clique e outro existem colcheias (“1 e”) e semicolcheias (“1 e e e”). Quem sente a subdivisão não corre nem atrasa.</p>
""" + tabela(["Subdivisão", "Como contar", "Notas por clique"],
             [["Semínima", "1 – 2 – 3 – 4", "1"], ["Colcheia", "1 e 2 e 3 e 4 e", "2"], ["Tercina", "1 – trip – let", "3"],
              ["Semicolcheia", "1 e & a 2 e & a", "4"]]) + """
<h2>Encaixar com a banda</h2>
<p>Na banda, o tempo é coletivo. O bumbo costuma marcar os tempos 1 e 3, e a caixa os tempos 2 e 4. Toque os acordes junto com o bumbo e evite “andar na frente” da bateria.</p>
<div class="call"><b class="t">Teste da gravação</b>Grave-se tocando com o metrônomo e ouça: as notas caem exatamente no clique? Se o clique “some”, você está no tempo. Se você ouve dois sons, há diferença.</div>
""",
        "passos": ["Em 70 BPM, toque acordes em semínimas por 1 minuto.", "Mude para colcheias contando “1 e 2 e”.",
                   "Toque tercinas e depois semicolcheias.", "Alterne a cada compasso: semínimas, colcheias, tercinas, semicolcheias.",
                   "Grave e confira se as notas caem no clique."],
        "exercicios": [("Escada de subdivisões", "1, 2, 3 e 4 notas por clique, um compasso cada.", "5 min · 70 BPM"),
                       ("Clique no 2 e 4", "Metrônomo como caixa da bateria.", "5 min · 70 BPM"),
                       ("Mão esquerda e direita", "Esquerda em semínimas, direita em colcheias.", "5 min · 70 BPM"),
                       ("Gravação", "Grave 1 minuto e avalie.", "5 min")],
        "erros": [("Correr nas semicolcheias", "Conte em voz alta e diminua o BPM."), ("Atrasar depois de pausas", "Conte a pausa com a mesma atenção."),
                  ("Tocar na frente da bateria", "Escute o bumbo e a caixa."), ("Nunca se gravar", "O ouvido engana; a gravação não.")],
        "resumo": ["Precisão vem de sentir a subdivisão.", "Semínima, colcheia, tercina, semicolcheia: 1, 2, 3, 4 por clique.",
                   "Encaixe com o bumbo (1 e 3) e a caixa (2 e 4).", "Grave para conferir."],
    },
    {
        "slug": "tocar-em-grupo",
        "titulo": "Domínio de tocar em grupo",
        "sub": "Ouvir, deixar espaço e se comunicar com a banda.",
        "objetivos": ["Entender o papel do teclado na banda", "Dividir o espaço com outros instrumentos",
                      "Usar o mapa da música no ensaio", "Comunicar-se durante a música"],
        "p1": """
<h2>Na banda, cada um tem o seu espaço</h2>
<p>Tocar em grupo é diferente de tocar sozinho. Se todos tocam tudo, o som embola. O segredo é dividir as <b>regiões</b> e as <b>funções</b>:</p>
""" + tabela(["Instrumento", "Região principal", "O que o teclado faz"],
             [["Baixo", "Graves", "Mão esquerda mais leve ou sem oitavas graves"],
              ["Violão / guitarra base", "Médios", "Acordes em outra região ou com outro ritmo"],
              ["Guitarra solo", "Médio-agudos", "Deixe espaço nas frases dela"],
              ["Voz", "Médios", "No verso, acompanhe com poucas notas"],
              ["Bateria", "Ritmo", "Encaixe os acordes com o bumbo e a caixa"]]) + """
<h2>Ensaio e comunicação</h2>
<p>Antes de tocar, combine o <b>mapa da música</b> (ordem das partes), o tom e o BPM. Durante a música, olhe para quem conduz e use sinais combinados: quantas vezes repetir o refrão, quando ir para a ponte, quando terminar.</p>
<div class="call"><b class="t">Ouça mais do que toca</b>Se você não está ouvindo o baixo e a voz, provavelmente está alto demais. Ajuste o volume pelo retorno (monitor), não pela força do toque.</div>
""",
        "passos": ["No ensaio, confira tom, BPM e mapa da música com a banda.", "Combine quem toca em cada região (graves, médios, agudos).",
                   "Toque o verso com poucas notas, deixando espaço para a voz.", "Combine os sinais de repetir, ponte e final.",
                   "Grave o ensaio e ouça se o teclado está equilibrado."],
        "exercicios": [("Mapa da música", "Escreva e compartilhe o mapa de 3 músicas.", "8 min"),
                       ("Mão esquerda leve", "Toque com baixista sem oitavas graves.", "5 min"),
                       ("Espaço para o solo", "Segure um pad enquanto a guitarra faz a frase.", "5 min"),
                       ("Sinais", "Ensaie os sinais com a banda.", "5 min")],
        "erros": [("Tocar na mesma região do violão", "Mude a região ou o ritmo."), ("Mão esquerda brigando com o baixo", "Deixe os graves para o baixo."),
                  ("Não olhar para quem conduz", "Olhe a cada fim de parte."), ("Aumentar o volume para se ouvir", "Ajuste o retorno, não a força.")],
        "resumo": ["Cada instrumento tem sua região.", "Teclado: deixe graves para o baixo e espaço para a voz.",
                   "Combine tom, BPM, mapa e sinais.", "Ouça mais do que toca."],
    },
]
