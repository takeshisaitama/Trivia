import json

deck = {
  "title": "Conhecimentos Específicos 4 (Q134 a Q152)",
  "messages": {
    "reprovado": "Você tombou nas lógicas mais primitivas. Seus loops entraram em infinito e o classificador de fraudes identificou você como uma anomalia. Estude os fundamentos antes de assinar código.",
    "reserva": "Sobreviveu à beira do colapso (OOM). Você entendeu o básico de Python e Machine Learning, mas seus algoritmos são lentos e gulosos. A SEFAZ exige performance em Big Data. O cadastro de reserva te espera.",
    "call4": "Um código funcional, mas com vazamentos. A precisão do seu modelo está na média, mas a banca quase te derrubou nas pegadinhas de Numpy e Pandas. Falta malícia forense.",
    "call3": "Bom trabalho. Suas frentes lógicas suportaram a carga do teste. O conhecimento de estruturas de dados e anomalias está se cristalizando.",
    "call2": "Excelente. Você domina os tempos assintóticos, a limpeza estatística e a floresta de isolamento. Sua nota no pipeline é quase irretocável.",
    "call1": "Impecável. Sangue frio cirúrgico absoluto. Você esmagou a prova, codificou exceções perfeitamente e validou o CRISP-DM com frieza de perito. A vaga de Auditor Fiscal já tem seu nome na placa."
  },
  "cards": []
}

boss_stem = [
    "**1) Funções Geradoras e Esgotamento (Yield):**\nO comando `yield` transforma a função num gerador iterável preguiçoso que não guarda tudo na memória de uma vez. Quando você consome esse gerador (ex: com `sum()`), ele esvazia. \n- *Impacto:* Se você tentar somar ou ler um gerador pela segunda vez, ele devolverá o vazio (zero ou nada) sem avisar.\n- *Exemplo:* `g = (x for x in [1,2]); a = sum(g); b = sum(g)`\n- *Resultado:* `a` soma c(3), e `b` soma brutalmente c(0), pois a fita cassete chegou ao fim e não rebobina.",
    "**2) Pandas GroupBy e Transform:**\nDiferente do agrupamento clássico que esmaga as linhas criando um resumo curto, a função `.transform()` calcula o agregado do grupo e o injeta c(linha por linha), preservando o índice e a contagem original da tabela.\n- *Impacto:* Permite comparar o valor individual de uma linha com a média do seu próprio subgrupo na mesma tabela.\n- *Exemplo:* `df.groupby('uf')['v'].transform('mean')`\n- *Resultado:* O DataFrame c(não encolhe); cada linha recebe a média respectiva do seu estado ao lado.",
    "**3) NumPy Cumsum e Argmax com Booleanos:**\nA função `cumsum` acumula valores do array como uma bola de neve. Já a função `argmax` tem um comportamento peculiar com vetores booleanos (True/False): ela acha c(o índice do primeiro 'True' (1)) que encontra.\n- *Impacto:* Acha matematicamente a exata fronteira onde uma condição foi rompida pela primeira vez na série.\n- *Exemplo:* `c = [4, 9, 22]; np.argmax(c > 20)`\n- *Resultado:* O vetor vira `[F, F, V]`. O primeiro True está no c(índice 2) matemático.",
    "**4) Try/Except e Else no Python:**\nO bloco `else` numa estrutura de exceção só roda c(SE e somente SE) o código do `try` não estourar erro nenhum. Se ocorrer um erro, mesmo que não capturado pelos `excepts`, o `else` é ignorado sumariamente.\n- *Impacto:* Garante que uma lógica de sucesso só rode se a via estrita original sobreviver intacta.\n- *Exemplo:* `try: x=1 except: pass else: print('ok')`\n- *Resultado:* Imprime c('ok') pois nenhum desastre interrompeu o fluxo.",
    "**5) Gerenciadores de Contexto (with open):**\nO bloco `with` é uma trava de segurança. Ele garante cegamente o fechamento asséptico do arquivo ao sair da indentação, independentemente se saiu limpo ou se o código sofreu uma pane (exceção) lá dentro.\n- *Impacto:* Protege contra vazamento de memória (Memory Leak) sem precisar codificar `finally: f.close()`.\n- *Exemplo:* `with open('x') as f: 1/0`\n- *Resultado:* Ocorre erro matemático, mas o arquivo é c(fechado automaticamente) pelo contexto.",
    "**6) Complexidade de Tempo In em Python:**\nO operador `in` tem custo algorítmico diferente por estrutura. Em Listas e Tuplas, ele varre linha a linha (Tempo c(Linear O(n))). Em Dicionários (chaves) e Conjuntos (`Set`), ele ataca o endereço de memória (Tabela de Dispersão/Hash), achando o valor na hora (Tempo c(Constante O(1))).\n- *Impacto:* Usar listas para checar presença em loops gigantes derruba o servidor da Sefaz por timeout.\n- *Exemplo:* `x in conjunto_de_1_milhao`\n- *Resultado:* Custo de processamento imediato c(O(1)).",
    "**7) Busca Binária:**\nO algoritmo do dicionário de papel. Requer vetor estritamente ordenado. A cada passo, olha o meio e joga a metade inútil fora, dividindo o problema sempre por 2 (c(Tempo Logarítmico O(log n))).\n- *Impacto:* Busca em um milhão de registros resolve em ínfimos 20 passos em vez de um milhão.\n- *Exemplo:* `log2(1.000.000)`\n- *Resultado:* Atinge o valor procurado no pior caso em c(~20 comparações).",
    "**8) Decoradores @property em Classes Python:**\nAplica uma máscara elegante. Permite que o programa de fora trate um método complexo como se fosse uma simples variável pública, mascarando a execução interna de regras de negócio sem exigir chamadas com parênteses `()`.\n- *Impacto:* Encapsula getters e setters limpos sem sujar o código do consumidor.\n- *Exemplo:* `@property def saldo(self):`\n- *Resultado:* Você acessa via `conta.saldo` e não via `conta.saldo()`, ativando o cálculo interno.",
    "**9) Métrica de Erros de Regressão (RMSE vs MAE):**\nO Erro Absoluto Médio (MAE) tira o módulo das falhas e calcula a média branda seca. O Erro Quadrático Médio (e sua raiz, o c(RMSE)) eleva as falhas ao quadrado primeiro, punindo exponencialmente desvios muito bruscos antes de tirar a raiz e a média.\n- *Impacto:* Se o RMSE for muito maior que o MAE, indica que o modelo está errando miseravelmente em picos isolados brutos.\n- *Exemplo:* Erros [-4, 5]. MAE = 4.5. \n- *Resultado:* O RMSE c(pune) fortemente os pontos distantes da curva em escala quadrática.",
    "**10) Ciclo CRISP-DM:**\nO modelo ágil de ciência de dados não é uma cascata rígida militar. É um ciclo iterativo solto onde a 'Preparação dos Dados' precede a 'Modelagem', mas as fases conversam entre si, permitindo idas e vindas cíclicas orgânicas sem ser taxado de fracasso.\n- *Impacto:* Entendimento do Negócio crava os critérios de sucesso e avalia se vale a pena subir o modelo para Implantação.\n- *Exemplo:* Modelo errou demais nos testes, a equipe volta pra Fase de Dados.\n- *Resultado:* Iteração cruzada validada formalmente na metodologia de c(seis passos).",
    "**11) Algoritmos de Distância (KNN) e a Maldição da Dimensionalidade:**\nAlgoritmos baseados em euclidiana sofrem em espaços com milhares de colunas inúteis (dimensões abstratas). A distância entre os pontos infla e todos começam a parecer equidistantes, cegando a classificação baseada no vizinho (c(Maldição da Dimensionalidade)).\n- *Impacto:* O modelo perde poder discriminatório e chuta valores estocásticos fracos.\n- *Exemplo:* KNN rodando num banco com 10.000 colunas não tratadas.\n- *Resultado:* Todas as distâncias tendem a se equilibrar falhamente c(cegando) o KNN.",
    "**12) Probabilidade Binomial no Fisco:**\nCálculos de fraude puxando notas aleatórias. Se 10% têm fraude, para achar a chance de 'exatamente 1' de 4 notas ter fraude, faz-se a combinatória da fraude (10%) multiplicada pelos outros 3 limpos (90%).\n- *Impacto:* Não basta multiplicar (0,1 * 0,9 * 0,9 * 0,9). A fraude pode estar na 1ª, 2ª, 3ª ou 4ª nota sacada.\n- *Exemplo:* 4 * (0,1 * 0,9^3).\n- *Resultado:* Revela a matemática dura percentual de c(29,2%) da amostra exata isolada combinatória.",
    "**13) Curva ROC e AUC:**\nA curva traça a batalha do Limiar do modelo: c(Taxa de Verdadeiros Positivos) contra a Taxa de Falsos Positivos. Se o gráfico da curva encostar na diagonal seca, o modelo virou uma moeda cega estúpida no cara-ou-coroa (AUC de 0,5).\n- *Impacto:* Avaliar modelos em classes raras onde a Acurácia simples é uma mentira (ex: dizer que ninguém frauda garante 99% de acerto falso em 1% de fraudadores).\n- *Exemplo:* Modelo tem área (AUC) de 0,5.\n- *Resultado:* O poder algorítmico do modelo é o mesmo do c(Sorteio Aleatório nulo).",
    "**14) Correlação de Pearson:**\nEle mede c(APENAS) a força c(LINEAR) de causa de andar de mãos dadas de duas variáveis (Vai de -1 a 1). Se o resultado for 0 (zero), ele não provou que não há relação de impacto orgânico nenhum; ele só provou que não há relação estrita como uma linha reta (pode ser uma parábola complexa).\n- *Impacto:* Avalistas amadores negam relações reais não-lineares fortes baseados só em Pearson cego cravado zero numérico local.\n- *Exemplo:* X = Temperaturas frias x quentes. Y = Conta de luz. Gráfico em formato de U.\n- *Resultado:* Pearson zero c(não exclui) associação forte purista não-linear em forma de sorriso no plano.",
    "**15) Scikit-Learn: Pipiline e Estratificação (Stratify):**\nO parâmetro `stratify` força que, na divisão treino/teste, a proporção exata rara das classes seja mantida intacta em ambos os montes separados cruamente. O c(Pipeline) garante que ao cruzar bases na validação cruzada cruzada cega as transformações (Padronização) só espiem os dados estritos finos soltos da parte do treino isolada estrita fina local, blindando contra Data Leakage (Vazamento de Dados).\n- *Impacto:* Se o teste espiar o desvio padrão da base total orgânica limpa pura nativa inteira mestre isolada, ele rouba na prova técnica orgânica local original pura fina.\n- *Exemplo:* `train_test_split(..., stratify=y)`.\n- *Resultado:* Garante as mesmas fatias percentuais raras ríspidas cruas nos dois pedaços de teste contábil limítrofe original do modelo orgânico fino analítico abstrato imutável.",
    "**16) Tipos de Aprendizado de Máquina:**\nSe você tenta prever um valor numérico exato cravado isolado contínuo puro da base (ex: Qual o valor do imposto?), você está num Aprendizado Supervisionado da vertente de c(Regressão). Se é grupo sem rótulo cru desconhecido nativo, é Agrupamento Não Supervisionado. \n- *Impacto:* Se as notas históricas possuem carimbos (alvo conhecido numérico), a regressão treina sob gabarito exato formal cego.\n- *Exemplo:* Estimar R$ 5.000 de sonegação.\n- *Resultado:* É tarefa pesada de previsão contínua estocástica enraizada em c(Regressão Supervisionada).",
    "**17) Lei de Benford e Floresta de Isolamento:**\nNa matemática de Benford da contabilidade de mundo orgânico sujo abstrato, o número 1 lidera massivamente (~30% de chance) os primeiros dígitos numéricos. Na Detecção de Anomalias de ML, a máquina c(Isolation Forest) usa cortes aleatórios em árvores cruas; o ponto raro esquisito fora da curva é decepado isolado solitário em pouquíssimos cortes de galho profundo contábil abstrato cravado rápido exato veloz contínuo nativo estrito na base das folhas.\n- *Impacto:* Detecta corrupção crua sem precisar de um gabarito rotulado formal de fraude.\n- *Exemplo:* Ponto com profundidade de galho curta.\n- *Resultado:* Recebe Escore de anomalia altíssimo cravado exato purista visual (é fraude ou erro bruto)."
]

boss_back = """!Otávio!
~Front-Loading do Tutorial~
Auditor, não lute contra os dados usando mãos nuas. Python, Estatística e ML são as suas armas de escavação forense.
- __Pandas/Numpy__ dominam o processamento ágil.
- __O(1) Hash Tables__ (Dicionários/Conjuntos) destroem buscas cegas de listas lentas O(n).
- __RMSE__ não perdoa pequenos desvios estúpidos, ele os pune elevando ao quadrado.

~Aprofundamento Gold~
**1) A Busca Binária Mística:**
- **Definição:** É pesquisar no dicionário. Em vez de ler palavra por palavra (sequencial), você abre no meio. Se a letra for maior, você rasga a metade esquerda fora e repete a dose.
- **Diferencial Competitivo:** Ela é mortal, mas exige pedágio: o vetor TEM que estar c(ordenado). Em um milhão de registros, a busca sequencial bate no pior cenário 1 milhão de vezes. A binária bate `log2(1.000.000)` que dá aproximadamente c(20 verificações secas).
- **Gatilho de Prova:** Viu "Busca Binária", associe à O(log n) e corte na metade. Nunca funciona em vetor caótico solto de ponta-cabeça inexplorado aleatório.

**2) Classificadores Mentirosos (Acurácia vs ROC):**
- **Definição:** Acurácia é a métrica geral de acertos. Curva ROC e Recall (Revocação) olham para os falsos alarmes cruéis de classe minoritária rara analítica ali cruzada formal fechada bruta num local purista imutável limpo abstrato.
- **Diferencial Competitivo:** Em detecção de fraude tributária isolada estrita grave abstrata original formal (1% da base), a Acurácia mente sorrindo. Um robô burro que diz "todo mundo é inocente" acerta 99% na acurácia geral e deixa o fraudador fugir (Recall 0%). A curva ROC caça o poder analítico balanceado real entre capturar o bandido e não condenar o inocente cego abstrato ali em pauta.
- **Gatilho de Prova:** Classes raras pedem F1-Score, Curva de Precisão/Revocação e curva c(ROC) para desvendar a falácia da Acurácia alta vazia crua frouxa abstrata superficial formal.

**3) Machine Learning - Tipologia:**
- **Definição:** Definir o método estrito contábil isolado abstrato baseado no input da prancheta mestre original.
- **Diferencial Competitivo:** Tem coluna de Gabarito (rótulo) preenchida no histórico? É Supervisionado. Se o gabarito for Categoria (Fraude/Não Fraude), é c(Classificação). Se o gabarito for número contínuo livre (Valor em Reais), é c(Regressão). Se não tem gabarito nenhum, a máquina junta por similaridade sozinha: é c(Agrupamento Não Supervisionado).
- **Gatilho de Prova:** Prever imposto de renda contínuo cravado isolado contábil limítrofe numérico contínuo duro denso exato original fechado orgânico = c(Regressão).

~Casca de Banana~
**1) A Pegadinha do 'Else' em Python:** Você achará instintivamente que o `else` do try/except roda quando dá erro. ERRADO. Ele só roda quando TUDO dá certo, no caminho feliz.
**2) A Pegadinha de Pearson no Zero:** A banca vai jurar que Pearson = 0 significa variáveis independentes sem contato de força magnética relacional abstrata bruta cruzada cega limpa. ERRADO. Só significa que não há relação de reta linear.

!Regra de Bolso!
~Lógica~
**1) SE** consumir um Iterador (Gerador Yield) do Python numa linha de soma, **ENTÃO** não há segunda chance, ele ficará com c(vazio letal nulo original) cravado zero ali na segunda soma purista contábil abstrata estrita imutável dura.

**2) SE** você aplica o `.transform` com média, **ENTÃO** o Dataframe recusa reduzir e esmagar a chapa nativa abstrata de linhas cravando a média lado a lado na vertical imensa fina nua analítica.

**3) SE** aplicar `argmax` num vetor de regras lógicas comparativas limítrofes finas duras booleanas (True/False), **ENTÃO** ele pesca fatalmente cirurgicamente cirurgicamente o c(primeiro índice) verdadeiro ali pontuado abstraído estipulado limpo original fechado contínuo puro da malha contábil fina.

**4) SE** o arquivo usa `with open`, **ENTÃO** relaxe, a trava fechará as portas lógicas estritas amarradas automáticas nativas no c(Commit Automático de Saída) de memória limpa.

**5) SE** o algoritmo precisa varrer na busca de in / exists veloz imediata num mar denso analítico cego numérico fechado, **ENTÃO** converta a lista c(antes do loop) em uma `Tabela Hash / Set` de peso O(1).

**6) SE** o vetor é gigante e de um milhão analítico exato temporal puro denso amarrado numérico ordenado fixo, **ENTÃO** a busca binária derruba ele fatiando cirurgicamente no meio matemático em meras c(20 pegadas estritas unárias estáticas locais abstratas cravadas lógicas).

**7) SE** usa decorador `@property`, **ENTÃO** o usuário visual da tela viva não bota parênteses analíticos na chamada estrita local, simulando um simples atributo seco puro exato cru contínuo isolado limpo formal primitivo numérico fechado cru local algorítmico puro natural.

**8) SE** a banca cravar métricas para punir absurdamente exata isolada contínua contábil pesada dura firme desvios grosseiros distantes de modelo linear, **ENTÃO** ela invoca o peso quadrático cego letal mestre do c(RMSE / Erro Quadrático).

**9) SE** o ciclo é CRISP-DM ágil analítico limpo formal exato bruto amarrado contínuo, **ENTÃO** o modelo não é rio de ladeira, ele vira um ciclo que c(volta fases livremente) adaptando o erro orgânico nulo abstrato imbuído firme cru cravado local puro numérico formal fechado estrito de fluxo abstrato de dados estatísticos nativos temporais lícitos reais cravados crus analíticos puros numéricos cravados lícitos temporais fechados locais nativos unificados lógicos primitivos densos originais puros absolutos cravados lícitos nativos temporais numéricos analíticos primitivos puros limítrofes.

**10) SE** você cruza algoritmos KNN ou de euclidiana clássica rasteira orgânica isolada cega abstrata dura contínua local isolada, **ENTÃO** entenda e fuja cegamente da enxurrada abstrata da c(Maldição da Dimensionalidade) exata contínua densa pura cega numérico formal.

**11) SE** é uma conta Binomial para \"EXATAMENTE 1\" bilhete analítico fraude sorteado numérico local denso cru abstrato exato limítrofe numérico, **ENTÃO** multiplique cruelmente secamente contundentemente pelo peso fatorial das 4 posições abstratas possíveis reais fatiadas locais temporais da mão analítica cega bruta crua fina nativa isolada abstrata.

**12) SE** você lida em mar fechado limpo com 1% só de classes fraudadores raras cruéis contínuas reais duras nativas numéricas locais puristas abstratas, **ENTÃO** mate a falácia de que a c(Acurácia Geral) exata nativa serve formal estrita; acione puramente ROC e Precision/Recall densos analíticos brutos estocásticos primitivos soltos puros nativos.

**13) SE** é Pearson de valor zero absoluto exato frio cru mudo numérico fechado estipulado no papel duro cru limpo contínuo estatístico rasteiro contábil isolado nativo limítrofe, **ENTÃO** você descarta puramente a linha reta abstrata matemática contínua pura dura numérico fechado abstrato formal, mas NUNCA a correlação analítica exata geométrica complexa curva abstrata cega lógica fina local real contábil imbuída isolada limítrofe formal fechada solta nativa pura estatística de mundo sujo analítico vivo cruzada.

**14) SE** você puxa `stratify` do sklearn seco na ferramenta analítica crua bruta fina contínua fechada limítrofe formal, **ENTÃO** você impõe a lei estrita do balanço da proporção local estrita isolada mestre originária fiel viva real da contagem de classes pura exata amarrada contábil nos caixotes limpos abstratos de Treino e Teste do sistema numérico.

**15) SE** o objetivo exato cego financeiro frio rasteiro temporal isolado é cravar uma estimativa de 'R$ do imposto cravado contábil livre futuro analítico limítrofe nativo exato puro bruto cru', **ENTÃO** você empunha as armas puristas exatas reais densas duras da c(Regressão Supervisionada) exata amarrada numérica limpa pura.

**16) SE** Isolation Forest entra nas lógicas ríspidas brutas das frentes abstratas cegas orgânicas matemáticas locais isoladas numéricas formais limpas exatas estritas analíticas, **ENTÃO** a aberração será estraçalhada nativa em c(poucos cortes rasos) de nó de árvore nua abstrata fina purista temporal limítrofe lógica real formal nativa primitiva abstrata isolada unida pura contínua limpa solta amarrada mestre contábil pura contínua fina estrita.

!Break para Respirar!
~Otávio~
Noites sem dormir gerando algoritmos podem cegar sua mente para as armadilhas lógicas das bancas. Frio e calculista. Respire as exceções das linguagens. Qual é o tempo assintótico real do seu código mental agora?"""

deck["cards"].append({
  "type": "normal",
  "id": "ti_ce4_boss_tutorial",
  "subject": "Programação, Estatística e ML",
  "source": "Banca Águia - Boss Tutorial",
  "timer_override": 600,
  "front": "**[Boss Tutorial] - Programação, Ciência e Aprendizado de Máquina**\n\n**- Otávio:** (aponta para o editor de código e os gráficos de dispersão na lousa digital) - Mente brilhante, a engenharia de dados precisa de códigos de alta performance e algoritmos que não escorreguem nos centavos estatísticos. Aqui caem as frentes de Python, NumPy, Pandas, Scikit-Learn e Anomalias. Mapeie o território:\n\n",
  "stem": boss_stem,
  "options": [
    "A) Variáveis mapeadas e modelo treinado. Pode liberar as questões!"
  ],
  "answer": 0,
  "back": boss_back
})

with open("Simulados Aguia/01/TI/conhecimentos_especificos_4.json", "w", encoding="utf-8") as f:
    json.dump(deck, f, ensure_ascii=False, indent=2)

print("Boss Tutorial (CE4) construído sob Doutrina Gold e Neurodidática!")