import json

with open("Simulados Aguia/01/TI/conhecimentos_especificos_4.json", "r", encoding="utf-8") as f:
    deck = json.load(f)

cards = [
    {
      "type": "normal",
      "id": "ti_ce4_q134",
      "subject": "Programação - Python Yield",
      "source": "Banca Águia - Q134",
      "timer_override": 180,
      "front": "**Questão 134:**\n\nConsidere o código em Python a seguir.\n\n```python\ndef pares(v):\n    for x in v:\n        if x % 2 == 0:\n            yield x\n\ng = pares([3, 8, 10, 7, 30])\na = sum(g)\nb = sum(g)\nprint(a, b)\n```\n\nApós a execução, é exibido:",
      "stem": [],
      "options": [
        "A) 48 48.",
        "B) 58 58.",
        "C) 48 None.",
        "D) 48 0.",
        "E) 58 0."
      ],
      "answer": 3,
      "back": "Gabarito: D.\n\n!Otávio!\n~Teoria~\n**1) Funções Geradoras (Yield):**\nO `yield` transforma a função num c(Gerador) (Generator). Ele é o pedreiro que entrega um tijolo de cada vez (preguiçoso/lazy) pra não explodir a memória do caminhão de uma vez só com a parede inteira. \n**2) Esgotamento do Gerador:**\nGeradores em Python funcionam como uma fita cassete velha. Quando você dá 'Play' consumindo ele (ex: a função `sum()`), ele vai lendo até chegar no final. Se você pedir para rodar de novo na linha seguinte, ele c(NÃO REBOBINA). A fita já está no fim. Ele devolve o vazio.\n\n~Gabarito~\n**D) 48 0.**\n**> CERTO <**\n\n**Passo 1 — O gerador:** A função `pares` devolve um gerador contendo estritamente apenas os elementos pares sob demanda: 8, 10 e 30.\n**Passo 2 — Primeira soma (`a`):** O comando `sum` consome avidamente o gerador até o talo final: a = 8 + 10 + 30 = c(48).\n**Passo 3 — Segunda soma (`b`):** O gerador já foi completamente esgotado e espremido na linha anterior e não recomeça organicamente; a segunda iteração não produz elemento algum. A soma matemática nua de uma sequência puramente vazia é c(0).\n\n~Gentalha~\n**A) 48 48.**\n**> ERRADO <**\n\nSupõe erroneamente de forma clássica amadora que o gerador recomece a cada uso, imitando uma c(Lista) tradicional armazenada passivamente na RAM. \n\n**C) 48 None.**\n**> ERRADO <**\n\nSupõe ingenuamente que a soma nativa da linguagem sobre uma sequência vazia estouraria erro ou devolveria `None`. A função agregadora nativa `sum([])` sempre devolve zero algébrico íntegro.\n\n**E) 58 0.**\n**> ERRADO <**\n\nDescuido algorítmico matemático: o aluno desatento e eufórico que não leu a barreira do `x % 2 == 0` soma equivocadamente os ímpares também inflando a conta errônea.\n\n!Regra de Bolso!\n~Lógica~\n**1) SE** a variável é um c(Gerador) alimentado por um `yield` e você já engoliu ele num comando (como `list()`, `sum()` ou um laço `for`), **ENTÃO** a segunda tentativa de engolir ele vai retornar c(ZERO ou VAZIO) porque ele já secou para sempre.\n\n!Interpretando a Banca!\n~Gatilho~\nEu sei que parece lógico pensar que uma variável declarada guarda seu valor para ser reusada eternamente, mas a fumaça aqui é ardilosa: a palavra `yield` muda o contrato. Ela não guarda os valores em bloco na RAM, ela guarda apenas a c(Receita de como buscar). Se ela buscou até o final, o cursor estourou."
    },
    {
      "type": "normal",
      "id": "ti_ce4_q135",
      "subject": "Programação - Pandas Transform",
      "source": "Banca Águia - Q135",
      "timer_override": 180,
      "front": "**Questão 135:**\n\nConsidere o código em Python, com a biblioteca pandas, a seguir.\n\n```python\nimport pandas as pd\ndf = pd.DataFrame({\n    \"uf\": [\"SC\", \"SC\", \"PR\", \"SC\", \"PR\"],\n    \"v\": [100, 300, 200, 650, 260]\n})\ndf[\"m\"] = (df.groupby(\"uf\")[\"v\"].transform(\"mean\"))\nr = df[df[\"v\"] > df[\"m\"]]\nprint(len(r), r[\"v\"].sum())\n```\n\nApós a execução, é exibido:",
      "stem": [],
      "options": [
        "A) 2 910.",
        "B) 1 650.",
        "C) 0 0.",
        "D) 3 1210.",
        "E) 5 1510."
      ],
      "answer": 0,
      "back": "Gabarito: A.\n\n!Otávio!\n~Teoria~\n**1) Pandas Transform vs Agg:**\n- **Agg (ou mean direto):** Esmaga o GroupBy. Se você agrupar por Estado (UF), ele pega as 5 linhas, reduz tudo e te devolve uma tabelinha anã de 2 linhas secas brutas (SC e PR) com as médias ao lado.\n- **Transform:** O iterador elegante. Ele agrupa, acha a média, mas ao invés de esmagar o banco e diminuir as linhas, ele volta injetando a média na veia orgânica de cada uma das 5 linhas estendidas preservadas originais na planilha, casando o valor espelhado daquele grupo na exata mesma geometria.\n\n~Gabarito~\n**A) 2 910.**\n**> CERTO <**\n\n**Passo 1 — Médias por grupo (Transform).** \nO transform devolve para cada linha a média esmagada do seu grupo, alinhada cirurgicamente ao índice intocável longo original da placa mãe:\nSC tem (100 + 300 + 650) / 3 = c(350)\nPR tem (200 + 260) / 2 = c(230).\nNa coluna \"m\", as 5 linhas ganham: `[350, 350, 230, 350, 230]`.\n**Passo 2 — Filtro.** \nA equação `df[\"v\"] > df[\"m\"]` fica restrita as linhas com valor blindado acima da média do c(próprio grupo isolado) local. \nPassam no teste: A linha SC de 650 (650 > 350) e a linha PR de 260 (260 > 230).\n**Passo 3 — Saída.** \nSobraram c(2) linhas blindadas. Que somam juntas 650 + 260 = c(910).\n\n~Gentalha~\n**B) 1 650.**\n**> ERRADO <**\n\nCompara equivocadamente cruel com a média global maciça total inteira de 302, ignorando a fatiada orgânica local espremida agrupada por Estado da função mágica operadora frontal de Data Science.\n\n**C) 0 0.**\n**> ERRADO <**\n\nÉ o que ocorreria brutalmente se usasse `mean()` nativo puro bruto enxuto vazio ali no lugar do `transform`, pois a série resultante minguada indexada purista ficaria desalinhada cega em linhas tortas vazias c(NaN) sem preenchimento correto injetado iterativo da máscara preenchida fina contínua de broadcast relacional.\n\n!Regra de Bolso!\n~Lógica~\n**1) SE** precisar achar a média de um grupo mas sem amassar e diminuir o número de linhas da planilha, mantendo a geometria visual imensa inteira, **ENTÃO** você fuzila o comando `.transform()` mágico preservador estrito formal lógico.\n\n!Interpretando a Banca!\n~Gatilho~\nEu sei que parece lógico pensar que GroupBy sempre encolhe a tabela num resumo esmagado, mas a fumaça aqui é ardilosa: a palavra `transform` é a chave mestra que injeta o resumo devolta sem quebrar a espinha dorsal original do tamanho da matriz do Excel analítico."
    },
    {
      "type": "normal",
      "id": "ti_ce4_q136",
      "subject": "Programação - NumPy Cumsum e Argmax",
      "source": "Banca Águia - Q136",
      "timer_override": 180,
      "front": "**Questão 136:**\n\nConsidere o código em Python, com a biblioteca NumPy, a seguir.\n\n```python\nimport numpy as np\na = np.array([4, 5, 0, 13, 3, 5])\nc = np.cumsum(a)\ni = np.argmax(c > 20)\nprint(i, c[i], c[-1])\n```\n\nApós a execução, é exibido:",
      "stem": [],
      "options": [
        "A) 4 25 30.",
        "B) 3 22 30.",
        "C) 3 13 30.",
        "D) 5 30 30.",
        "E) 1 9 30."
      ],
      "answer": 1,
      "back": "Gabarito: B.\n\n!Otávio!\n~Teoria~\n**1) np.cumsum (Soma Acumulada):**\nEle vai rolando uma bola de neve, somando o anterior e criando um novo vetor iterado inchado.\n**2) np.argmax com Booleanos:**\nO `argmax` não devolve o maior valor da lista. Ele devolve o c(Índice) de onde o maior valor da lista mora. Quando injetado em cima de um vetor booleano `[False, False, True]`, como o `True` vale 1 e o `False` vale 0 (na estatística analítica matemática binária de máquina nativa real limpa abstrata do Python), ele pesca o primeiro `True` que trombar pelo caminho limítrofe contínuo.\n\n~Gabarito~\n**B) 3 22 30.**\n**> CERTO <**\n\n**Passo 1 — Soma Acumulada.** \n`c = [4, 9, 9, 22, 25, 30]`.\n**Passo 2 — Primeiro acumulado acima de 20.** \nA comparação c(vetorial orgânica densa de array) `c > 20` gera o vetor booleano binário bruto limítrofe: `[False, False, False, True, True, True]`.\nO comando `np.argmax` pega esse vetor binário esmagado falso local limpo lógico estrito da lista analítica matemática crua exata pura fina relacional cega formal isolada e devolve o índice da primeira ocorrência do maior valor de todos (do primeiro `True` encontrado brutalmente). \nO primeiro `True` habita matematicamente puramente cirurgicamente no índice `i` = c(3) (Lembrete: Python conta o dedo a partir do Zero).\n**Passo 3 — Saída Final de Impressão.** \n`i` = 3\n`c[3]` (O valor na bola de neve contínua) = 22\n`c[-1]` (O último elemento da bola arrastada pesada global unida inteira final) = 30.\n\n~Gentalha~\n**A) 4 25 30.**\n**> ERRADO <**\n\nConta as posições de forma medieval cega purista clássica ignorante desatenta a partir de 1, esquecendo o zero-index originário estrito formal brutal puro lógico limpo abstrato do pilar de C/Python estipulado na raiz unificada do array nativo do banco.\n\n**C) 3 13 30.**\n**> ERRADO <**\n\nExibe o elemento da array limpa nativa seca de origem `a`, e não a estocada acumulada fina atrelada densa amarrada inchada engordada analítica estrita `c` ali exigida.\n\n**D) 5 30 30.**\n**> ERRADO <**\n\nAplica argmax direto cego sem máscara no vetor gordo acumulado, achando de fato estupidamente ingenuamente cruamente o maior valor da base sem checar o gatilho da barreira condicional atrelada booleana restritiva amarrada fina da restrição imposta `c > 20`.\n\n!Regra de Bolso!\n~Lógica~\n**1) SE** você aplica função Numpy de `.argmax()` no meio de comparações booleanas cruas finas estritas reais formais analíticas brutas atreladas amarradas unárias secas (ex: `Vetor > X`), **ENTÃO** você extrai fatal e mecanicamente o c(Índice Posição Zero-based do Primeiro True) avistado pela máquina no horizonte de execução linear contínuo.\n\n!Interpretando a Banca!\n~Gatilho~\nEu sei que parece lógico pensar que argmax é para encontrar picos estatísticos altos (e é o uso primário), mas a fumaça aqui é ardilosa: a ciência de dados forense corrompe e usa o argmax como um `find_first()` para descobrir matematicamente a barreira onde o sonegador passou do limite X pela primeira vez na auditoria temporal."
    },
    {
      "type": "normal",
      "id": "ti_ce4_q137",
      "subject": "Programação - Exceções e Arquivos Python",
      "source": "Banca Águia - Q137",
      "timer_override": 180,
      "front": "**Questão 137:**\n\nAcerca de tratamento de exceções, de arquivos e de dados em Python 3, julgue as afirmativas a seguir em verdadeiras (V) ou falsas (F).",
      "stem": [
        "vf(I. Em um bloco try/except/else, o bloco else é executado quando ocorre uma exceção que os blocos except anteriores não tratam.)",
        "vf(II. Ao sair por causa de uma exceção de um bloco with open(...) as f, o arquivo permanece aberto até ser liberado pelo coletor de lixo, o que exige fechá-lo no except.)",
        "vf(III. Depois de um bloco except ValueError as e, a variável e continua disponível no restante da função, com a última exceção capturada.)",
        "vf(IV. Na leitura de um JSON com json.loads, os números com parte decimal são convertidos no tipo Decimal, o que evita os erros de arredondamento do ponto flutuante.)"
      ],
      "options": [
        "A) F, V, F, F.",
        "B) F, F, F, F.",
        "C) V, V, F, F.",
        "D) F, V, V, F.",
        "E) F, F, F, V."
      ],
      "answer": 1,
      "back": "Gabarito: B.\n\n!Otávio!\n~Teoria~\n**1) Python Try/Except/Else:**\nO bloco `else` só serve para a glória. Ele c(só roda) se nada estourar. Se a try der erro e o except capturar, o else não roda. Se der um erro que ninguém capturou (Crash), o programa morre e o else também afunda sem rodar.\n**2) With Open e Context Managers:**\nO `with` é uma maravilha auto-limpante isolada. Se estourar Kernel Panic e o código crashar com exceção fatal dura lá no meio da leitura do TXT, o `with` c(fecha o arquivo à força cravado) antes de entregar os pontos estritos limítrofes finos limpos da máquina.\n\n~Gabarito~\n**B) F, F, F, F.**\n\n**I. Em um bloco try/except/else, o bloco else é executado quando ocorre uma exceção que os blocos except anteriores não tratam.**\n**> ERRADO <**\n\nO `else` é executado puramente cruamente atreladamente linearmente quando o bloco `try` termina c(sem exceção alguma); a exceção não tratada sobe matando quem chamou brutalmente após engolir a máquina.\n\n**II. Ao sair por causa de uma exceção de um bloco with open(...) as f, o arquivo permanece aberto até ser liberado pelo coletor de lixo, o que exige fechá-lo no except.**\n**> ERRADO <**\n\nO gerenciador de contexto `with` fecha taxativamente categoricamente fatalmente blindadamente o arquivo fisicamente na gaveta ao sair da indentação formal, com ou sem a quebra abrupta mortal orgânica de estourar exceção pesada suja ali na veia.\n\n**III. Depois de um bloco except ValueError as e, a variável e continua disponível no restante da função, com a última exceção capturada.**\n**> ERRADO <**\n\nAo fim do bloco except abstrato duro fechado, o nome ali associado nativo com a diretriz sintática estrita orgânica `as` é c(removido e purgado na hora limpo exato), para evitar ganchos de vazamento nos laços de ciclos cruéis contínuos fechados ríspidos sujos com a pilha bruta da stacktrace rastreadora analítica nativa isolada. Chamar ela dá erro `NameError` mortal estrito.\n\n**IV. Na leitura de um JSON com json.loads, os números com parte decimal são convertidos no tipo Decimal, o que evita os erros de arredondamento do ponto flutuante.**\n**> ERRADO <**\n\nPor padrão nativo bruto isolado do núcleo primitivo raso seco abstrato Python original básico de raiz estipulado padrão oco, json.loads converte tudo quebrado imposto numérico cego solto no float; a conversão blindada contábil financeira contínua pura robusta analítica no c(Decimal) exige injeção dura do parâmetro obscuro avançado profundo analítico nativo relacional de máquina c(`parse_float=Decimal`).\n\n!Regra de Bolso!\n~Lógica~\n**1) SE** você bota um `else` depois da gangue dos `except`, **ENTÃO** você desenhou o Caminho Feliz que só aciona luz verde se nenhuma linha antes sofrer pane cega abstrata dura relacional matemática fechada limpa nativa orgânica viva contábil limítrofe no laço.\n\n!Interpretando a Banca!\n~Gatilho~\nEu sei que parece lógico pensar que no Try-Except o Else faz o papel de \"Se as capturas falharem, roda ele\", igual faz no If-Else tradicional. Mas a fumaça aqui é ardilosa: No fluxo de Exceções do Python, Else significa \"Deu tudo incrivelmente Certo no Try, então premie o usuário rodando essa linha extra de Sucesso\"."
    },
    {
      "type": "normal",
      "id": "ti_ce4_boss_inter_1",
      "subject": "Programação - Boss Intermediário 1",
      "source": "Banca Águia - Boss Intermediário 1",
      "timer_override": 400,
      "front": "**[Chefe Intermediário] - Validação em Lógica Pythonica**\n\nNesta etapa, demonstre sua maestria sobre a carga física, modelagem lógica e mecânica pesada do interpretador Python. Julgue:",
      "stem": [
        "vf(I. Na esteira implacável cirúrgica do Python em Pandas, o comando atrelado primitivo denso orgânico puro abstrato analítico orgânico formal estrito cravado limpo exato vivo de agrupamento formal `transform` reduz taxativamente de forma estática pura o espelhamento do volume das linhas nativas puras originais do dataframe original para um pequeno box resumido achatado analítico numérico local formal e contábil.)",
        "vf(II. A função nativa analítica iteradora orgânica mestre local geradora contínua atrelada do yield tem natureza imutável esgotável e de uso único estrito abstrato contínuo contábil cravado; ela desaba e quebra numa linha vazia sem acionar alerta mortal de erro técnico de barreira se iterada em nova tentativa cega bruta posterior local original na pilha limpa formal.)",
        "vf(III. O bloco de blindagem analítica sistêmica nativa amarrada fina fechada fechada purista viva orgânica `with open(...)` delega aos braços analíticos cegos sujos orgânicos abstratos formais locais puristas originais duros secos soltos da ferramenta coletora universal abstrata Garbage Collector o selo da fechadura limítrofe abstrata no fecho e finalização relacional em caso fatal analítico limpo purista duro exato crônico do desastre abrupto local da Exception nua limpa orgânica exata originária local contínua do banco limpo.)",
        "vf(IV. A varredura estrita cravada contínua lógica algorítmica imbuída num argmax que cruza a fronteira lógica nua de um array preenchido formal purista matemático booleano estrito puro nativo analítico Python retorna ao usuário impiedosamente fielmente isoladamente o valor numérico puro unário cravado do c(primeiro limite estipulado abstrato relacional cravado verdadeiro).) "
      ],
      "options": [
        "C) F, F, F, V.",
        "B) V, V, F, V.",
        "A) F, V, F, V.",
        "D) V, F, V, F.",
        "E) F, V, V, F."
      ],
      "answer": 2,
      "back": "Gabarito: A.\n\n!Otávio!\n~Teoria~\n**1) Checkpoint de Retenção - Python Engine:**\nOs conceitos foram destrinchados, vejamos o nível de aderência dos seus neurônios para as armadilhas sintáticas da prova.\n\n~Gabarito~\n**A) F, V, F, V.**\n\n**I. Na esteira implacável cirúrgica do Python em Pandas...**\n**> ERRADO <**\n\nO `transform` não esmaga nem achata linhas. Ele preserva com unhas e dentes a geometria do grid inteiro original de ponta a ponta e injeta o resumo lá dentro das veias de forma iterativa fina blindada local abstrata formal solta orgânica contínua.\n\n**II. A função nativa analítica iteradora orgânica mestre local geradora contínua atrelada do yield tem natureza imutável...**\n**> CERTO <**\n\nO Gerador Yield é descartável (Single-use puro). Ao terminar de cuspir a fita abstrata solta isolada temporal na memória RAM orgânica bruta de chapa analítica ele entra em silêncio contábil esgotado vazio.\n\n**III. O bloco de blindagem analítica sistêmica nativa amarrada fina fechada...**\n**> ERRADO <**\n\nEle não espera e não delega pro lixeiro frouxo lento contábil cego sujo tardio abstrato nativo orgânico local do Garbage Collector. O With fecha e tranca o cofre fisicamente no milissegundo imediato do impacto letal final bruto da falha sem demora estrita cega abstrata dura.\n\n**IV. A varredura estrita cravada contínua lógica algorítmica...**\n**> CERTO <**\n\nO Numpy Argmax é burro pra booleanos, mas na Engenharia usamos isso como um faro letal e sagaz para farejar o índice (a linha exata abstrata da denúncia do banco original do fraudador) de ocorrência pura isolada contábil fina de primeira linha do primeiro cara cruzando atrelado na fita condicional formal estrita.\n\n!Regra de Bolso!\n~Lógica~\n**1) SE** você ler `.transform`, **ENTÃO** guarde as linhas. Ele amassa a conta, c(mas nunca amassa o número de linhas da planilha inteira abstrata bruta original).\n\n!Break para Respirar!\n~Otávio~\nA armadilha sintática vai testar seu conhecimento frio da RAM versus o CPU local purista orgânico real nativo relacional isolado."
    }
]

deck["cards"].extend(cards)

with open("Simulados Aguia/01/TI/conhecimentos_especificos_4.json", "w", encoding="utf-8") as f:
    json.dump(deck, f, ensure_ascii=False, indent=2)

print("Q134 a Q137 + Boss Intermediário 1 construídos com sucesso!")
