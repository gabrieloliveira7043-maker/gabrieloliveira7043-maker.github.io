"""Conteúdo do material didático do módulo Teclado 1 (um tópico por PDF)."""
from gerar import teclado, figura

MODULO = "Teclado 1"
PASTA = "teclado-1"

LEG_MAOS = '<i style="background:#E7A64A"></i>Mão esquerda <i style="background:#99AB59"></i>Mão direita · os números são os dedos'


def linha_tempo(compassos, acordes, pedal=False, w=640):
    """Compassos em 4/4 com o acorde de cada compasso; se pedal=True desenha a linha do pedal (sobe e desce na troca)."""
    cw = w / compassos
    h = 150 if pedal else 96
    s = [f'<svg viewBox="0 0 {w} {h}" width="100%" style="max-width:{w}px" xmlns="http://www.w3.org/2000/svg">']
    for c in range(compassos):
        x = c * cw
        s.append(f'<rect x="{x + 2}" y="6" width="{cw - 4}" height="34" rx="8" fill="#ECF1DB" stroke="#99AB59"/>')
        s.append(f'<text x="{x + cw / 2}" y="29" text-anchor="middle" font-size="15" font-weight="800" fill="#1C2410">{acordes[c]}</text>')
        for b in range(4):
            bx = x + cw * (b + 0.5) / 4
            s.append(f'<circle cx="{bx}" cy="62" r="{8 if b == 0 else 5}" fill="{"#4D5C1B" if b == 0 else "#B9C38F"}"/>')
            s.append(f'<text x="{bx}" y="88" text-anchor="middle" font-size="11" font-weight="700" fill="#5A6447">{b + 1}</text>')
    if pedal:
        pts = []
        for c in range(compassos):
            x = c * cw
            pts += [(x + 4, 104), (x + 10, 132), (x + cw - 4, 132)]
        pts.append((w - 2, 104))
        s.append('<polyline points="' + " ".join(f"{a},{b}" for a, b in pts) + '" fill="none" stroke="#E7A64A" stroke-width="4" stroke-linejoin="round"/>')
        s.append('<text x="4" y="148" font-size="10.5" font-weight="700" fill="#8A5A12">pedal: sobe na troca do acorde e desce logo em seguida</text>')
    s.append("</svg>")
    return "".join(s)


TOPICOS = [
    # 1 -------------------------------------------------------------
    {
        "slug": "dedos-1-3-5",
        "titulo": "Uso correto dos dedos 1, 3 e 5 com as duas mãos",
        "sub": "A digitação básica que você vai usar em quase todos os acordes do teclado.",
        "objetivos": ["Saber o número de cada dedo nas duas mãos", "Montar um acorde com os dedos 1, 3 e 5",
                      "Entender por que a mão esquerda “inverte” a ordem", "Tocar acordes sem olhar para a mão o tempo todo"],
        "p1": """
<h2>Os dedos têm números</h2>
<p>No teclado, cada dedo recebe um número, e eles são iguais nas duas mãos: <b>1 = polegar</b>, <b>2 = indicador</b>, <b>3 = médio</b>, <b>4 = anelar</b> e <b>5 = mínimo</b>. Partituras, cifras com digitação e professores usam esses números para dizer qual dedo vai em qual tecla.</p>
<p>Um acorde básico (tríade) tem três notas, sempre pulando uma tecla branca entre elas: <span class="chip">Dó – Mi – Sol</span>. Para alcançar essas três notas com conforto, usamos os dedos <b>1, 3 e 5</b>.</p>
""" + figura(teclado({"C0": ("5", "e"), "E0": ("3", "e"), "G0": ("1", "e"), "C1": ("1", "d"), "E1": ("3", "d"), "G1": ("5", "d")}, letras=True, legenda=LEG_MAOS),
             "Acorde de Dó (C) nas duas mãos. Repare que a mão esquerda começa pelo dedo 5.") + """
<h2>Por que a mão esquerda é “ao contrário”?</h2>
<p>As mãos são espelhadas. Na <b>mão direita</b>, o polegar (1) fica à esquerda, então a nota mais grave do acorde é tocada pelo 1 e a mais aguda pelo 5. Na <b>mão esquerda</b>, o polegar fica à direita: a nota mais grave é tocada pelo <b>5</b> e a mais aguda pelo <b>1</b>.</p>
<div class="call"><b class="t">Regra de ouro</b>Mão direita: 1 – 3 – 5, de baixo para cima. Mão esquerda: 5 – 3 – 1, de baixo para cima. Os dedos 2 e 4 ficam “descansando” no ar, sem encostar nas teclas.</div>
""",
        "passos": ["Apoie a mão direita sobre as teclas com os dedos levemente curvados, como se segurasse uma laranja.",
                   "Coloque o polegar (1) no Dó, o médio (3) no Mi e o mínimo (5) no Sol.",
                   "Toque as três notas juntas, apertando com a ponta dos dedos, e solte devagar.",
                   "Repita com a mão esquerda uma oitava abaixo: 5 no Dó, 3 no Mi e 1 no Sol.",
                   "Agora mova o mesmo formato para Fá (Fá–Lá–Dó) e Sol (Sol–Si–Ré), sem mudar os dedos."],
        "exercicios": [("Acorde de Dó, mão direita", "Toque e solte 8 vezes, contando 1-2-3-4 em cada acorde.", "3 min"),
                       ("Acorde de Dó, mão esquerda", "Mesmo exercício com 5-3-1. Olhe para a mão só no começo.", "3 min"),
                       ("Dó → Fá → Sol → Dó", "Mude de acorde sem trocar a digitação. Uma troca a cada 4 tempos.", "5 min · 60 BPM"),
                       ("Acorde quebrado", "Toque as notas uma de cada vez (1, 3, 5, 3) e repita, nas duas mãos.", "4 min")],
        "erros": [("Usar o dedo 2 ou 4 no lugar do 3", "Deixe 2 e 4 levantados de propósito e repita devagar."),
                  ("Dedo 5 “deitado” ou dobrando para trás", "Toque com a pontinha do dedo e mantenha a mão em concha."),
                  ("Polegar duro e esticado", "Deixe o polegar relaxado, tocando com a lateral da ponta."),
                  ("Mão esquerda usando 1-3-5 de baixo para cima", "Lembre do espelho: na esquerda o grave é sempre o 5.")],
        "resumo": ["Os dedos são numerados de 1 (polegar) a 5 (mínimo) nas duas mãos.",
                   "Tríade = três notas pulando uma tecla branca entre elas.",
                   "Mão direita 1-3-5; mão esquerda 5-3-1, sempre do grave para o agudo.",
                   "Mantenha o mesmo formato de mão para mudar de acorde."],
    },
    # 2 -------------------------------------------------------------
    {
        "slug": "uso-do-pedal",
        "titulo": "Uso do pedal",
        "sub": "Como sustentar o som sem embolar as notas quando o acorde muda.",
        "objetivos": ["Saber para que serve o pedal de sustentação", "Ligar e testar o pedal no teclado",
                      "Fazer a troca de pedal na mudança de acorde", "Evitar o som “embolado”"],
        "p1": """
<h2>O que o pedal faz</h2>
<p>O pedal de sustentação (no piano é o pedal da direita) faz as notas continuarem soando mesmo depois que você tira os dedos das teclas. Ele deixa a música mais cheia e ligada, e dá tempo para a mão mudar de posição sem o som “cortar”.</p>
<p>No teclado, o pedal é um acessório que se liga na entrada <b>SUSTAIN</b> ou <b>PEDAL</b> na parte de trás. Ligue o pedal <b>antes</b> de ligar o teclado: muitos modelos leem a posição do pedal ao ligar, e se ele estiver pisado nessa hora, funciona ao contrário.</p>
""" + figura(linha_tempo(4, ["C", "F", "G", "C"], pedal=True),
             "Troca de pedal: a cada acorde novo, o pé sobe rapidinho e desce de novo logo depois de tocar.") + """
<h2>O segredo: trocar o pedal junto com o acorde</h2>
<p>Se você deixar o pedal pisado o tempo todo, as notas de um acorde se misturam com as do próximo e o som fica embolado. Por isso fazemos a <b>troca de pedal</b>: toque o acorde novo, levante o pé e pise de novo logo em seguida. É como “limpar” o som a cada mudança.</p>
<div class="call warm"><b class="t">Atenção ao pé</b>O calcanhar fica sempre apoiado no chão. Quem se mexe é só a parte da frente do pé, como se você batesse o pé bem de leve.</div>
""",
        "passos": ["Conecte o pedal na entrada SUSTAIN com o teclado desligado e ligue o teclado com o pé fora do pedal.",
                   "Toque um Dó, pise no pedal e tire a mão: o som deve continuar.",
                   "Toque o acorde de Dó e pise no pedal logo depois.",
                   "No tempo 1 do próximo compasso, toque o Fá e, ao mesmo tempo, levante o pé.",
                   "Pise de novo logo em seguida, com o Fá ainda tocando. Repita para Sol e Dó."],
        "exercicios": [("Teste do som", "Toque notas soltas com e sem pedal e perceba a diferença.", "2 min"),
                       ("Troca de pedal em Dó – Fá", "Um acorde a cada 4 tempos, trocando o pedal em cada mudança.", "5 min · 60 BPM"),
                       ("Progressão Dó – Fá – Sol – Dó", "A sequência do diagrama, sem som embolado entre os acordes.", "5 min · 60 BPM"),
                       ("Ouvido atento", "Grave-se no celular e escute: dá para ouvir dois acordes misturados? Corrija o tempo do pé.", "3 min")],
        "erros": [("Som embolado, acordes misturados", "Faça a troca de pedal em toda mudança de acorde."),
                  ("Som corta entre um acorde e outro", "Você levantou o pé antes de tocar o acorde novo. Primeiro toca, depois troca."),
                  ("Pedal funciona ao contrário", "Desligue o teclado, solte o pedal e ligue de novo (ou ajuste a polaridade no menu)."),
                  ("Perna cansada ou calcanhar no ar", "Apoie o calcanhar e use só a ponta do pé.")],
        "resumo": ["O pedal de sustentação mantém o som depois que a mão sai da tecla.",
                   "Ligue o pedal antes de ligar o teclado.",
                   "Troca de pedal: toca o acorde novo, sobe o pé e desce logo em seguida.",
                   "Calcanhar no chão; quem trabalha é a ponta do pé."],
    },
    # 3 -------------------------------------------------------------
    {
        "slug": "funcao-de-cada-mao",
        "titulo": "Função de cada mão",
        "sub": "Mão direita faz o acorde cheio e os dedilhados; mão esquerda faz a base.",
        "objetivos": ["Entender o papel da mão direita e da mão esquerda", "Tocar a base com a fundamental na mão esquerda",
                      "Combinar base e acorde no mesmo tempo", "Começar a separar o que cada mão faz"],
        "p1": """
<h2>Duas mãos, dois trabalhos</h2>
<p>Quando tocamos acompanhando uma música, as mãos dividem a tarefa. A <b>mão direita</b> toca o acorde completo (as três notas) e faz os dedilhados, que dão cor e movimento. A <b>mão esquerda</b> faz a <b>base</b>: toca a nota que dá nome ao acorde, chamada <b>fundamental</b>, na região grave do teclado.</p>
<p>A base da mão esquerda funciona como o “chão” da música: é ela que dá peso e mostra qual acorde está tocando. Uma forma simples e muito usada é tocar a fundamental em <b>oitava</b> (a mesma nota, uma grave e uma mais aguda), com os dedos 5 e 1.</p>
""" + figura(teclado({"C0": ("5", "e"), "C1": ("1", "e"), "C2": ("1", "d"), "E2": ("3", "d"), "G2": ("5", "d")}, oitavas=3, ww=26, letras=True, legenda=LEG_MAOS),
             "Acorde de Dó: mão esquerda em oitava (Dó grave + Dó) e mão direita com a tríade Dó–Mi–Sol.") + """
<h2>Como as mãos conversam</h2>
<p>No começo, as duas mãos tocam <b>juntas no tempo 1</b> de cada compasso. Depois a mão direita passa a repetir o acorde ou a dedilhar nos outros tempos, enquanto a esquerda segura a base.</p>
<div class="call"><b class="t">Dica</b>Se a música ficar pesada, tire notas da mão esquerda, não da direita. A base precisa ser firme, mas simples.</div>
""",
        "passos": ["Encontre o Dó mais grave da região do meio para baixo e coloque o dedo 5 da mão esquerda nele.",
                   "Coloque o dedo 1 da mão esquerda no Dó seguinte (uma oitava acima).",
                   "Monte a tríade de Dó na mão direita (1-3-5) duas oitavas acima.",
                   "Conte 1-2-3-4 e toque as duas mãos juntas no tempo 1, segurando até o 4.",
                   "Depois, mantenha a mão esquerda segurando e repita o acorde da mão direita nos tempos 2, 3 e 4."],
        "exercicios": [("Só a base", "Mão esquerda em oitava: Dó, Fá, Sol, Dó. Um por compasso.", "3 min · 60 BPM"),
                       ("Juntas no tempo 1", "Base + acorde completo no tempo 1, segurando 4 tempos.", "4 min · 60 BPM"),
                       ("Direita em semínimas", "Esquerda segura a base; direita toca o acorde nos 4 tempos.", "5 min · 70 BPM"),
                       ("Dedilhado simples", "Direita toca 1-3-5-3 enquanto a esquerda segura a oitava.", "5 min · 60 BPM")],
        "erros": [("As duas mãos fazendo a mesma coisa", "Pense: esquerda = base, direita = acorde. Separe os papéis."),
                  ("Base embolada, grave demais", "Toque a oitava mais próxima do meio do teclado, sem descer muito."),
                  ("Mão esquerda entrando atrasada", "Toque só o tempo 1 juntas, bem devagar, antes de acelerar."),
                  ("Mão direita forte demais", "Equilibre: o acorde acompanha, não briga com a base.")],
        "resumo": ["Mão direita: acorde cheio e dedilhados.", "Mão esquerda: base com a fundamental, de preferência em oitava (5 e 1).",
                   "Comece com as mãos juntas no tempo 1.", "A base é o chão da música: firme e simples."],
    },
    # 4 -------------------------------------------------------------
    {
        "slug": "teclado-e-piano",
        "titulo": "Diferença entre teclado e piano",
        "sub": "Conhecer o seu instrumento ajuda a estudar melhor e a escolher o som certo.",
        "objetivos": ["Saber o que muda entre teclado, piano digital e piano acústico", "Entender teclas sensitivas e peso",
                      "Conhecer timbres e ritmos do teclado", "Saber o que vale para os dois na técnica"],
        "p1": """
<h2>Parecidos por fora, diferentes por dentro</h2>
<p>O <b>piano acústico</b> produz som com martelos que batem em cordas. O <b>piano digital</b> imita o piano com sons gravados e teclas com peso. O <b>teclado arranjador</b> (o mais comum para começar) é mais leve, tem menos teclas e vem com muitos timbres, ritmos e acompanhamentos automáticos.</p>
<table><tr><th>Característica</th><th>Teclado</th><th>Piano (acústico ou digital)</th></tr>
<tr><td>Número de teclas</td><td>Geralmente 61 (5 oitavas)</td><td>88 (7 oitavas e um pouco)</td></tr>
<tr><td>Toque</td><td>Teclas leves, sensitivas ou não</td><td>Teclas pesadas, que imitam os martelos</td></tr>
<tr><td>Sons</td><td>Centenas de timbres e ritmos</td><td>Foco no som de piano</td></tr>
<tr><td>Pedal</td><td>Acessório ligado na entrada SUSTAIN</td><td>Pedais próprios (o da direita sustenta)</td></tr>
<tr><td>Transporte</td><td>Leve, funciona até com pilhas</td><td>Pesado; o acústico precisa de afinação</td></tr></table>
<div class="call"><b class="t">Tecla sensitiva</b>Se o seu teclado é “sensitivo” (touch response), o volume muda com a força do toque. Deixe essa função <b>ligada</b> para treinar dinâmica, como no piano.</div>
""",
        "passos": ["Conte as teclas do seu teclado e descubra quantas oitavas ele tem (cada oitava tem 12 teclas).",
                   "Procure no painel a função TOUCH ou SENSITIVITY e deixe ligada.",
                   "Escolha o timbre de piano (geralmente o número 001) como som principal de estudo.",
                   "Teste o mesmo acorde bem fraco e bem forte e ouça a diferença.",
                   "Experimente dois outros timbres (órgão e cordas) e perceba como mudam o clima da música."],
        "exercicios": [("Mapa do teclado", "Conte as oitavas e marque os Dós com o dedo, do grave ao agudo.", "2 min"),
                       ("Fraco e forte", "Toque o acorde de Dó 4 vezes fraco e 4 vezes forte.", "3 min"),
                       ("Passeio pelos timbres", "Toque Dó–Fá–Sol–Dó em piano, órgão e cordas.", "5 min"),
                       ("Sem ritmo automático", "Estude sempre primeiro sem acompanhamento automático, só com metrônomo.", "lembrete")],
        "erros": [("Estudar com o toque sensitivo desligado", "Ligue o TOUCH: assim você treina força e delicadeza."),
                  ("Escolher um timbre diferente a cada dia", "Use o piano como base; os outros timbres são para depois."),
                  ("Depender do ritmo automático", "Treine com o metrônomo; o ritmo pronto esconde erros de tempo."),
                  ("Achar que técnica de teclado e piano são diferentes", "Postura, dedos e acordes são os mesmos nos dois.")],
        "resumo": ["Teclado: leve, 61 teclas, muitos sons. Piano: 88 teclas pesadas, foco no som de piano.",
                   "A técnica (postura, dedos, acordes) vale para os dois.",
                   "Deixe a função sensitiva ligada e estude com o timbre de piano.",
                   "Timbres e ritmos automáticos são recursos, não muletas."],
    },
    # 5 -------------------------------------------------------------
    {
        "slug": "percepcao-auditiva",
        "titulo": "Percepção auditiva das notas",
        "sub": "Encontrar as notas no teclado e começar a reconhecê-las pelo ouvido.",
        "objetivos": ["Achar qualquer Dó no teclado", "Saber o nome das 7 notas naturais em português e em cifra",
                      "Diferenciar som grave e agudo", "Cantar e reconhecer notas simples"],
        "p1": """
<h2>As 7 notas e o mapa do teclado</h2>
<p>A música usa 7 notas naturais, que são as teclas brancas: <b>Dó, Ré, Mi, Fá, Sol, Lá, Si</b>. Na cifra, elas viram letras: <span class="chip">C D E F G A B</span>. Depois do Si, tudo se repete, uma oitava acima.</p>
<p>Para se localizar, olhe as teclas pretas: elas vêm em grupos de <b>duas</b> e de <b>três</b>. O <b>Dó</b> é sempre a tecla branca logo à esquerda do grupo de <b>duas pretas</b>. Achou o Dó, achou todas as outras.</p>
""" + figura(teclado({"C0": ("Dó", "n"), "C1": ("Dó", "n")}, solfejo=True),
             "O Dó fica à esquerda do grupo de duas teclas pretas. O Fá fica à esquerda do grupo de três.") + """
<h2>Ouvido: grave e agudo</h2>
<p>Quanto mais para a <b>esquerda</b>, mais <b>grave</b> (grosso) é o som; quanto mais para a <b>direita</b>, mais <b>agudo</b> (fino). Treinar o ouvido é ligar o que você ouve ao lugar no teclado e ao som da sua voz.</p>
<div class="call"><b class="t">Cante junto</b>Toque uma nota e cante “lá” na mesma altura. Se a sua voz e o teclado parecem uma só, você está afinado. Se “batem” ou vibram, ajuste a voz devagar.</div>
""",
        "passos": ["Encontre todos os grupos de duas teclas pretas e toque o Dó à esquerda de cada um.",
                   "Do Dó do meio, suba falando o nome de cada nota: Dó, Ré, Mi, Fá, Sol, Lá, Si, Dó.",
                   "Faça o mesmo dizendo as letras: C, D, E, F, G, A, B, C.",
                   "Toque um Dó e cante a mesma nota. Depois faça com Mi e Sol.",
                   "Peça para alguém tocar uma nota grave ou aguda sem você olhar e diga qual foi."],
        "exercicios": [("Caça aos Dós", "Toque todos os Dós do teclado, do grave ao agudo, sem errar.", "2 min"),
                       ("Escala falada", "Suba e desça Dó a Dó falando os nomes e depois as letras.", "4 min"),
                       ("Cantar a nota", "Toque Dó, Mi e Sol e cante cada uma na mesma altura.", "5 min"),
                       ("Grave ou agudo?", "Com um colega ou app: identifique se a segunda nota é mais grave ou mais aguda.", "4 min")],
        "erros": [("Confundir Dó com Fá", "Dó: grupo de 2 pretas. Fá: grupo de 3 pretas."),
                  ("Decorar só o Dó do meio", "Ache o Dó em todas as regiões do teclado."),
                  ("Cantar sem ouvir a nota primeiro", "Toque, escute 2 segundos, e só então cante."),
                  ("Misturar letra e nome", "Faça uma tabela: C = Dó, D = Ré... e cole no teclado.")],
        "resumo": ["Notas naturais: Dó Ré Mi Fá Sol Lá Si = C D E F G A B.",
                   "Dó = à esquerda das 2 pretas; Fá = à esquerda das 3 pretas.",
                   "Esquerda = grave; direita = agudo.", "Toque, escute e cante para treinar o ouvido."],
    },
    # 6 -------------------------------------------------------------
    {
        "slug": "acorde-maior-e-menor",
        "titulo": "Formação de acorde maior e menor",
        "sub": "Tônica, terça e quinta justa: a receita de qualquer acorde.",
        "objetivos": ["Saber o que é tônica, terça e quinta", "Contar semitons para montar acordes",
                      "Montar qualquer acorde maior e menor", "Ouvir a diferença entre alegre e triste"],
        "p1": """
<h2>A receita: tônica + terça + quinta</h2>
<p>Todo acorde básico (tríade) tem três notas. A <b>tônica</b> (ou fundamental) dá o nome ao acorde. A <b>terça</b> define se ele é maior ou menor. A <b>quinta justa</b> dá estabilidade e é igual nos dois.</p>
<p>Para montar, contamos <b>semitons</b>: um semitom é a distância de uma tecla para a vizinha, contando brancas e pretas.</p>
<table><tr><th>Tipo</th><th>Da tônica até a terça</th><th>Da terça até a quinta</th><th>Som</th></tr>
<tr><td><b>Maior</b></td><td>4 semitons (terça maior)</td><td>3 semitons</td><td>Aberto, alegre</td></tr>
<tr><td><b>Menor</b></td><td>3 semitons (terça menor)</td><td>4 semitons</td><td>Fechado, melancólico</td></tr></table>
<div class="two">""" + figura(teclado({"C0": ("T", "d"), "E0": ("3", "d"), "G0": ("5", "d")}, oitavas=1, ww=34, letras=True), "C (Dó maior): Dó – Mi – Sol") + \
             figura(teclado({"C0": ("T", "d"), "Eb0": ("3", "e"), "G0": ("5", "d")}, oitavas=1, ww=34, letras=True), "Cm (Dó menor): Dó – Mi♭ – Sol") + """</div>
<div class="call"><b class="t">Truque rápido</b>Para transformar qualquer acorde maior em menor, abaixe só a terça um semitom (uma tecla para a esquerda). A tônica e a quinta não mudam.</div>
""",
        "passos": ["Escolha a tônica (por exemplo, Ré) e coloque o dedo 1 da mão direita nela.",
                   "Conte 4 semitons a partir da tônica para achar a terça maior (Ré → Fá♯).",
                   "Conte mais 3 semitons para achar a quinta (Fá♯ → Lá). Acorde de Ré maior: Ré – Fá♯ – Lá.",
                   "Abaixe a terça um semitom (Fá♯ → Fá) para formar Ré menor: Ré – Fá – Lá.",
                   "Toque maior e menor seguidos e ouça a mudança de clima."],
        "exercicios": [("Maior e menor em Dó", "Toque C e depois Cm, 4 vezes cada, ouvindo a diferença.", "3 min"),
                       ("Contando semitons", "Monte D, E e A maiores contando 4 + 3 em voz alta.", "5 min"),
                       ("Vira menor", "Transforme D, E e A em Dm, Em e Am abaixando a terça.", "5 min"),
                       ("Ditado de clima", "Alguém toca um acorde; você diz se é maior (alegre) ou menor (triste).", "4 min")],
        "erros": [("Contar só as teclas brancas", "Semitom conta toda tecla vizinha, branca ou preta."),
                  ("Mudar a quinta junto com a terça", "Na troca maior → menor, só a terça desce."),
                  ("Começar a contar na própria tônica como 1", "A tônica é o ponto zero; conte os passos a partir dela."),
                  ("Decorar sem ouvir", "Toque sempre maior e menor seguidos para fixar o som.")],
        "extra": """<h2>Acordes para consultar</h2><table><tr><th>Maior</th><th>Notas</th><th>Menor</th><th>Notas</th></tr>
<tr><td>C</td><td>Dó – Mi – Sol</td><td>Cm</td><td>Dó – Mi♭ – Sol</td></tr>
<tr><td>D</td><td>Ré – Fá♯ – Lá</td><td>Dm</td><td>Ré – Fá – Lá</td></tr>
<tr><td>E</td><td>Mi – Sol♯ – Si</td><td>Em</td><td>Mi – Sol – Si</td></tr>
<tr><td>A</td><td>Lá – Dó♯ – Mi</td><td>Am</td><td>Lá – Dó – Mi</td></tr></table>""",
        "resumo": ["Acorde = tônica + terça + quinta.", "Maior: 4 + 3 semitons. Menor: 3 + 4 semitons.",
                   "A terça decide se é maior ou menor; a quinta justa não muda.",
                   "Maior soa aberto; menor soa mais fechado."],
    },
    # 7 -------------------------------------------------------------
    {
        "slug": "troca-de-notas-no-tempo",
        "titulo": "Troca de notas em determinado período de tempo",
        "sub": "Mudar de acorde na hora certa, sem parar a música.",
        "objetivos": ["Sentir o pulso e contar os tempos do compasso", "Trocar de acorde exatamente no tempo 1",
                      "Preparar a mão antes da troca", "Usar o metrônomo para ganhar segurança"],
        "p1": """
<h2>Pulso, compasso e tempo 1</h2>
<p>Toda música tem um <b>pulso</b>, uma batida constante, como o tique-taque de um relógio. Os pulsos se agrupam em <b>compassos</b>; o mais comum tem 4 tempos (1-2-3-4). O <b>tempo 1</b> é o mais forte, e quase sempre é nele que o acorde muda.</p>
<p>Trocar de acorde “no tempo” significa que o acorde novo soa <b>exatamente</b> no tempo 1, sem atraso e sem pausa. Para isso, a mão precisa começar a se mover <b>antes</b>, no fim do tempo 4.</p>
""" + figura(linha_tempo(4, ["C", "F", "G", "C"]),
             "Cada caixa é um compasso de 4 tempos. O círculo maior marca o tempo 1, onde o acorde muda.") + """
<h2>Antecipe a mão</h2>
<p>Enquanto conta “3”, olhe para onde vai o próximo acorde. No “4”, solte o acorde atual e leve a mão até lá. No “1”, toque. Com a prática, esse movimento fica automático.</p>
<div class="call"><b class="t">Metrônomo é seu amigo</b>Comece em 60 BPM (uma batida por segundo). Só aumente a velocidade quando conseguir 4 compassos seguidos sem atrasar nenhuma troca.</div>
""",
        "passos": ["Ligue o metrônomo em 60 BPM e conte em voz alta: 1-2-3-4.",
                   "Toque Dó no tempo 1 e segure até o 4.",
                   "No tempo 4, já leve a mão para o Fá; toque o Fá no tempo 1 do compasso seguinte.",
                   "Continue: Sol, depois Dó, sempre trocando no tempo 1.",
                   "Quando ficar fácil, troque a cada 2 tempos (no 1 e no 3)."],
        "exercicios": [("Contar e bater palma", "Bata palma no tempo 1 e conte os outros, sem tocar.", "2 min · 60 BPM"),
                       ("Troca a cada 4 tempos", "C – F – G – C, uma troca por compasso.", "5 min · 60 BPM"),
                       ("Troca a cada 2 tempos", "Mesma sequência, trocando no 1 e no 3.", "5 min · 60 BPM"),
                       ("Subindo o tempo", "Repita a troca a cada 4 tempos em 70 e depois em 80 BPM.", "5 min · 70–80 BPM")],
        "erros": [("Parar a música para pensar no próximo acorde", "Olhe o próximo acorde já no tempo 3."),
                  ("Acorde novo entra atrasado", "Solte o acorde atual no 4 e mova a mão antes do 1."),
                  ("Acelerar sem perceber", "Use o metrônomo e grave-se para conferir."),
                  ("Subir a velocidade cedo demais", "Só aumente depois de 4 compassos perfeitos.")],
        "resumo": ["Pulso constante, compassos de 4 tempos, tempo 1 mais forte.",
                   "O acorde muda no tempo 1, sem atraso.", "Prepare a mão no tempo 4.",
                   "Estude com metrônomo a partir de 60 BPM."],
    },
    # 8 -------------------------------------------------------------
    {
        "slug": "postura-e-maos",
        "titulo": "Postura e posicionamento das mãos",
        "sub": "Tocar com conforto hoje evita dor e vícios amanhã.",
        "objetivos": ["Ajustar a altura e a distância do banco", "Sentar com as costas retas e os ombros soltos",
                      "Posicionar a mão em concha", "Perceber e corrigir tensões"],
        "p1": """
<h2>O corpo antes das mãos</h2>
<p>Uma boa postura deixa os braços livres e evita dor nas costas, nos ombros e nos punhos. Antes de tocar a primeira nota, faça um “check-up” rápido do corpo.</p>
<table><tr><th>Parte do corpo</th><th>Como deve ficar</th><th>Teste rápido</th></tr>
<tr><td>Banco</td><td>Na altura em que o antebraço fica paralelo ao chão</td><td>Cotovelo na mesma altura das teclas</td></tr>
<tr><td>Distância</td><td>Sentado na metade da frente do banco</td><td>Braços levemente dobrados, sem esticar</td></tr>
<tr><td>Centro</td><td>Umbigo na direção do Dó central</td><td>As duas mãos alcançam os lados sem girar o tronco</td></tr>
<tr><td>Costas e ombros</td><td>Coluna reta, ombros baixos e soltos</td><td>Respire fundo e solte os ombros</td></tr>
<tr><td>Pés</td><td>Apoiados no chão; o direito perto do pedal</td><td>Dá para levantar sem se apoiar no teclado</td></tr></table>
<h2>Mão em concha</h2>
<p>Imagine que você segura uma laranja: os dedos ficam <b>curvados</b> e tocam com a <b>ponta</b>; o <b>punho</b> fica alinhado com a mão, nem caído nem levantado; o polegar toca com a lateral da ponta.</p>
<div class="call"><b class="t">Sinal de alerta</b>Dor não é normal. Se sentir dor ou formigamento, pare, alongue e confira a postura. Tensão também atrapalha o som.</div>
""",
        "passos": ["Ajuste a altura do banco até o antebraço ficar paralelo ao chão.",
                   "Sente na metade da frente do banco, com o umbigo na direção do Dó central.",
                   "Apoie os pés no chão e deixe as costas retas, sem encostar.",
                   "Deixe os braços caírem ao lado do corpo, respire e só então leve as mãos ao teclado.",
                   "Forme a mão em concha sobre as teclas e toque o Dó com o dedo 3, sentindo a ponta do dedo."],
        "exercicios": [("Check-up de postura", "Passe pelos 5 itens da tabela antes de cada estudo.", "1 min"),
                       ("A laranja", "Segure uma bola ou laranja, observe o formato da mão e repita sem ela no teclado.", "2 min"),
                       ("Espelho", "Toque o acorde de Dó olhando no espelho ou filmando de lado.", "3 min"),
                       ("Soltar os ombros", "A cada 5 minutos de estudo, solte os ombros e confira o punho.", "lembrete")],
        "erros": [("Banco baixo, punho caído", "Suba o banco até o antebraço ficar na linha das teclas."),
                  ("Dedos esticados e retos", "Pense na laranja: dedos curvos, tocando com a ponta."),
                  ("Ombros levantados", "Respire fundo e solte o ar baixando os ombros."),
                  ("Costas curvadas para frente", "Sente mais à frente no banco e endireite a coluna.")],
        "resumo": ["Antebraço paralelo ao chão; sente na metade da frente do banco.",
                   "Umbigo na direção do Dó central; pés no chão.", "Mão em concha, dedos curvos, punho alinhado.",
                   "Dor é sinal para parar e ajustar."],
    },
    # 9 -------------------------------------------------------------
    {
        "slug": "exercicios-de-mobilidade",
        "titulo": "Exercícios de mobilidade",
        "sub": "Aquecer e soltar os dedos para tocar com mais agilidade e independência.",
        "objetivos": ["Aquecer as mãos antes de estudar", "Tocar a posição de cinco dedos",
                      "Ganhar independência entre os dedos", "Treinar com metrônomo de forma segura"],
        "p1": """
<h2>Por que treinar mobilidade</h2>
<p>Cada dedo tem força e agilidade diferentes; o 4 e o 5 costumam ser os mais fracos. Exercícios de mobilidade equilibram os dedos, deixam o toque mais uniforme e preparam as mãos para escalas e dedilhados.</p>
<p>A base é a <b>posição de cinco dedos</b>: cada dedo fica sobre uma tecla vizinha. Em Dó, a mão direita cobre <b>Dó–Ré–Mi–Fá–Sol</b> com os dedos 1 a 5; a esquerda cobre as mesmas notas com os dedos 5 a 1.</p>
""" + figura(teclado({"C0": ("5", "e"), "D0": ("4", "e"), "E0": ("3", "e"), "F0": ("2", "e"), "G0": ("1", "e"),
                     "C1": ("1", "d"), "D1": ("2", "d"), "E1": ("3", "d"), "F1": ("4", "d"), "G1": ("5", "d")}, letras=True, legenda=LEG_MAOS),
             "Posição de cinco dedos em Dó, nas duas mãos.") + """
<h2>Aquecimento de 2 minutos</h2>
<p>Antes do teclado: abra e feche as mãos 10 vezes; gire os punhos devagar para os dois lados; encoste a ponta de cada dedo no polegar, um de cada vez. Movimentos leves, sem forçar.</p>
<div class="call"><b class="t">Devagar e igual</b>O objetivo não é velocidade, é que todas as notas soem com o mesmo volume e a mesma duração.</div>
""",
        "passos": ["Faça o aquecimento sem o teclado.",
                   "Coloque a mão direita na posição de cinco dedos em Dó.",
                   "Toque 1-2-3-4-5-4-3-2-1, uma nota por batida, em 60 BPM.",
                   "Repita com a mão esquerda (5-4-3-2-1-2-3-4-5).",
                   "Junte as duas mãos em movimento contrário: elas se afastam e depois se aproximam."],
        "exercicios": [("Cinco dedos, mão direita", "1-2-3-4-5-4-3-2-1, notas iguais e ligadas.", "3 min · 60 BPM"),
                       ("Cinco dedos, mão esquerda", "5-4-3-2-1-2-3-4-5.", "3 min · 60 BPM"),
                       ("Pares de dedos", "Repita 1-2, 2-3, 3-4, 4-5 quatro vezes cada, nas duas mãos.", "4 min · 60 BPM"),
                       ("Movimento contrário", "Duas mãos juntas, saindo do Dó em direções opostas.", "4 min · 60–80 BPM")],
        "erros": [("Notas com volumes diferentes", "Toque mais devagar e ouça cada nota."),
                  ("Dedo 4 ou 5 levantando outros dedos", "Isso é normal no início; repita os pares 3-4 e 4-5 bem devagar."),
                  ("Punho subindo e descendo", "Mantenha o punho parado; quem se move são os dedos."),
                  ("Forçar até doer", "Pare, solte as mãos e diminua o tempo do exercício.")],
        "resumo": ["Aqueça as mãos antes de estudar.", "Posição de cinco dedos: um dedo por tecla vizinha.",
                   "Toque devagar, com volume igual em todas as notas.", "Aumente o BPM só quando estiver confortável."],
    },
    # 10 ------------------------------------------------------------
    {
        "slug": "letras-dos-acordes-maiores",
        "titulo": "Letra que define cada acorde maior",
        "sub": "Ler cifras: cada letra é um acorde maior.",
        "objetivos": ["Ligar cada letra à sua nota", "Saber que a letra sozinha é um acorde maior",
                      "Montar os 7 acordes maiores naturais", "Ler uma sequência de cifras"],
        "p1": """
<h2>Cifra: o alfabeto da música</h2>
<p>A cifra usa letras para indicar os acordes. Cada letra corresponde a uma nota, começando pelo <b>Lá = A</b>. Quando a letra aparece <b>sozinha</b>, o acorde é <b>maior</b>.</p>
<table><tr><th>Letra</th><th>Nota</th><th>Acorde maior</th><th>Notas do acorde</th></tr>
<tr><td><b>C</b></td><td>Dó</td><td>Dó maior</td><td>Dó – Mi – Sol</td></tr>
<tr><td><b>D</b></td><td>Ré</td><td>Ré maior</td><td>Ré – Fá♯ – Lá</td></tr>
<tr><td><b>E</b></td><td>Mi</td><td>Mi maior</td><td>Mi – Sol♯ – Si</td></tr>
<tr><td><b>F</b></td><td>Fá</td><td>Fá maior</td><td>Fá – Lá – Dó</td></tr>
<tr><td><b>G</b></td><td>Sol</td><td>Sol maior</td><td>Sol – Si – Ré</td></tr>
<tr><td><b>A</b></td><td>Lá</td><td>Lá maior</td><td>Lá – Dó♯ – Mi</td></tr>
<tr><td><b>B</b></td><td>Si</td><td>Si maior</td><td>Si – Ré♯ – Fá♯</td></tr></table>
""" + figura(teclado({}, letras=True), "As letras da cifra no teclado. Depois do B (Si), recomeça no C (Dó).") + """
<div class="call"><b class="t">Para memorizar</b>“A” é a primeira letra do alfabeto e a nota Lá. Conte a partir dela: A Lá, B Si, C Dó, D Ré, E Mi, F Fá, G Sol.</div>
""",
        "passos": ["Cole uma etiqueta com a letra em cada tecla branca de uma oitava (C a B).",
                   "Toque cada nota falando a letra e o nome: “C, Dó”.",
                   "Monte o acorde maior de cada letra com 1-3-5, contando 4 + 3 semitons.",
                   "Leia a sequência C – G – A – F e toque um acorde por compasso.",
                   "Tire as etiquetas e tente de novo, só de memória."],
        "exercicios": [("Letra e nome", "Aponte uma letra aleatória e diga a nota. 20 vezes.", "3 min"),
                       ("Os 7 maiores", "Toque C, D, E, F, G, A, B em sequência.", "5 min · 60 BPM"),
                       ("Sequência C – G – F – C", "Um acorde por compasso, lendo a cifra sem parar.", "4 min · 60 BPM"),
                       ("Ditado de cifras", "Alguém fala uma letra; você toca o acorde maior em até 3 segundos.", "4 min")],
        "erros": [("Achar que A é Dó", "A é Lá. O Dó é o C."), ("Esquecer as teclas pretas em D, E, A e B", "Conte os semitons: 4 + 3."),
                  ("Confundir B com Bb", "B é Si; Bb (Si bemol) é a tecla preta à esquerda do Si."),
                  ("Ler devagar e parar a música", "Leia o próximo acorde enquanto toca o atual.")],
        "resumo": ["A Lá · B Si · C Dó · D Ré · E Mi · F Fá · G Sol.", "Letra sozinha = acorde maior.",
                   "Monte com 1-3-5, contando 4 + 3 semitons.", "Leia a próxima cifra enquanto toca a atual."],
    },
    # 11 ------------------------------------------------------------
    {
        "slug": "letras-dos-acordes-menores",
        "titulo": "Letra que define cada acorde menor",
        "sub": "O “m” minúsculo depois da letra transforma o acorde em menor.",
        "objetivos": ["Reconhecer a cifra de acorde menor", "Montar os 7 acordes menores naturais",
                      "Trocar entre maior e menor da mesma letra", "Tocar uma sequência com maiores e menores"],
        "p1": """
<h2>Letra + m = menor</h2>
<p>Na cifra, o acorde menor é escrito com a letra seguida de um <b>m minúsculo</b>: <span class="chip">Cm</span> é Dó menor, <span class="chip">Am</span> é Lá menor. Atenção: <b>M maiúsculo</b> ou “maj” indicam outra coisa (acordes com sétima maior), que veremos mais adiante.</p>
<table><tr><th>Cifra</th><th>Acorde</th><th>Notas</th><th>Cifra</th><th>Acorde</th><th>Notas</th></tr>
<tr><td><b>Cm</b></td><td>Dó menor</td><td>Dó – Mi♭ – Sol</td><td><b>Gm</b></td><td>Sol menor</td><td>Sol – Si♭ – Ré</td></tr>
<tr><td><b>Dm</b></td><td>Ré menor</td><td>Ré – Fá – Lá</td><td><b>Am</b></td><td>Lá menor</td><td>Lá – Dó – Mi</td></tr>
<tr><td><b>Em</b></td><td>Mi menor</td><td>Mi – Sol – Si</td><td><b>Bm</b></td><td>Si menor</td><td>Si – Ré – Fá♯</td></tr>
<tr><td><b>Fm</b></td><td>Fá menor</td><td>Fá – Lá♭ – Dó</td><td></td><td></td><td></td></tr></table>
<div class="two">""" + figura(teclado({"A0": ("T", "d"), "C1": ("3", "d"), "E1": ("5", "d")}, oitavas=1, ww=30, letras=True), "Am: só teclas brancas") + \
             figura(teclado({"E0": ("T", "d"), "G0": ("3", "d"), "B0": ("5", "d")}, oitavas=1, ww=30, letras=True), "Em: só teclas brancas") + """</div>
<div class="call"><b class="t">Comece pelos fáceis</b>Dm, Em e Am usam só teclas brancas. Aprenda esses três primeiro e depois os que têm tecla preta.</div>
""",
        "passos": ["Leia a cifra: se tiver “m” minúsculo depois da letra, é menor.",
                   "Monte primeiro o acorde maior da letra (4 + 3 semitons).",
                   "Abaixe a terça um semitom: pronto, o acorde é menor (3 + 4).",
                   "Toque Am, Dm e Em, que são só teclas brancas.",
                   "Toque a sequência C – Am – F – G, um acorde por compasso."],
        "exercicios": [("Os três brancos", "Am, Dm e Em, 4 tempos cada.", "4 min · 60 BPM"),
                       ("Maior x menor", "C/Cm, D/Dm, E/Em, G/Gm: alterne e ouça.", "5 min · 60 BPM"),
                       ("Sequência C – Am – F – G", "Uma das sequências mais usadas em músicas.", "5 min · 60–70 BPM"),
                       ("Ditado", "Alguém fala “Fm”, “Bm”, “Gm”: monte em até 5 segundos.", "4 min")],
        "erros": [("Ler Am como Lá maior", "O “m” muda tudo: Am é menor."), ("Abaixar a quinta junto", "Só a terça desce."),
                  ("Confundir m com M ou maj", "m minúsculo = menor; M/maj = sétima maior."),
                  ("Fm e Bm saindo errados", "Conte os semitons: 3 + 4.")],
        "resumo": ["Letra + m minúsculo = acorde menor.", "Menor = terça menor (3) + quinta justa (3 + 4).",
                   "Am, Dm e Em usam só teclas brancas.", "Para virar menor, abaixe só a terça."],
    },
    # 12 ------------------------------------------------------------
    {
        "slug": "melodia-e-harmonia",
        "titulo": "Diferença entre melodia e harmonia",
        "sub": "Melodia é uma nota depois da outra; harmonia são notas ao mesmo tempo.",
        "objetivos": ["Entender melodia e harmonia", "Tocar uma melodia simples com a mão direita",
                      "Acompanhar a melodia com acordes", "Ouvir as duas coisas numa música"],
        "p1": """
<h2>Horizontal e vertical</h2>
<p><b>Melodia</b> é uma sequência de notas tocadas <b>uma depois da outra</b>. É a parte que você canta ou assobia. Pense nela como uma linha <b>horizontal</b>, que anda no tempo.</p>
<p><b>Harmonia</b> é um conjunto de notas tocadas <b>ao mesmo tempo</b>, como os acordes. É uma pilha <b>vertical</b> que dá cor e sustentação para a melodia.</p>
<figure><svg viewBox="0 0 620 150" width="100%" style="max-width:620px" xmlns="http://www.w3.org/2000/svg">
<text x="10" y="18" font-size="12" font-weight="800" fill="#4D5C1B">MELODIA · uma nota por vez</text>
""" + "".join(f'<circle cx="{40 + i * 40}" cy="{128 - y * 16}" r="11" fill="#99AB59"/><text x="{40 + i * 40}" y="{132 - y * 16}" text-anchor="middle" font-size="10" font-weight="800" fill="#1C2410">{n}</text>'
              for i, (n, y) in enumerate([("C", 0), ("C", 0), ("G", 4), ("G", 4), ("A", 5), ("A", 5), ("G", 4)])) + """
<text x="380" y="18" font-size="12" font-weight="800" fill="#8A5A12">HARMONIA · notas juntas</text>
""" + "".join(f'<rect x="{390 + i * 72}" y="{40 + 0}" width="52" height="96" rx="10" fill="#FBF1E2" stroke="#E7A64A"/>' +
              "".join(f'<circle cx="{416 + i * 72}" cy="{122 - k * 30}" r="10" fill="#E7A64A"/><text x="{416 + i * 72}" y="{126 - k * 30}" text-anchor="middle" font-size="10" font-weight="800" fill="#2A1A04">{nn}</text>' for k, nn in enumerate(notas))
              for i, notas in enumerate([("C", "E", "G"), ("F", "A", "C"), ("G", "B", "D")])) + """
</svg><figcaption>À esquerda, a melodia de “Brilha, brilha, estrelinha” andando no tempo. À direita, os acordes C, F e G empilhados.</figcaption></figure>
<div class="call"><b class="t">Na prática</b>Ao tocar uma música, a mão direita pode fazer a melodia e a mão esquerda (ou as duas) a harmonia. A melodia conta a história; a harmonia cria o clima.</div>
""",
        "passos": ["Toque com a mão direita a melodia: C C G G A A G · F F E E D D C (Brilha, brilha, estrelinha).",
                   "Cante junto enquanto toca para ligar a melodia ao ouvido.",
                   "Com a mão esquerda, toque só a fundamental: C sob o primeiro trecho e F, C, G, C sob o segundo.",
                   "Troque a fundamental por acordes completos na mão esquerda (5-3-1).",
                   "Junte: mão direita na melodia, mão esquerda segurando o acorde de cada trecho."],
        "exercicios": [("Só a melodia", "C C G G A A G · F F E E D D C, mão direita, devagar.", "4 min · 60 BPM"),
                       ("Só a harmonia", "Acordes C – C – F – C · F – C – G – C, um a cada 2 tempos.", "4 min · 60 BPM"),
                       ("Juntando", "Melodia na direita + acordes na esquerda.", "6 min · 50–60 BPM"),
                       ("Ouvido de detetive", "Escolha uma música que você gosta e diga: o que é melodia e o que é harmonia?", "3 min")],
        "erros": [("Achar que acorde é melodia", "Se as notas soam juntas, é harmonia."),
                  ("Harmonia mais alta que a melodia", "Toque a mão esquerda mais suave; a melodia precisa aparecer."),
                  ("Mãos perdidas ao juntar", "Treine cada mão separada até ficar automático."),
                  ("Correr na melodia", "Use o metrônomo; cada nota tem seu tempo.")],
        "extra": """<h2>Melodia e acordes de “Brilha, brilha, estrelinha”</h2><table><tr><th>Trecho</th><th>Melodia (mão direita)</th><th>Acordes (mão esquerda)</th></tr>
<tr><td>1</td><td>C C G G A A G</td><td>C · C · F · C</td></tr><tr><td>2</td><td>F F E E D D C</td><td>F · C · G · C</td></tr></table>""",
        "resumo": ["Melodia: notas uma após a outra (horizontal).", "Harmonia: notas ao mesmo tempo (vertical), como os acordes.",
                   "A melodia conta a história; a harmonia cria o clima.", "Treine as mãos separadas antes de juntar."],
    },
]
