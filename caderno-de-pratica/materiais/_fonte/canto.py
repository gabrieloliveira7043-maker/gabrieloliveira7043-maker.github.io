"""Conteúdo do material didático do módulo Canto (um tópico por PDF)."""
from gerar import teclado, figura
from teclado2 import tabela

MODULO = "Canto"
PASTA = "canto"

SAUDE = '<div class="call warm"><b class="t">Cuide da sua voz</b>Dor, rouquidão que dura mais de duas semanas ou perda de voz não são normais. Pare de forçar e procure um otorrinolaringologista ou fonoaudiólogo.</div>'

CINCO_NOTAS = figura(teclado({"C0": ("1", "n"), "D0": ("2", "n"), "E0": ("3", "n"), "F0": ("4", "n"), "G0": ("5", "n")}, oitavas=1, ww=40, letras=True),
                     "Cinco notas (Dó a Sol) para aquecer: suba e desça, depois repita meio-tom acima.")

TOPICOS = [
    {
        "slug": "respiracao-diafragmatica",
        "titulo": "Respiração diafragmática",
        "sub": "Respirar “baixo”, usando o diafragma, é a base de todo o canto.",
        "objetivos": ["Entender o que é o diafragma", "Diferenciar respiração alta e baixa", "Expandir as costelas ao inspirar",
                      "Respirar sem levantar os ombros"],
        "p1": """
<h2>O músculo da respiração</h2>
<p>O <b>diafragma</b> é um músculo em forma de cúpula que fica embaixo dos pulmões. Quando inspiramos, ele desce e abre espaço para o ar entrar. Na respiração diafragmática, sentimos a <b>barriga e as costelas de baixo se expandirem</b> para os lados e para trás, sem que o peito e os ombros subam.</p>
""" + tabela(["", "Respiração alta (evitar)", "Respiração diafragmática (buscar)"],
             [["Onde expande", "Peito e ombros sobem", "Abdômen e costelas flutuantes se abrem"],
              ["Quantidade de ar", "Pouca, curta", "Mais ar, mais controle"],
              ["Tensão", "Pescoço e ombros tensos", "Pescoço livre"],
              ["Resultado no canto", "Frases curtas, voz apertada", "Frases longas, voz estável"]]) + """
<div class="call"><b class="t">Teste rápido</b>Coloque uma mão no peito e outra na barriga. Inspire pelo nariz: a mão da barriga deve se mover mais do que a do peito. Os ombros ficam parados.</div>
""" + SAUDE,
        "passos": ["Deite de barriga para cima com um livro sobre o abdômen.", "Inspire pelo nariz em 4 tempos: o livro sobe, o peito fica quase parado.",
                   "Expire em 4 tempos pela boca: o livro desce.", "Em pé, coloque as mãos nas costelas de baixo e sinta-as abrirem ao inspirar.",
                   "Repita sem levantar os ombros, olhando no espelho."],
        "exercicios": [("Livro na barriga", "Inspira 4, expira 4, deitado.", "3 min"),
                       ("Costelas para os lados", "Em pé, mãos nas costelas, inspira 4, segura 2, expira 6.", "3 min"),
                       ("Espelho", "Inspire olhando os ombros: eles não sobem.", "2 min"),
                       ("Respirar entre frases", "Cante uma frase curta e respire baixo antes da próxima.", "4 min")],
        "erros": [("Ombros subindo", "Olhe no espelho e solte os ombros antes de inspirar."), ("Encher só a barriga para frente", "Sinta também os lados e as costas."),
                  ("Inspirar fazendo barulho", "Inspire com a garganta aberta, como num bocejo leve."), ("Prender a barriga", "O abdômen precisa ficar livre para se mover.")],
        "resumo": ["O diafragma desce na inspiração e abre espaço para o ar.", "Expanda abdômen e costelas, não o peito.",
                   "Ombros e pescoço relaxados.", "Treine deitado e depois em pé."],
    },
    {
        "slug": "apoio-e-controle-do-ar",
        "titulo": "Apoio e controle do ar",
        "sub": "Liberar o ar aos poucos, sem soprar demais nem apertar.",
        "objetivos": ["Entender por que controlar a saída do ar", "Soltar o ar de forma constante", "Aumentar a duração das frases",
                      "Evitar voz soprada e voz apertada"],
        "p1": """
<h2>O ar é o combustível da voz</h2>
<p>A voz é produzida quando o ar passa pelas pregas vocais e as faz vibrar. Se o ar sai de uma vez, a voz fica soprada e as frases acabam cedo. Se o ar é segurado com força, a voz fica apertada. O objetivo é um <b>fluxo constante e controlado</b>.</p>
""" + tabela(["Exercício", "Como fazer", "Meta"],
             [["Sss contínuo", "Solte o ar num “sss” uniforme, sem variar o volume", "20 a 30 segundos"],
              ["Sss com pulsos", "“Ss-ss-ss” curtos, sentindo o abdômen trabalhar", "Abdômen ativo, garganta livre"],
              ["Vela", "Segure uma vela (ou o dedo) na frente da boca e cante sem fazer a chama tremer", "Voz sem sopro"],
              ["Frase longa", "Cante “uuu” numa nota confortável o máximo possível com som estável", "Aumentar a cada semana"]]) + """
<div class="call"><b class="t">Não é segurar o ar</b>Controlar o ar não é travar a garganta. A garganta fica aberta; quem regula a saída do ar é a musculatura do abdômen e das costelas.</div>
""",
        "passos": ["Inspire baixo (respiração diafragmática).", "Solte o ar num “sss” bem uniforme, contando os segundos.",
                   "Mantenha as costelas abertas o máximo possível enquanto solta o ar.", "Troque o “sss” por um “vvv” (com som) e depois por “uuu”.",
                   "Cante uma frase de música usando o mesmo controle."],
        "exercicios": [("Sss contínuo", "Anote quantos segundos consegue sem variar.", "3 min"),
                       ("Pulsos", "Ss-ss-ss em ritmo, sentindo o abdômen.", "2 min"),
                       ("Vvv → uuu", "Mesmo fluxo de ar, agora com som.", "4 min"),
                       ("Frase longa", "Cante uma frase de música inteira sem respirar no meio.", "4 min")],
        "erros": [("Voz soprada", "Menos ar, mais foco no som (exercício da vela)."), ("Garganta apertada", "Boceje levemente antes de cantar para abrir."),
                  ("Costelas fechando logo no início", "Mantenha-as abertas enquanto o ar sai."), ("Usar todo o ar na primeira palavra", "Distribua o ar pela frase inteira.")],
        "resumo": ["Voz = ar passando pelas pregas vocais.", "Fluxo constante: nem sopro, nem aperto.",
                   "Garganta aberta; o controle vem do abdômen e das costelas.", "Meça seu “sss” e acompanhe a evolução."],
    },
    {
        "slug": "nao-usar-voz-de-garganta",
        "titulo": "Não usar voz de garganta",
        "sub": "Tirar o esforço da garganta e levar para o apoio e a ressonância.",
        "objetivos": ["Reconhecer a voz de garganta", "Entender os riscos para a saúde vocal", "Usar o apoio do diafragma",
                      "Sentir as ressonâncias da cabeça e do peito"],
        "p1": """
<h2>Quando a garganta faz todo o trabalho</h2>
<p>A <b>voz de garganta</b> acontece quando o esforço fica concentrado na laringe e na faringe: o pescoço tensiona, as veias aparecem e a voz sai apertada. Ela cansa rápido, causa rouquidão e, com o tempo, pode gerar lesões como nódulos nas pregas vocais.</p>
""" + tabela(["Sinal de voz de garganta", "O que fazer"],
             [["Pescoço tenso, veias saltando", "Solte o pescoço e a mandíbula; diminua o volume"],
              ["Queixo levantando nas notas agudas", "Queixo paralelo ao chão"],
              ["Rouquidão depois de cantar", "Descanso vocal e revisão da técnica"],
              ["Sensação de “raspar”", "Mais apoio do ar, menos força na garganta"]]) + """
<h2>Para onde levar o esforço</h2>
<p>O ar vem do <b>apoio</b> (abdômen e costelas) e o som ganha volume nas <b>ressonâncias</b>: no peito para as notas graves e na “máscara” (região do nariz, bochechas e testa) para as médias e agudas. A garganta fica livre, como no começo de um bocejo.</p>
""" + SAUDE,
        "passos": ["Boceje levemente e sinta a garganta abrir.", "Faça um “mmm” de boca fechada e sinta a vibração nos lábios e no nariz.",
                   "Abra o “mmm” para “miii” mantendo a vibração na frente do rosto.", "Cante uma nota média, coloque a mão no pescoço e confira se está relaxado.",
                   "Cante uma frase da música pensando no som “na frente”, não na garganta."],
        "exercicios": [("Bocejo-suspiro", "Boceje e solte um suspiro do agudo para o grave.", "2 min"),
                       ("Mmm na máscara", "Humming em 5 notas, sentindo a vibração no rosto.", "3 min"),
                       ("Mão no pescoço", "Cante notas médias sem sentir o pescoço endurecer.", "3 min"),
                       ("Frase com volume moderado", "Cante a frase mais aguda da música em volume médio.", "4 min")],
        "erros": [("Gritar para ter volume", "Volume vem do apoio e da ressonância."), ("Queixo para cima no agudo", "Mantenha o queixo nivelado."),
                  ("Ignorar a rouquidão", "Rouquidão é aviso: descanse a voz."), ("Mandíbula travada", "Solte a mandíbula, boca relaxada.")],
        "resumo": ["Voz de garganta: esforço na laringe, pescoço tenso.", "Cansa, causa rouquidão e pode lesionar.",
                   "Ar do apoio, som nas ressonâncias.", "Garganta aberta como num bocejo leve."],
    },
    {
        "slug": "apoio-vocal-suporte",
        "titulo": "Apoio vocal (suporte)",
        "sub": "A musculatura do abdômen e das costelas sustentando o fluxo de ar.",
        "objetivos": ["Entender o que é apoio", "Ativar abdômen e intercostais", "Manter o apoio durante a frase",
                      "Usar o apoio em notas longas e agudas"],
        "p1": """
<h2>O que é apoio</h2>
<p><b>Apoio</b> (ou suporte) é o trabalho da musculatura do <b>abdômen</b> e dos <b>músculos intercostais</b> (entre as costelas) para manter a pressão do ar estável enquanto você canta. É a diferença entre uma nota que balança e uma nota firme.</p>
<p>Pense numa mangueira: se a pressão da água varia, o jato oscila. O apoio mantém a “pressão” do ar constante, e a garganta não precisa compensar.</p>
""" + tabela(["Sensação", "Onde", "Como treinar"],
             [["Firmeza (não rigidez)", "Abdômen, logo abaixo do umbigo", "Tossir de leve e sentir onde o músculo trabalha"],
              ["Costelas abertas", "Laterais e costas", "Manter a expansão enquanto canta"],
              ["Pressão constante", "Toda a região do tronco", "Notas longas sem oscilar"]]) + """
<div class="call"><b class="t">Apoio não é apertar a barriga</b>Contrair tudo com força trava a respiração. O apoio é uma firmeza flexível, como a de quem segura uma caixa leve na frente do corpo.</div>
""",
        "passos": ["Inspire baixo, abrindo costelas e abdômen.", "Comece um “sss” e sinta o abdômen trabalhar para manter o fluxo.",
                   "Troque por um “zzz”, mantendo a mesma firmeza.", "Cante uma nota longa em “ah” com as mãos nas costelas, mantendo-as abertas.",
                   "Cante uma frase aguda pensando no apoio, não na garganta."],
        "exercicios": [("Tossida leve", "Tossa de leve e sinta o músculo do apoio.", "1 min"),
                       ("Sss → zzz", "Mesma pressão do começo ao fim.", "3 min"),
                       ("Nota longa estável", "“Ah” numa nota média por 8 tempos sem oscilar.", "4 min · 60 BPM"),
                       ("Agudo com apoio", "Frase aguda com mais apoio e menos volume.", "4 min")],
        "erros": [("Barriga rígida como pedra", "Firmeza flexível, sem travar."), ("Perder o apoio no fim da frase", "As notas finais precisam de mais apoio, não menos."),
                  ("Compensar com a garganta", "Se a garganta aperta, falta apoio."), ("Ombros subindo", "Ombros baixos, apoio embaixo.")],
        "resumo": ["Apoio = abdômen e intercostais mantendo a pressão do ar.", "Firmeza flexível, sem rigidez.",
                   "Costelas abertas durante a frase.", "Notas agudas e longas pedem mais apoio."],
    },
    {
        "slug": "voz-de-peito",
        "titulo": "Voz de peito",
        "sub": "O registro mais firme e potente, ideal para notas graves e médias.",
        "objetivos": ["Reconhecer a voz de peito", "Sentir a ressonância no peito", "Cantar graves e médios com firmeza",
                      "Saber o limite da voz de peito"],
        "p1": """
<h2>A voz da fala</h2>
<p>A <b>voz de peito</b> (registro de mecanismo 1) é a voz que usamos para falar. As pregas vocais vibram de forma mais grossa e completa, e o som ganha corpo e potência. A vibração é sentida no peito, por isso o nome.</p>
""" + tabela(["Característica", "Voz de peito"],
             [["Região", "Notas graves e médias"], ["Som", "Cheio, firme, potente"], ["Onde vibra", "Peito"],
              ["Usa em", "Versos, partes mais faladas, notas graves com presença"],
              ["Cuidado", "Levar o peito muito para o agudo gera esforço (voz de garganta)"]]) + """
<div class="call"><b class="t">Teste da mão no peito</b>Coloque a mão no peito e fale “ei!” como quem chama alguém. Sinta a vibração. Agora cante essa mesma sensação numa nota média.</div>
""" + SAUDE,
        "passos": ["Fale frases em voz normal, com a mão no peito, sentindo a vibração.", "Cante “ei” numa nota da fala.",
                   "Desça 5 notas cantando “ei”, mantendo o som firme.", "Suba devagar até perceber que fica difícil manter o som cheio.",
                   "Pare antes de forçar: esse é o limite atual da sua voz de peito."],
        "exercicios": [("Fala cantada", "Fale uma frase e depois cante na mesma altura.", "2 min"),
                       ("Ei descendo", "5 notas descendo em “ei”.", "3 min"),
                       ("Graves com presença", "Cante o verso de uma música só em voz de peito.", "4 min"),
                       ("Mapa do limite", "Anote a nota mais aguda confortável em voz de peito.", "2 min")],
        "erros": [("Empurrar o peito para o agudo", "Ao sentir esforço, passe para a voz mista."), ("Grave sem apoio", "Graves também precisam de ar e apoio."),
                  ("Volume exagerado", "Firmeza não é gritar."), ("Pescoço tenso", "Solte o pescoço e a mandíbula.")],
        "resumo": ["Voz de peito = voz da fala; vibra no peito.", "Ideal para graves e médios.", "Som cheio e potente.",
                   "Não leve para o agudo à força."],
    },
    {
        "slug": "voz-de-cabeca",
        "titulo": "Voz de cabeça",
        "sub": "O registro leve, ideal para notas agudas e texturas suaves.",
        "objetivos": ["Reconhecer a voz de cabeça", "Sentir a ressonância na cabeça", "Cantar agudos leves sem esforço",
                      "Diferenciar voz de cabeça e falsete"],
        "p1": """
<h2>Leveza no agudo</h2>
<p>Na <b>voz de cabeça</b>, as pregas vocais vibram de forma mais fina e alongada. O som fica leve e a vibração é sentida na cabeça (testa, nariz, topo da cabeça). É o registro natural para as notas agudas.</p>
""" + tabela(["", "Voz de peito", "Voz de cabeça"],
             [["Região", "Graves e médios", "Agudos"], ["Som", "Cheio, potente", "Leve, brilhante"],
              ["Onde vibra", "Peito", "Cabeça e rosto"], ["Uso", "Versos, presença", "Agudos suaves, texturas delicadas"]]) + """
<div class="call"><b class="t">Cabeça e falsete</b>O falsete é uma voz de cabeça mais soprada e sem corpo. A voz de cabeça bem treinada é leve, mas com som definido. Comece pelo falsete se precisar e vá “fechando” o som aos poucos.</div>
""",
        "passos": ["Imite um “uhuu” de coruja, leve e agudo.", "Faça uma sirene: deslize do grave ao agudo em “uuu”.",
                   "No agudo, sinta a vibração na cabeça.", "Cante 5 notas descendo em “uu”, começando numa nota aguda confortável.",
                   "Deixe o som definido, sem sopro, mantendo a leveza."],
        "exercicios": [("Coruja", "“Uhuu” leve, várias alturas.", "2 min"),
                       ("Sirene", "Grave → agudo → grave em “uuu”, sem quebras bruscas.", "3 min"),
                       ("5 notas descendo", "Em “uu”, começando no agudo.", "4 min"),
                       ("Frase aguda leve", "Cante o trecho mais agudo de uma música em volume baixo.", "4 min")],
        "erros": [("Empurrar volume no agudo", "Agudo leve primeiro; potência vem depois com a voz mista."), ("Som muito soprado", "Feche o som aos poucos com “uu” e “ii”."),
                  ("Levantar o queixo", "Queixo nivelado."), ("Desistir na quebra", "A passagem entre registros se treina com sirenes.")],
        "resumo": ["Voz de cabeça = registro leve dos agudos.", "Vibra na cabeça e no rosto.",
                   "Diferente do falsete, tem som definido.", "Sirenes e “uu” ajudam a encontrá-la."],
    },
    {
        "slug": "voz-mista",
        "titulo": "Voz mista (mix voice)",
        "sub": "Equilibrar peito e cabeça para cantar agudos com potência e sem quebras.",
        "objetivos": ["Entender a voz mista", "Suavizar a passagem entre registros", "Cantar agudos com corpo e sem esforço",
                      "Treinar com exercícios de semioclusão"],
        "p1": """
<h2>O melhor dos dois registros</h2>
<p>A <b>voz mista</b> é a coordenação muscular que equilibra a voz de peito e a voz de cabeça. Com ela, o cantor sobe para o agudo mantendo parte do corpo da voz de peito, sem a “quebra” brusca na passagem e sem gritar.</p>
""" + tabela(["Problema", "Sem voz mista", "Com voz mista"],
             [["Passagem", "A voz “quebra” ou muda de repente", "Transição suave"], ["Agudo", "Grito ou som fraco demais", "Potência com conforto"],
              ["Esforço", "Garganta tensa", "Apoio e ressonância trabalham"]]) + """
<h2>Exercícios de semioclusão</h2>
<p>Exercícios com a boca parcialmente fechada (“lábios vibrando”, “língua vibrando”, cantar num canudo) equilibram a pressão do ar e ajudam as pregas vocais a encontrar a coordenação da voz mista com menos esforço.</p>
<div class="call"><b class="t">Paciência</b>A voz mista leva semanas ou meses para se firmar. Treine pouco e todo dia, sempre sem dor.</div>
""" + SAUDE,
        "passos": ["Faça vibração de lábios (“brrr”) numa sirene do grave ao agudo.", "Repita cantando dentro de um canudo.",
                   "Troque por “nei-nei-nei” em 5 notas subindo, com som um pouco “anasalado”.",
                   "Aos poucos, abra a vogal para “ná” mantendo a sensação.", "Cante a frase mais aguda de uma música com essa coordenação."],
        "exercicios": [("Brrr em sirene", "Lábios vibrando, grave → agudo → grave.", "3 min"),
                       ("Canudo", "Cante uma melodia simples dentro de um canudo.", "3 min"),
                       ("Nei-nei", "5 notas subindo e descendo, meio-tom acima a cada vez.", "5 min"),
                       ("Frase aguda", "Aplique na passagem aguda de uma música.", "4 min")],
        "erros": [("Puxar o peito para o agudo", "Deixe a voz ficar mais leve ao subir."), ("Tudo em falsete", "Use “nei” para dar mais corpo."),
                  ("Treinar até cansar", "Sessões curtas e diárias."), ("Forçar volume", "Volume moderado até a coordenação ficar estável.")],
        "resumo": ["Voz mista equilibra peito e cabeça.", "Passagem suave e agudo sem grito.", "Semioclusão: brrr, canudo, “nei”.",
                   "Treine pouco, todo dia, sem dor."],
    },
    {
        "slug": "aquecimento-vocal",
        "titulo": "Aquecimento vocal",
        "sub": "Uma rotina de 10 minutos antes de cantar.",
        "objetivos": ["Entender por que aquecer", "Seguir uma rotina completa e curta", "Aquecer corpo, respiração e voz",
                      "Desaquecer depois de cantar muito"],
        "p1": """
<h2>A voz também precisa aquecer</h2>
<p>Assim como um atleta, quem canta precisa preparar os músculos. O aquecimento aumenta a circulação, solta tensões, deixa a voz mais flexível e reduz o risco de lesões. Faça sempre antes de ensaios e ministrações.</p>
""" + tabela(["Etapa", "Exercício", "Tempo"],
             [["1. Corpo", "Girar ombros, soltar pescoço, massagear a mandíbula", "2 min"],
              ["2. Respiração", "Inspirar baixo e soltar em “sss”", "2 min"],
              ["3. Semioclusão", "Lábios vibrando (“brrr”) em sirenes", "2 min"],
              ["4. Ressonância", "Humming (“mmm”) em 5 notas", "2 min"],
              ["5. Vogais e extensão", "“Miii-meee-maaa” em 5 notas, subindo meio-tom", "2 min"]]) + CINCO_NOTAS + """
<div class="call"><b class="t">Desaquecimento</b>Depois de cantar muito, faça 2 minutos de humming suave e sirenes descendentes. A voz volta ao estado de repouso.</div>
""",
        "passos": ["Solte o corpo: ombros, pescoço e mandíbula.", "Faça 5 respirações diafragmáticas com “sss”.",
                   "Vibre os lábios em sirenes, do grave ao agudo.", "Faça humming nas 5 notas, subindo meio-tom a cada repetição.",
                   "Cante “miii-meee-maaa” nas 5 notas, sem forçar os extremos."],
        "exercicios": [("Rotina completa", "As 5 etapas da tabela.", "10 min"),
                       ("Brrr com teclado", "Vibração de lábios seguindo as 5 notas do teclado.", "3 min"),
                       ("Humming subindo", "5 notas, meio-tom acima a cada vez.", "3 min"),
                       ("Desaquecimento", "Humming suave e sirenes descendo.", "2 min")],
        "erros": [("Pular o aquecimento", "Mesmo com pouco tempo, faça 3 minutos."), ("Aquecer já no agudo forte", "Comece leve, no médio."),
                  ("Aquecer só a voz", "Corpo e respiração fazem parte."), ("Esquecer de desaquecer", "2 minutos depois de cantar muito.")],
        "resumo": ["Aquecer protege a voz e melhora o som.", "Corpo → respiração → semioclusão → ressonância → vogais.",
                   "Comece leve e no médio.", "Desaqueça depois de cantar muito."],
    },
    {
        "slug": "dinamica-vocal",
        "titulo": "Dinâmica vocal",
        "sub": "Variar a intensidade e a cor da voz para dar vida à música.",
        "objetivos": ["Entender dinâmica na voz", "Cantar suave sem perder o som", "Cantar forte sem gritar",
                      "Planejar a dinâmica de uma música"],
        "p1": """
<h2>A música precisa respirar</h2>
<p>Cantar tudo no mesmo volume deixa a música cansativa. A <b>dinâmica vocal</b> é a variação de intensidade (suave e forte) e de cor (mais aberta, mais escura, mais aérea) ao longo da música, de acordo com o que a letra e o momento pedem.</p>
""" + tabela(["Parte da música", "Dinâmica comum", "Como cantar"],
             [["Verso", "Suave a médio", "Mais próximo da fala, voz de peito leve"],
              ["Pré-refrão", "Crescendo", "Aumentar apoio e intensidade aos poucos"],
              ["Refrão", "Forte", "Voz cheia, com apoio, sem gritar"],
              ["Ponte", "Varia", "Contraste: pode cair ou subir"],
              ["Final", "Suave", "Voltar ao íntimo, encerrando"]]) + """
<div class="call"><b class="t">Suave também precisa de apoio</b>Cantar baixo exige tanto controle quanto cantar forte. Sem apoio, a voz suave fica soprada e desafinada.</div>
""",
        "passos": ["Escolha uma música e escreva a estrutura.", "Marque em cada parte: suave, médio, forte, crescendo.",
                   "Cante o verso em volume baixo, com apoio.", "Cresça no pré-refrão aumentando o apoio, não a garganta.",
                   "Cante a música inteira seguindo o mapa de dinâmica."],
        "exercicios": [("Mesma frase, 3 volumes", "Cante uma frase suave, média e forte.", "3 min"),
                       ("Crescendo numa nota", "“Ah” do suave ao forte em 8 tempos.", "3 min · 60 BPM"),
                       ("Mapa de dinâmica", "Escreva o mapa de uma música.", "5 min"),
                       ("Música com mapa", "Cante seguindo o mapa e grave.", "6 min")],
        "erros": [("Tudo forte", "Guarde a intensidade máxima para o clímax."), ("Suave soprado", "Mantenha o apoio no volume baixo."),
                  ("Forte gritado", "Mais apoio e ressonância, não garganta."), ("Dinâmica que não combina com a letra", "Leia a letra e sinta o que ela pede.")],
        "resumo": ["Dinâmica = variar intensidade e cor da voz.", "Verso suave, refrão forte, final íntimo (em geral).",
                   "Suave e forte precisam de apoio.", "Planeje com um mapa de dinâmica."],
    },
    {
        "slug": "tons-para-sua-voz",
        "titulo": "Procura de tons adequados para a sua voz e timbre",
        "sub": "Descobrir a sua extensão e escolher o tom certo de cada música.",
        "objetivos": ["Descobrir sua extensão confortável", "Conhecer a classificação vocal", "Testar o tom de uma música",
                      "Conversar com o tecladista sobre o tom"],
        "p1": """
<h2>Cada voz tem a sua região</h2>
<p><b>Extensão vocal</b> é o intervalo entre a nota mais grave e a mais aguda que você consegue cantar. Mais importante que ela é a <b>região confortável</b>: as notas que você canta com bom som, sem esforço, por uma música inteira.</p>
""" + tabela(["Classificação", "Voz", "Região aproximada"],
             [["Soprano", "Feminina aguda", "Dó4 a Dó6"], ["Mezzo-soprano", "Feminina média", "Lá3 a Lá5"], ["Contralto", "Feminina grave", "Fá3 a Fá5"],
              ["Tenor", "Masculina aguda", "Dó3 a Dó5"], ["Barítono", "Masculina média", "Lá2 a Lá4"], ["Baixo", "Masculina grave", "Mi2 a Mi4"]]) + """
<p>As regiões são aproximadas e variam de pessoa para pessoa. Dó4 é o Dó central do piano.</p>
<div class="call"><b class="t">Teste do tom</b>Cante a nota mais aguda e a mais grave da música. Se a aguda exige esforço, desça o tom; se a grave some, suba. O tom certo deixa a parte principal da música na sua região confortável.</div>
""",
        "passos": ["Com o teclado, a partir do Dó central, desça nota por nota cantando “ah” até o som perder qualidade.",
                   "Suba até a nota mais aguda confortável (sem esforço).", "Anote a sua região confortável.",
                   "Numa música, encontre a nota mais aguda e a mais grave da melodia.", "Teste a música em 2 ou 3 tons e escolha com o tecladista."],
        "exercicios": [("Mapa da voz", "Anote a nota mais grave e mais aguda confortáveis.", "5 min"),
                       ("Nota mais aguda da música", "Encontre-a no teclado.", "3 min"),
                       ("3 tons", "Cante o refrão em três tons diferentes.", "6 min"),
                       ("Registro de tons", "Anote o tom ideal de cada música do seu repertório.", "5 min")],
        "erros": [("Cantar sempre no tom da gravação", "O tom do artista pode não ser o seu."), ("Escolher pelo verso", "Teste a parte mais aguda (refrão, ponte)."),
                  ("Confundir extensão com conforto", "Use a região confortável."), ("Não anotar", "Guarde o tom de cada música.")],
        "resumo": ["Região confortável importa mais que a extensão máxima.", "Classificação vocal ajuda a entender sua voz.",
                   "Teste a nota mais aguda e a mais grave da música.", "Anote o tom ideal de cada música."],
    },
    {
        "slug": "controle-de-intensidade",
        "titulo": "Controle de intensidade",
        "sub": "Crescendo e decrescendo mantendo o apoio.",
        "objetivos": ["Fazer crescendo controlado", "Fazer decrescendo sem perder a afinação", "Manter o apoio em qualquer volume",
                      "Usar a intensidade de forma expressiva"],
        "p1": """
<h2>Aumentar e diminuir aos poucos</h2>
<p><b>Crescendo</b> é aumentar o volume gradualmente; <b>decrescendo</b> é diminuir gradualmente. Os dois exigem controle do ar: o volume muda, mas a nota, a afinação e a qualidade do som permanecem.</p>
""" + tabela(["Técnica", "O que acontece", "Erro comum"],
             [["Crescendo", "Mais pressão de ar com o apoio, ressonância aberta", "Empurrar com a garganta e desafinar para cima"],
              ["Decrescendo", "Menos ar, mas apoio mantido", "Voz “cair”, desafinar para baixo ou ficar soprada"],
              ["Messa di voce", "Suave → forte → suave numa só nota", "Exercício clássico de controle"]]) + """
<div class="call"><b class="t">O apoio não diminui</b>No decrescendo, o volume baixa, mas o apoio continua ativo. É ele que mantém a nota afinada e o som definido até o fim.</div>
""",
        "passos": ["Escolha uma nota média confortável.", "Cante “ah” suave por 2 tempos, cresça até o forte em 4 tempos.",
                   "Volte ao suave em 4 tempos (decrescendo).", "Confira com o teclado se a afinação se manteve.",
                   "Aplique em uma frase de música que termina em nota longa."],
        "exercicios": [("Messa di voce", "Suave → forte → suave em uma nota.", "4 min · 60 BPM"),
                       ("Crescendo em 5 notas", "Escala de 5 notas crescendo do início ao fim.", "3 min"),
                       ("Decrescendo no fim da frase", "Frases que terminam suaves.", "4 min"),
                       ("Gravação", "Grave e confira afinação nos extremos.", "3 min")],
        "erros": [("Desafinar no forte", "Mais apoio, menos garganta."), ("Voz cair no decrescendo", "Mantenha o apoio até o fim."),
                  ("Mudança brusca", "Distribua a mudança ao longo dos tempos."), ("Som soprado no suave", "Foco no som, menos ar.")],
        "resumo": ["Crescendo e decrescendo são graduais.", "A afinação não muda com o volume.", "O apoio continua ativo no suave.",
                   "Messa di voce é o exercício-base."],
    },
    {
        "slug": "ornamentos",
        "titulo": "Ornamentos: vibrato e melismas",
        "sub": "Enfeitar a melodia com naturalidade e precisão.",
        "objetivos": ["Entender o vibrato natural", "Deixar o vibrato aparecer sem forçar", "Cantar melismas com precisão",
                      "Usar ornamentos com bom gosto"],
        "p1": """
<h2>Vibrato</h2>
<p>O <b>vibrato</b> é uma leve oscilação regular da nota. Quando a voz está livre e bem apoiada, ele aparece de forma <b>espontânea</b> nas notas longas. Vibrato forçado (balançando a mandíbula ou a barriga) soa artificial e cansa.</p>
<h2>Melismas</h2>
<p><b>Melisma</b> é cantar várias notas numa mesma sílaba, como em “a-a-a-amém”. Para soar limpo, cada nota precisa ser clara e afinada. O segredo é treinar devagar, nota por nota, e acelerar aos poucos.</p>
""" + tabela(["Ornamento", "Como treinar", "Cuidado"],
             [["Vibrato", "Notas longas com voz relaxada e apoio; deixe surgir no fim da nota", "Não force com a mandíbula"],
              ["Melisma simples", "3 notas: Sol–Lá–Sol em “a”, devagar", "Cada nota afinada"],
              ["Melisma de 5 notas", "Dó–Ré–Mi–Ré–Dó, aumentando o BPM", "Não embolar"],
              ["Apojatura", "Nota de enfeite antes da nota principal", "Usar pouco"]]) + """
<div class="call"><b class="t">Bom gosto</b>Ornamento é tempero. A melodia precisa continuar reconhecível; use os enfeites em pontos especiais, não em todas as palavras.</div>
""",
        "passos": ["Cante uma nota longa em “ah” com o corpo relaxado.", "No fim da nota, solte a voz e deixe o vibrato surgir sem forçar.",
                   "Com o teclado, toque Sol–Lá–Sol e cante em “a”, bem devagar.", "Aumente para 5 notas e suba o BPM aos poucos.",
                   "Coloque um melisma num ponto de uma música e grave."],
        "exercicios": [("Nota longa relaxada", "8 tempos, deixando o vibrato aparecer.", "3 min · 60 BPM"),
                       ("Melisma de 3 notas", "Sol–Lá–Sol em “a”.", "4 min · 60 BPM"),
                       ("Melisma de 5 notas", "Dó–Ré–Mi–Ré–Dó, subindo o BPM.", "5 min · 60 → 90 BPM"),
                       ("Na música", "Um melisma em um ponto da música.", "4 min")],
        "erros": [("Vibrato forçado", "Relaxe; ele vem com voz livre e apoio."), ("Melisma embolado", "Mais devagar, nota por nota."),
                  ("Ornamento em tudo", "Use em poucos pontos."), ("Desafinar nas notas rápidas", "Treine com o teclado e grave.")],
        "resumo": ["Vibrato natural surge com voz livre e apoio.", "Melisma = várias notas numa sílaba.",
                   "Treine devagar e acelere aos poucos.", "Ornamento é tempero: use com moderação."],
    },
    {
        "slug": "afinacao-e-percepcao",
        "titulo": "Afinação e percepção auditiva",
        "sub": "Ouvir, reconhecer e manter a nota certa.",
        "objetivos": ["Entender o que é cantar afinado", "Reproduzir notas do teclado", "Reconhecer intervalos simples",
                      "Manter a nota com estabilidade"],
        "p1": """
<h2>Afinação começa no ouvido</h2>
<p>Cantar afinado é emitir exatamente a altura da nota pedida. Para isso, o ouvido precisa perceber a nota, a voz precisa reproduzi-la e o apoio precisa sustentá-la. A boa notícia: afinação se treina.</p>
""" + tabela(["Intervalo", "Distância", "Música de referência para lembrar"],
             [["Segunda maior", "2 semitons", "O começo da escala: Dó–Ré"], ["Terça maior", "4 semitons", "Dó–Mi, som alegre"],
              ["Quinta justa", "7 semitons", "Dó–Sol, som aberto e estável"], ["Oitava", "12 semitons", "Mesma nota, mais aguda"]]) + CINCO_NOTAS + """
<div class="call"><b class="t">Ouvir antes de cantar</b>Toque a nota, escute em silêncio por 2 segundos, imagine o som e só então cante. Esse pequeno intervalo melhora muito a afinação.</div>
""",
        "passos": ["Toque Dó no teclado, escute e cante a mesma nota em “lá”.", "Toque Dó–Mi–Sol e cante cada nota.",
                   "Cante as 5 notas subindo e descendo com o teclado, depois sem.", "Toque só a primeira nota e cante uma terça acima; confira no teclado.",
                   "Grave-se cantando uma melodia e compare com a gravação original."],
        "exercicios": [("Eco", "Alguém toca uma nota, você repete.", "4 min"),
                       ("5 notas sem teclado", "Cante e confira a última nota no teclado.", "4 min"),
                       ("Intervalos", "Terças e quintas a partir de notas diferentes.", "4 min"),
                       ("Nota sustentada", "Cante uma nota 8 tempos com o teclado tocando: sem “ondas”.", "3 min")],
        "erros": [("Cantar antes de ouvir", "Escute 2 segundos antes."), ("Desafinar no fim das notas longas", "Mantenha o apoio até o fim."),
                  ("Treinar só com a gravação", "Treine também com notas isoladas no teclado."), ("Desanimar", "Afinação melhora com treino diário.")],
        "resumo": ["Afinação = ouvido + voz + apoio.", "Ouça antes de cantar.", "Intervalos de referência: segunda, terça, quinta, oitava.",
                   "Grave-se e compare."],
    },
    {
        "slug": "psicodinamica-da-voz",
        "titulo": "Psicodinâmica da voz",
        "sub": "Usar o timbre para transmitir emoções de forma intencional.",
        "objetivos": ["Entender a psicodinâmica vocal", "Perceber como o timbre comunica emoção", "Variar a cor da voz conforme a letra",
                      "Cantar com intenção, não só com técnica"],
        "p1": """
<h2>A voz comunica além das palavras</h2>
<p><b>Psicodinâmica vocal</b> é o efeito que as características da voz (timbre, intensidade, velocidade, ar) causam em quem ouve. A mesma frase pode soar íntima, triste, alegre ou firme dependendo de <b>como</b> é cantada.</p>
""" + tabela(["Intenção", "Recursos de voz", "Exemplo de momento"],
             [["Intimidade", "Volume baixo, um pouco de ar, mais perto do microfone", "Verso de oração"],
              ["Alegria", "Voz brilhante, sorriso, articulação leve", "Música de celebração"],
              ["Firmeza / declaração", "Voz cheia de peito, articulação clara", "Refrão de declaração"],
              ["Emoção / clamor", "Crescendo, mais intensidade, notas longas", "Ponte e clímax"]]) + """
<div class="call"><b class="t">Intenção vem da letra</b>Antes de cantar, leia a letra em voz alta como se estivesse falando com alguém. O jeito de falar mostra o jeito de cantar.</div>
""",
        "passos": ["Leia a letra da música em voz alta, como uma conversa.", "Marque em cada parte a intenção: íntimo, alegre, firme, clamor.",
                   "Cante a mesma frase com duas intenções diferentes e compare.", "Escolha os recursos de voz de cada parte (volume, ar, brilho).",
                   "Cante a música inteira com intenção e grave."],
        "exercicios": [("Uma frase, quatro emoções", "Cante a mesma frase de 4 jeitos.", "4 min"),
                       ("Ler a letra", "Leia em voz alta antes de cantar.", "3 min"),
                       ("Sorriso no som", "Cante uma frase sorrindo e outra sem sorrir.", "2 min"),
                       ("Música com intenção", "Cante seguindo as marcações e grave.", "6 min")],
        "erros": [("Cantar no automático", "Pense no que a frase quer dizer."), ("Exagerar a emoção", "Verdade é mais forte que exagero."),
                  ("Sacrificar a técnica", "Emoção com apoio e sem esforço na garganta."), ("Mesma cor a música inteira", "Varie conforme a letra.")],
        "resumo": ["Psicodinâmica = efeito da voz em quem ouve.", "Timbre, volume e ar comunicam emoção.",
                   "A intenção nasce da letra.", "Emoção verdadeira, técnica preservada."],
    },
    {
        "slug": "postura-corporal",
        "titulo": "Postura corporal",
        "sub": "O corpo alinhado deixa a respiração e a laringe livres.",
        "objetivos": ["Alinhar o corpo para cantar", "Relaxar pescoço e ombros", "Manter a laringe livre",
                      "Cantar em pé e sentado com boa postura"],
        "p1": """
<h2>O corpo é o instrumento</h2>
<p>Uma postura alinhada permite que o diafragma se mova livremente, que as costelas se expandam e que a laringe fique solta. Tensões no corpo viram tensões na voz.</p>
""" + tabela(["Parte do corpo", "Como deve ficar"],
             [["Pés", "Afastados na largura dos quadris, peso distribuído"], ["Joelhos", "Destravados, levemente flexionados"],
              ["Coluna", "Alongada, sem curvar nem arquear"], ["Peito", "Aberto, sem estufar"],
              ["Ombros", "Baixos e soltos"], ["Pescoço e cabeça", "Cervical relaxada, queixo paralelo ao chão"],
              ["Mandíbula", "Solta, sem travar"]]) + """
<div class="call"><b class="t">Imagem do fio</b>Imagine um fio puxando o topo da cabeça para cima. A coluna se alonga sem esforço e os ombros caem naturalmente.</div>
""",
        "passos": ["Fique em pé com os pés na largura dos quadris.", "Destrave os joelhos e alongue a coluna (imagem do fio).",
                   "Gire os ombros para trás e solte-os para baixo.", "Mova a cabeça devagar em “sim” e “não” para soltar o pescoço.",
                   "Cante uma frase observando-se no espelho: nada sobe, nada trava."],
        "exercicios": [("Check-up de postura", "Passe pelos itens da tabela antes de cantar.", "1 min"),
                       ("Fio na cabeça", "Cante 5 notas mantendo a coluna alongada.", "3 min"),
                       ("Espelho", "Cante uma música observando ombros e queixo.", "4 min"),
                       ("Sentado", "Cante sentado na beira da cadeira, coluna alongada.", "3 min")],
        "erros": [("Joelhos travados", "Destrave levemente."), ("Queixo para frente ou para cima", "Queixo paralelo ao chão."),
                  ("Peito estufado e rígido", "Peito aberto, mas relaxado."), ("Encostar na cadeira", "Sente na beira, coluna alongada.")],
        "resumo": ["Pés na largura dos quadris, joelhos destravados.", "Coluna alongada, ombros baixos.",
                   "Queixo paralelo ao chão, mandíbula solta.", "Postura livre = voz livre."],
    },
    {
        "slug": "uso-do-microfone",
        "titulo": "Uso do microfone",
        "sub": "Distância, ângulo e efeito de proximidade no estúdio e no palco.",
        "objetivos": ["Segurar o microfone corretamente", "Ajustar a distância conforme o volume", "Entender o efeito de proximidade",
                      "Evitar ruídos e microfonia"],
        "p1": """
<h2>O microfone faz parte da técnica</h2>
<p>O microfone capta e amplifica a voz. Usá-lo bem é parte do canto: a distância e o ângulo mudam o volume, o timbre e a clareza que chegam às pessoas.</p>
""" + tabela(["Situação", "Distância aproximada", "Por quê"],
             [["Voz suave, íntima", "2 a 5 cm", "Capta os detalhes; mais graves"], ["Voz média", "5 a 10 cm", "Som equilibrado"],
              ["Voz forte, agudos potentes", "10 a 20 cm (afaste)", "Evita distorção e excesso de volume"]]) + """
<h2>Efeito de proximidade</h2>
<p>Quanto mais perto do microfone, mais <b>graves</b> ele capta. Use a favor nos momentos íntimos e afaste nos momentos fortes. Aponte o microfone para a boca, de frente, e não cubra a grade (cabeça) do microfone com a mão: isso abafa o som e pode causar microfonia.</p>
<div class="call"><b class="t">Retorno</b>No palco, peça ao técnico um retorno (monitor) em que você ouça a sua voz. Quem não se ouve tende a forçar e desafinar.</div>
""",
        "passos": ["Segure o microfone pelo corpo, longe da grade.", "Aponte para a boca, a uns 5 cm, e cante uma frase média.",
                   "Cante uma frase suave aproximando para 2–3 cm.", "Cante um agudo forte afastando para uns 15 cm.",
                   "Faça a passagem de som com o técnico e ajuste o retorno."],
        "exercicios": [("Três distâncias", "A mesma frase a 3, 8 e 15 cm.", "3 min"),
                       ("Movimento no forte", "Afaste ao crescer, aproxime ao diminuir.", "4 min"),
                       ("Gravação", "Grave-se com o celular como microfone e compare.", "4 min"),
                       ("Passagem de som", "Cante o trecho mais forte e o mais suave para o técnico.", "5 min")],
        "erros": [("Cobrir a grade com a mão", "Segure pelo corpo do microfone."), ("Mesma distância o tempo todo", "Afaste no forte, aproxime no suave."),
                  ("Microfone apontado para o peito", "Aponte para a boca."), ("Forçar por não se ouvir", "Peça ajuste no retorno.")],
        "resumo": ["Segure pelo corpo, aponte para a boca.", "Perto = íntimo e grave; longe = forte sem distorcer.",
                   "Efeito de proximidade realça os graves.", "Ajuste o retorno para não forçar."],
    },
    {
        "slug": "cuidados-com-a-voz",
        "titulo": "Cuidados básicos com a voz",
        "sub": "Hábitos simples que mantêm a voz saudável.",
        "objetivos": ["Conhecer os principais cuidados diários", "Saber o que prejudica a voz", "Descansar a voz após ministrações",
                      "Reconhecer sinais de alerta"],
        "p1": """
<h2>Saúde vocal no dia a dia</h2>
""" + tabela(["Faça", "Evite"],
             [["Beba água ao longo do dia (hidratação começa horas antes)", "Gritar, falar alto em ambientes barulhentos"],
              ["Descanse a voz depois de ministrações e ensaios longos", "Pigarrear com força (beba água ou engula em seco)"],
              ["Durma bem", "Cigarro, álcool em excesso e ambientes com fumaça"],
              ["Aqueça antes e desaqueça depois de cantar", "Alimentos que deixam pigarro antes de cantar (para muitas pessoas: leite e derivados, chocolate)"],
              ["Faça pausas ao falar ou cantar por muito tempo", "Cantar doente ou rouco forçando a voz"]]) + """
<div class="call"><b class="t">Repouso vocal</b>Depois de cantar muito, reduza a fala, evite sussurrar (sussurro também cansa) e faça um desaquecimento leve.</div>
""" + SAUDE,
        "passos": ["Leve uma garrafa de água para ensaios e ministrações.", "Faça o aquecimento de 10 minutos antes de cantar.",
                   "Após ministrar, faça 2 minutos de desaquecimento e fale menos pelo resto do dia.",
                   "Observe quais alimentos deixam você com pigarro e evite-os antes de cantar.", "Anote no caderno sinais de cansaço vocal."],
        "exercicios": [("Diário de hidratação", "Anote quantos copos de água bebeu no dia.", "1 min"),
                       ("Pigarro consciente", "Troque o pigarro por um gole de água.", "lembrete"),
                       ("Desaquecimento", "Humming suave e sirenes descendo após cantar.", "2 min"),
                       ("Diário vocal", "Anote como a voz estava antes e depois de cantar.", "2 min")],
        "erros": [("Beber água só na hora de cantar", "A hidratação começa horas antes."), ("Pigarrear sempre", "Beba água ou engula em seco."),
                  ("Cantar rouco forçando", "Descanse; se persistir, procure um especialista."), ("Sussurrar para “poupar” a voz", "Sussurro também cansa: fale baixo e pouco.")],
        "resumo": ["Hidratação, sono e descanso vocal.", "Evite gritos, pigarro forçado e fumaça.",
                   "Aqueça antes e desaqueça depois.", "Rouquidão persistente: procure um especialista."],
    },
    {
        "slug": "ministracao-e-composicao",
        "titulo": "Ministração e composição",
        "sub": "Unir a técnica vocal ao propósito de levar as pessoas a adorarem.",
        "objetivos": ["Entender o papel de quem ministra", "Equilibrar técnica e expressão", "Conduzir a congregação a cantar junto",
                      "Preparar-se espiritual e tecnicamente"],
        "p1": """
<h2>Cantar não é só técnica</h2>
<p>Na ministração, a técnica vocal está a serviço de algo maior: <b>levar as pessoas a adorarem</b>. Cantar é expressão do Reino de Deus. A técnica bem treinada liberta quem ministra para se concentrar no momento, em vez de se preocupar com a voz.</p>
""" + tabela(["Área", "Na prática"],
             [["Preparação", "Oração, conhecer bem as letras, ensaio com a banda, aquecimento"],
              ["Conduzir", "Cantar de forma que as pessoas consigam acompanhar: tom acessível, melodia clara"],
              ["Comunicar", "Olhar para as pessoas, falar entre as músicas com clareza e brevidade"],
              ["Sensibilidade", "Perceber o momento: repetir um refrão, fazer silêncio, cantar algo espontâneo"],
              ["Equipe", "Combinar sinais com a banda e respeitar quem conduz"]]) + """
<div class="call"><b class="t">Tom para a congregação</b>Para quem ministra, o tom ideal é aquele que a maioria das pessoas consegue cantar. Evite tons muito agudos ou muito graves para a congregação.</div>
""",
        "passos": ["Prepare-se em oração antes do ensaio.", "Estude as letras até cantar sem ler.", "Ensaie com a banda os sinais e as transições.",
                   "Aqueça a voz antes da ministração.", "Durante a ministração, olhe para as pessoas e cante de forma que elas possam acompanhar."],
        "exercicios": [("Letras de memória", "Cante as músicas da lista sem ler.", "10 min"),
                       ("Falar entre músicas", "Treine uma fala curta de transição (até 30 segundos).", "3 min"),
                       ("Tom da congregação", "Teste se a música está confortável para outras pessoas cantarem.", "5 min"),
                       ("Espontâneo", "Cante uma frase espontânea sobre uma progressão simples.", "5 min")],
        "erros": [("Foco só na técnica", "A técnica serve ao momento de adoração."), ("Tom alto demais", "Escolha um tom que a congregação acompanhe."),
                  ("Não saber as letras", "Estude até cantar sem ler."), ("Falar demais entre músicas", "Falas curtas e claras.")],
        "resumo": ["A técnica serve ao propósito de levar à adoração.", "Prepare-se espiritual e tecnicamente.",
                   "Cante de forma que as pessoas acompanhem.", "Sensibilidade e trabalho em equipe."],
    },
    {
        "slug": "como-compor",
        "titulo": "Como compor",
        "sub": "Da inspiração à canção pronta: começo, meio, fim e ponte.",
        "objetivos": ["Buscar a inspiração da canção", "Escrever a letra a partir de uma mensagem", "Criar a melodia e escolher o gênero",
                      "Organizar a estrutura completa"],
        "p1": """
<h2>Comece pelo coração</h2>
<p>Busque primeiro o coração do Senhor. A inspiração pode vir de versos da Bíblia, de algo que Deus falou com você recentemente ou de um momento que você viveu. Escreva tudo, mesmo que pareça simples: a ideia central de uma canção costuma caber numa frase.</p>
""" + tabela(["Etapa", "O que fazer", "Dica"],
             [["1. Mensagem", "Escreva em uma frase o que a canção quer dizer", "Ex.: “Deus é fiel em todo tempo”"],
              ["2. Fontes", "Versos bíblicos e anotações pessoais sobre o tema", "Guarde um caderno só de ideias"],
              ["3. Gênero e clima", "Escolha o estilo e o andamento", "Balada, celebração, oração…"],
              ["4. Melodia", "Cante a frase principal até achar uma melodia", "Grave tudo no celular"],
              ["5. Estrutura", "Organize em verso, refrão, ponte e final", "Refrão = a mensagem principal"]]) + """
<h2>Estrutura da canção</h2>
<p>Toda composição precisa de <b>começo</b> (verso que apresenta o tema), <b>meio</b> (refrão com a mensagem principal), uma <b>ponte</b> (uma parte diferente, que traz um novo ângulo) e um <b>fim</b>. Um caminho comum: Verso 1 – Refrão – Verso 2 – Refrão – Ponte – Refrão – Final.</p>
<div class="call"><b class="t">Simples é forte</b>Melodias fáceis de cantar e letras claras ajudam a congregação a cantar junto. Revise a canção depois de alguns dias, com ouvidos descansados.</div>
""",
        "passos": ["Ore e escreva a mensagem central em uma frase.", "Reúna versos bíblicos e anotações sobre o tema.",
                   "Escolha o gênero e um andamento, e uma progressão simples (ex.: I – V – vi – IV).",
                   "Cante a frase principal sobre a progressão até nascer a melodia do refrão; grave.", "Escreva os versos e a ponte, e organize a estrutura completa."],
        "exercicios": [("Mensagem em uma frase", "Escreva 3 possibilidades e escolha uma.", "5 min"),
                       ("Caderno de ideias", "Anote um verso bíblico e uma frase pessoal por dia.", "3 min"),
                       ("Melodia do refrão", "Cante a mensagem sobre I – V – vi – IV e grave 3 versões.", "10 min"),
                       ("Estrutura completa", "Escreva verso, refrão, ponte e final.", "15 min")],
        "erros": [("Começar pela rima", "Comece pela mensagem; a rima vem depois."), ("Melodia difícil de cantar", "Pense em quem vai cantar junto."),
                  ("Ideias demais numa canção", "Uma mensagem central por canção."), ("Não gravar", "Grave cada ideia na hora.")],
        "resumo": ["Busque primeiro o coração do Senhor: Bíblia e o que Ele falou com você.", "Mensagem central em uma frase.",
                   "Escolha gênero, progressão e melodia; grave tudo.", "Estrutura: começo, meio (refrão), ponte e fim."],
    },
]
