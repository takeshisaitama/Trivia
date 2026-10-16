import json

data = {
  "messages": {
    "aprovado": "Parabéns, você dominou os conceitos finais!"
  },
  "cards": [
    {
      "type": "normal",
      "id": "ti_ce6_boss_tutorial",
      "subject": "Auditoria de TI e Inglês Técnico",
      "source": "Banca Águia - Boss Tutorial",
      "timer_override": 600,
      "front": "**[Boss Tutorial] - Otávio:**\n(abre o painel de auditoria final)\n- Estrategista, este é o último bloco. Vamos mapear os conceitos de Auditoria de Sistemas (CAATs), Bancos de Dados, Inteligência Artificial e a leitura instrumental do Inglês Técnico. Estude o verso com atenção:",
      "stem": [
        "vf(1. O teste de sequência examina a numeração aguardada e não os totais genéricos: ausências não se anulam com duplicidades; se há 2 duplicatas e faltam 4 números, são problemas independentes.)",
        "vf(2. A Simulação Paralela submete os dados de teste fictícios ao sistema em produção para verificação de limites e saldos.)",
        "vf(3. Módulos de auditoria embutidos ficam fora do sistema operando após o processamento com as cópias de dados extraídas das bases.)",
        "vf(4. A padronização da chave primária (como CNPJ de 14 dígitos formatado como texto) evita cruzamentos falsos gerados por exclusão de zeros à esquerda em chaves numéricas inteiras.)",
        "vf(5. No SQL, a função agregadora COUNT() e SUM() atua no conjunto filtrado pelo WHERE, logo, registros descartados nas condições não afetam as somatórias e a contagem final das linhas.)",
        "vf(6. O uso de IA (LLMs) em auditoria encerra a fase de averiguação: as resenhas criadas pela máquina ou escores de ML são provas definitivas incontestes perante o TCU.)",
        "vf(7. Termos em inglês fiscal: \"In its own right\" significa por si mesmo/próprio direito, e \"regardless of\" introduz uma ideia condicional.)"
      ],
      "options": [
        "A) Estou pronto para a revisão. Pode soltar os chefes!"
      ],
      "answer": 0,
      "back": "Gabarito: A.\n\n!Otávio!\n~Teoria~\n **1) Matemática da Sequência:** \n **Como aparece:** \nA questão lista registros que possuem duplicatas e falhas na ordem, pedindo a quantia de furos.\n **Pegadinha:** \nO candidato usa o número final de linhas para abater a numeração, c(mascarando) furos com as duplicatas.\n **Decisão:** \nAnalise o conjunto c(esperado). Se era de 1 a 20 (20 itens) e você achou apenas 16 distintos, faltam 4. Duplicatas são outro problema contabilizado à parte.\n\n **2) Técnicas CAATs (Simulação Paralela vs. Dados de Teste):** \n **Como aparece:** \nAs bancas invertem os conceitos de CAATs.\n **Pegadinha:** \nDizer que a Simulação Paralela usa dados fictícios.\n **Decisão:** \nc(Dados de Teste): Fictícios jogados no sistema real para ver se ele engasga com lixo.\nc(Simulação Paralela): O auditor pega dados reais e joga no programa DELE para comparar com o resultado do sistema.\n\n **3) Módulos Embutidos (Embedded Audit Modules):** \n **Como aparece:** \nA banca diz que o módulo roda fora do sistema ou numa cópia velha.\n **Pegadinha:** \nSeparar o módulo da aplicação viva.\n **Decisão:** \nEles habitam c(dentro) do sistema vivo, em produção, capturando fraudes em tempo real.\n\n **4) Padronização de Chaves (Joins):** \n **Como aparece:** \nA banca sugere converter CNPJ para INTEIRO (INT) para economizar bytes.\n **Pegadinha:** \nO candidato acha que número e INT são sempre melhores.\n **Decisão:** \nCNPJ convertido para Inteiro perde os zeros à esquerda, quebrando a chave de cruzamento (Join). O ideal é formatar como c(Texto) padronizado (14 posições com zeros preservados).\n\n **5) Restrições SQL (O Filtro WHERE):** \n **Como aparece:** \nUm emaranhado de datas e condições cruzadas com COUNT e SUM.\n **Pegadinha:** \nO candidato soma a tabela inteira e ignora as barreiras do WHERE.\n **Decisão:** \nA cláusula c(WHERE) passa um rodo na tabela antes. O que não atende as condições temporais ou de categoria cai no lixo e não vai para a agregação c(SUM).\n\n **6) Limites da IA na Auditoria:** \n **Como aparece:** \nA banca sugere que a IA ou o ML são autônomos e substituem a prova material.\n **Pegadinha:** \nAcreditar que a IA e a predição são provas judiciais ou fechamento de caso.\n **Decisão:** \nA IA ajuda na c(triagem). As conclusões e evidências devem ser sempre lastreadas no c(documento original) conferido pelo olho humano do auditor. IA também não tem \"sigilo\" garantido em plataformas públicas gratuitas da web.\n\n **7) Termos do Inglês (Regardless of e In its own right):** \n **Como aparece:** \nA banca pede o sentido e o sinônimo da conjunção e expressão idiomática.\n **Pegadinha:** \nDizer que Regardless of é condição, e In its own right é posse de direito/autoral.\n **Decisão:** \nc(In its own right): Por si mesmo / Como um problema próprio. \nc(Regardless of): Concessão / Independentemente de.\n\n!Regra de Bolso!\n~Lógica~\n**1) SE** é Simulação Paralela, **ENTÃO** são dados reais no programa fictício do auditor.\n**2) SE** é Dados de Teste, **ENTÃO** são dados fictícios no programa real.\n**3) SE** é Regardless of, **ENTÃO** é a ideia de Concessão.\n\n!Break para Respirar!\n~Otávio~\n- Tudo anotado? Nesse bloco, você não apenas vai analisar as funções, mas sim hackear a intenção do sistema, o SQL puro e a língua inglesa."
    },
    {
      "type": "normal",
      "id": "ti_ce6_q172",
      "subject": "Auditoria de Sistemas - Teste de Sequência",
      "source": "Banca Águia - Q172",
      "timer_override": 300,
      "front": "**Questão 172:**\n\nUma série de notas fiscais de entrada deveria conter os números de 501 a 520. A base extraída do sistema trouxe os seguintes números, já ordenados: 501, 502, 503, 505, 506, 506, 507, 510, 511, 512, 513, 513, 514, 515, 517, 518, 519 e 520. A quantidade de números ausentes da sequência e a quantidade de números que aparecem em duplicidade são, respectivamente:",
      "stem": [],
      "options": [
        "A) 4 e 2.",
        "B) 2 e 0.",
        "C) 3 e 2.",
        "D) 4 e 4.",
        "E) 2 e 2."
      ],
      "answer": 0,
      "back": "Gabarito: A.\n\n!Otávio!\n~Teoria~\n**1) Teste de Sequência:**\nEm auditoria contábil e de TI, os furos (gaps) numéricos indicam ocultação de receitas ou documentos excluídos; as duplicatas indicam injeções ilícitas de faturamento repetido. Eles não se compensam algebricamente. \n\n~Gabarito~\n**A) 4 e 2.**\n**> CERTO <**\n**Passo 1 — Os números distintos:** A faixa original é de 501 a 520. Logo, deveríamos ter c(20 números) exatos.\nOlhando para a lista, temos as duplicatas dos números 506 e 513. Ou seja, dos 18 registros que temos em mãos, há apenas c(16 números distintos).\n**Passo 2 — Quantidade ausente:** Se esperávamos 20 números, e temos 16 distintos, faltam c(4 números) reais na sequência (504, 508, 509 e 516).\n**Passo 3 — Quantidade de duplicatas:** Apenas dois números são fraudes de repetição (o 506 e o 513). Logo, há c(2) números em duplicidade.\n\n~Gentalha~\n**B) 2 e 0.**\n**> ERRADO <**\nO candidato apenas observou a contagem bruta de registros da tabela (18) e subtraiu da expectativa (20), mascarando a gravidade das ausências, já que as duplicatas maquiaram a contagem bruta.\n\n**C) 3 e 2.**\n**> ERRADO <**\nO candidato olhou o buraco entre 507 e 510, viu que faltam 508 e 509, e contou essas ausências contíguas como uma \"única\" lacuna visual, o que é um equívoco numérico.\n\n**D) 4 e 4.**\n**> ERRADO <**\nConta os 4 registros envolvidos na treta (duas vezes o 506 e duas vezes o 513), em vez de contar que a quantidade \"de números\" duplicados são apenas dois em essência.\n\n**E) 2 e 2.**\n**> ERRADO <**\nToma apenas a diferença algébrica bruta de contagem (20 - 18 = 2 registros faltantes), ignorando as distorções das repetidas.\n\n!Regra de Bolso!\n~Lógica~\n**1) SE** você vai aplicar teste de gaps sequenciais, **ENTÃO** você deve extrair o esqueleto de números c(Distintos) (únicos) da base suja e descontar do Total Esperado, sob pena da duplicata abafar e mascarar um buraco.\n\n!Interpretando a Banca!\n~Gatilho~\nA banca fornece uma lista enganosa de 18 itens para você, no pânico do relógio, pensar: \"Bom, de 18 pra 20, faltam 2\". E ela até escondeu a malícia. Nunca subtraia contagem crua."
    },
    {
      "type": "normal",
      "id": "ti_ce6_q173",
      "subject": "Auditoria de Sistemas - CAATs",
      "source": "Banca Águia - Q173",
      "timer_override": 180,
      "front": "**Questão 173:**\n\nAcerca das técnicas de auditoria assistidas por computador, julgue as afirmativas a seguir em verdadeiras (V) ou falsas (F).\n\nA sequência correta, de cima para baixo, é:",
      "stem": [
        "vf(I. Na simulação paralela, o auditor submete dados de teste fictícios ao sistema em produção e compara os resultados obtidos com os resultados esperados.)",
        "vf(II. Os módulos de auditoria embutidos são programas executados pelo auditor fora do sistema, após o processamento, sobre cópias das bases extraídas.)",
        "vf(III. Na técnica de dados de teste, o auditor processa transações fictícias, preparadas com resultados conhecidos, para verificar se os controles do programa funcionam como esperado.)",
        "vf(IV. A instalação de teste integrada cria uma entidade fictícia no sistema em produção, por meio da qual transações de teste são processadas com as reais, o que exige cuidado para que não afetem os relatórios oficiais.)"
      ],
      "options": [
        "A) F, F, V, V.",
        "B) F, V, V, V.",
        "C) F, V, V, F.",
        "D) V, V, V, V.",
        "E) F, F, F, V."
      ],
      "answer": 0,
      "back": "Gabarito: A.\n\n!Otávio!\n~Teoria~\n**Técnicas de CAATs:**\nO auditor não audita apenas a tabela final do banco, ele audita a inteligência do código do governo. Se o programa do governo for falho, a tabela nasce corrompida.\n\n~Gabarito~\n**A) F, F, V, V.**\n\n**I. (F)**\n**> ERRADO <**\nA assertiva descreve a técnica de c(Dados de Teste) crua. Na Simulação Paralela (Parallel Simulation), o auditor reprocessa os dados da produção c(reais) rodando tudo em um código dele mesmo (um programa próprio do auditor) que emula o do ente para provar a distorção.\n\n**II. (F)**\n**> ERRADO <**\nOs módulos embutidos (Embedded Audit Modules) habitam as veias vivas c(dentro) do sistema do cliente em tempo de execução contínua, extraindo ou alarmando o auditor sobre lixo contábil inserido online na nuvem do ente. Eles NÃO operam fora em cópias antigas frias e estáticas.\n\n**III. (V)**\n**> CERTO <**\nEsta é a essência do CAAT de Dados de Teste: injeção de lixo proposital fictício montado pela auditoria no tubo original do ente para descobrir se o validador dele (IFs do código) ejeta o lixo ou se o lixo o contamina.\n\n**IV. (V)**\n**> CERTO <**\nA ITF (Integrated Test Facility) anexa uma base de CNPJ sombra (\"entidade fictícia de testes\") na fábrica vital viva real (produção). O cuidado máximo recai na barreira contábil obrigatória de c(desfazer as reversões fictícias) do teste antes do fechamento financeiro, senão a inflação orçamentária é maquiada pro TCU.\n\n!Regra de Bolso!\n~Lógica~\n**1) SE** a técnica usa um espelho do código do ente refeito na linguagem e no colo analítico puro estrito do auditor rodando dados originais do Estado, **ENTÃO** isso responde pelo nome sagrado de c(Simulação Paralela).\n\n!Interpretando a Banca!\n~Gatilho~\nA banca sempre inverte os sujeitos e os dados de \"Simulação Paralela\" e \"Dados de Teste\". A chave é memorizar: quem forneceu os dados? E quem forneceu o código? Na paralela, o código é do auditor, e o dado é real."
    },
    {
      "type": "normal",
      "id": "ti_ce6_q174",
      "subject": "Banco de Dados - Chave de Cruzamento",
      "source": "Banca Águia - Q174",
      "timer_override": 180,
      "front": "**Questão 174:**\n\nPara cruzar a base de pagamentos do sistema financeiro com a base de contratos do sistema de compras, o auditor precisa definir a chave de cruzamento e o tipo de junção. Acerca desse cruzamento, é correto afirmar que:",
      "stem": [],
      "options": [
        "A) a chave de cruzamento deve ser padronizada nas duas bases, como o CNPJ em texto de 14 posições, com zeros à esquerda, para evitar falsas ausências.",
        "B) a conversão do CNPJ em número inteiro preserva os zeros à esquerda e, por isso, é a forma indicada de padronizar a chave de cruzamento entre as bases.",
        "C) a junção interna entre pagamentos e contratos revela os pagamentos sem contrato correspondente, que são o objeto principal do teste de auditoria.",
        "D) a razão social do fornecedor é chave de cruzamento mais confiável que o CNPJ, por ser menos sujeita a erros de digitação e a abreviações nos cadastros.",
        "E) datas gravadas como texto em formatos diferentes, como DD/MM/AAAA e AAAA-MM-DD, podem ser comparadas diretamente, por representarem as mesmas datas."
      ],
      "answer": 0,
      "back": "Gabarito: A.\n\n!Otávio!\n~Teoria~\n**1) Preparação de Base e Chaves (Joins):**\nBancos de dados são burros. Eles comparam strings literais. Se a máscara não tiver perfeitamente idêntica, o JOIN falha miseravelmente devolvendo vazio ou ausência.\n\n~Gabarito~\n**A) a chave de cruzamento deve ser padronizada nas duas bases, como o CNPJ em texto de 14 posições, com zeros à esquerda, para evitar falsas ausências.**\n**> CERTO <**\nPadronizar o tipo (string/texto), o tamanho e o preenchimento (lpad com 0 à esquerda) garante que o número 01.111.111 e o 1.111.111 se cruzem harmoniosamente sem a rejeição visual estrita do motor do banco.\n\n~Gentalha~\n**B) A conversão do CNPJ em número inteiro preserva os zeros.**\n**> ERRADO <**\nA conversão em Inteiro (INT) fatalmente arranca os zeros inúteis matemáticos cruamente, matando o padrão de formatação e afundando o match relacional.\n\n**C) A junção interna revela os pagamentos sem contrato.**\n**> ERRADO <**\nA Junção Interna (INNER JOIN) devolve SOMENTE os cruzamentos que deram match. O que ficar de fora do contrato no sistema de pagamentos será tragado pela Anti-junção (Anti-join) ou revelado no estrito limite limpo de um LEFT JOIN filtrado com condição nula (IS NULL).\n\n**D) Razão social do fornecedor é mais confiável.**\n**> ERRADO <**\nO nome do boteco \"Bar do Tião\", \"BAR TIAO LTDA\", \"Tiao Bar\" é um caos na grafia humana (Abreviações). O número identificador exato limítrofe (CNPJ) é a arma superior, cega, livre de interpretações formais.\n\n**E) Datas de formato texto são comparadas diretamente.**\n**> ERRADO <**\nA máquina cruza bytes cegos literais; um texto '31/12/2026' destoa frontalmente do texto '2026-12-31'. O cruzamento morre antes do teste relacional contábil iniciar.\n\n!Regra de Bolso!\n~Lógica~\n**1) SE** você cruzar CNPJ entre tabelas orçamentárias, **ENTÃO** você formata tudo para VARCHAR (Texto) com preenchimento limpo padrão estrito cravado, fugindo absurdamente dos Inteiros que comeriam o zero cego primário limitante.\n\n!Interpretando a Banca!\n~Gatilho~\nA banca apela para o senso comum de quem acha que Inner Join busca erros, mas o Inner busca paridade. Pra achar os solteiros sem par no banco (os pagamentos anômalos sem contrato) você precisa de junção periférica."
    },
    {
      "type": "normal",
      "id": "ti_ce6_q175",
      "subject": "Banco de Dados - SQL",
      "source": "Banca Águia - Q175",
      "timer_override": 300,
      "front": "**Questão 175:**\n\nA tabela despesas registra a data do fato gerador (dt_fato), a data da liquidação (dt_liq), a indicação de inscrição em restos a pagar (rp) e o valor, em milhares de reais, de despesas de um órgão.\n\n| doc | dt_fato | dt_liq | rp | valor |\n|---|---|---|---|---|\n| D1 | 2025-12-15 | 2026-01-10 | N | 20 |\n| D2 | 2025-12-28 | 2026-01-05 | S | 30 |\n| D3 | 2026-01-02 | 2026-01-08 | N | 15 |\n| D4 | 2025-11-30 | 2026-02-03 | N | 12 |\n| D5 | 2025-12-31 | 2025-12-31 | N | 40 |\n| D6 | 2025-12-20 | 2026-01-15 | N | 13 |\n\nPara identificar despesas com fato gerador em 2025, liquidadas em 2026 e sem inscrição em restos a pagar, o auditor executou a consulta a seguir.\n\n```sql\nSELECT COUNT(*), SUM(valor)\nFROM despesas\nWHERE dt_fato < '2026-01-01'\nAND dt_liq >= '2026-01-01'\nAND rp = 'N';\n```\n\nOs valores retornados por COUNT(*) e por SUM(valor) são, respectivamente:",
      "stem": [],
      "options": [
        "A) 3 e 45.",
        "B) 4 e 75.",
        "C) 4 e 60.",
        "D) 2 e 33.",
        "E) 5 e 90."
      ],
      "answer": 0,
      "back": "Gabarito: A.\n\n!Otávio!\n~Teoria~\n**1) Análise de Filtros Sucessivos (WHERE com AND):**\nO filtro funciona como peneiras seguidas. Basta falhar numa condição para a linha inteira ser ejetada do somatório final. As condições exigidas eram: ser anterior a 2026 no fato, posterior ou igual a 2026 na liquidação, e sem RP.\n\n~Gabarito~\n**A) 3 e 45.**\n**> CERTO <**\n**Peneira 1 — Fato gerador estrito cravado antes de 2026:** \nFicam as linhas: D1, D2, D4, D5 e D6. (A D3 teve fato gerador já em 2026, fora).\n**Peneira 2 — Liquidação estrita original dentro de 2026:** \nEntre as sobreviventes, D5 foi liquidada em dezembro de 2025 (velha). Ela sai. \nRestam: D1, D2, D4 e D6.\n**Peneira 3 — Sem restos a pagar (rp='N'):** \nA linha D2 foi inscrita formalmente em restos a pagar (rp='S'). Ela sai.\nSobreviventes do rito de auditoria puro: c(D1, D4 e D6).\n\n**O Agregador Final:**\nCOUNT(As linhas vivas) = c(3) relatórios.\nSUM(Valores vivos de D1 + D4 + D6) = 20 + 12 + 13 = c(45).\n\n~Gentalha~\n**B) 4 e 75.**\n**> ERRADO <**\nO candidato ignora violentamente o filtro do restos a pagar de \"N\", trazendo a gorda falha de D2 (30 k) para o bolo analítico purista de 45 e inchando os contadores.\n\n**C) 4 e 60.**\n**> ERRADO <**\nO candidato cego esquece a barreira brutal analítica do fato gerador, agregando amadoramente D3 no agrupamento restritivo nativo.\n\n**D) 2 e 33.**\n**> ERRADO <**\nO descuidado remove a D4 sem motivo por ter liq em fevereiro, quando na verdade ela atende perfeitamente ao corte estrito solto formal bruto (>= jan/26).\n\n**E) 5 e 90.**\n**> ERRADO <**\nIgnora todos os recortes de filtro WHERE estritos de junção AND.\n\n!Regra de Bolso!\n~Lógica~\n**1) SE** você ler comandos com \"AND\" atrelados em WHERE sequencial, **ENTÃO** aplique os cortes brutalmente um por um e risque a caneta a linha descartada; o banco só contará as ilesas.\n\n!Interpretando a Banca!\n~Gatilho~\nA banca testa a competência orçamentária do fato gerador atrelado cruzado com o pagamento diferido de despesas passadas que burla os bloqueios contábeis."
    },
    {
      "type": "normal",
      "id": "ti_ce6_q176",
      "subject": "Inteligência Artificial na Auditoria",
      "source": "Banca Águia - Q176",
      "timer_override": 180,
      "front": "**Questão 176:**\n\nJulgue os itens a seguir, relativos ao uso de inteligência artificial e de ferramentas analíticas em trabalhos de auditoria.\n\nEstão corretos os itens:",
      "stem": [
        "vf(I. O uso de modelo de linguagem para resumir cláusulas de contratos pode acelerar a triagem, desde que as conclusões que fundamentem achados sejam conferidas no texto original do contrato.)",
        "vf(II. Os escores de um modelo de risco validado com dados históricos constituem evidência suficiente de irregularidade nos casos sinalizados, o que encerra a etapa de exame desses casos.)",
        "vf(III. A reprodutibilidade de uma análise de dados em auditoria fica assegurada com o arquivamento do relatório final e das planilhas de resultado, que permitem refazer a análise.)",
        "vf(IV. O envio de documentos com dados de contribuintes a um serviço gratuito de IA generativa na internet preserva o sigilo fiscal, porque o serviço não armazena o conteúdo das conversas.)"
      ],
      "options": [
        "A) I e IV.",
        "B) I, II e IV.",
        "C) Todos os itens estão incorretos.",
        "D) I.",
        "E) I, III e IV."
      ],
      "answer": 3,
      "back": "Gabarito: D.\n\n!Otávio!\n~Teoria~\n**Automação vs. Juízo de Valor:**\nA IA é um assistente rápido que sofre de alucinação algorítmica; as evidências não pertencem ao código, e o juiz contábil não aceita o output da IA como sentença de culpa.\n\n~Gabarito~\n**D) I.**\n**> CERTO (Apenas I) <**\n**I. (V)** O uso da ferramenta abstrata purista exata de linguagem acelera absurdamente a triagem viva; contudo, a responsabilidade e o lastro exigem a confirmação presencial estrita formal limítrofe no núcleo do texto físico validado da empresa.\n\n~Gentalha~\n**II. (F)**\n**> ERRADO <**\nNenhum escore preditivo estatístico analítico exato encerra caso contábil; ele não é sentença. O escore apenas cria a \"prioridade de trilha\", exigindo brutalmente o olho pericial do humano na frente limítrofe material do fato investigado real bruto amarrado purista.\n\n**III. (F)**\n**> ERRADO <**\nRelatório cego limítrofe de output final e planilha de resultado final morta exata estrita nativa NUNCA provam reprodutibilidade orgânica. A ciência reproduz se arquivar os c(DADOS ORIGINAIS), c(CÓDIGOS-FONTES/Scripts de ETL) e as chaves sementes formais.\n\n**IV. (F)**\n**> ERRADO <**\nA ingenuidade cibernética de jogar dado sigiloso fiscal denso bruto numérico protegido unificado em Chatbots públicos na web livre é suicídio de cargo. A política global é clara de que as plataformas abertas treinam suas raízes puristas cegas com as perguntas puras do cidadão.\n\n!Regra de Bolso!\n~Lógica~\n**1) SE** a banca afirmar que a Inteligência Artificial encerrou a auditoria, que suas previsões são absolutas na lousa jurídica ou que não precisa de lastro humano, **ENTÃO** você tem uma sentença c(Falsa) absoluta no painel de TI Público.\n\n!Interpretando a Banca!\n~Gatilho~\nA doutrina do TCU já blindou: algoritmos facilitam, mas não julgam por si mesmos e o código precisa ser explicável/auditável (White Box)."
    },
    {
      "type": "normal",
      "id": "ti_ce6_boss_inter_1",
      "subject": "Auditoria de TI - Chefe Intermediário",
      "source": "Banca Águia - Boss Intermediário",
      "timer_override": 400,
      "front": "**[Chefe Intermediário] - Revisão Rápida CAATs e SQL**\n\n- Otávio: (desdobra o mapa de auditoria de logs no laboratório pericial) - O tempo urge, estrategista. Valide as assertivas do pátio cibernético estatal:\n\nA sequência correta, de cima para baixo, é:",
      "stem": [
        "vf(I. Na simulação paralela nativa cega amarrada analítica, os dados originais puros crus vivos nativos originais do sistema são lançados num programa de espelho analítico purista atrelado cego feito pelo próprio fiscal contínuo mestre formador do laudo orgânico.)",
        "vf(II. A chave de integração de CNPJs puros lógicos numéricos deve priorizar imperativamente implacavelmente a conversão estrita direta para inteiros (INT) cravando e forçando a redução formal de formatação contínua de memória original na máscara nativa.)",
        "vf(III. A injeção estrita atrelada de Dados de Teste no seio puro vivo real sistêmico do ente demanda puramente e restritivamente contínuo uso das artimanhas reais originais limpas orgânicas para estourar o limite de validação local unificada analítica.)",
        "vf(IV. Ausências numéricas orgânicas na fita serial são neutralizadas pela contagem geral unificada se houver as distorções espelhadas puristas cegas equivalentes e puristas cruas nas repetições no cálculo geral da auditoria de fita limítrofe pura.)"
      ],
      "options": [
        "A) V, F, F, F.",
        "B) F, F, V, V.",
        "C) V, V, F, F.",
        "D) F, V, V, F.",
        "E) V, V, V, V."
      ],
      "answer": 0,
      "back": "Gabarito: A.\n\n!Otávio!\n~Teoria~\n**Retenção e Fixação Estratégica:**\nAuditoria pura é exatidão: dados trocados quebram métodos.\n\n~Gabarito~\n**A) V, F, F, F.**\n\n**I. (V) Simulação Paralela:**\n**> CERTO <**\nÉ isso mesmo. O dado c(REAL) da prefeitura é jogado no código c(FICTÍCIO) (Criado) pelo auditor e depois ele compara o output.\n\n**II. (F) CNPJ para INT:**\n**> ERRADO <**\nA conversão INT cravada aniquila os zeros iniciais puros. CNPJ formatado no banco deve ser mantido como STRING lpad para bater nos Joins exatos.\n\n**III. (F) Dados de Teste usa dados reais:**\n**> ERRADO <**\nDados de Teste são lixos e casos fictícios inventados (Eles NÃO SÃO dados originais/reais orgânicos) para bombardear e estourar a validação purista cega real do ente.\n\n**IV. (F) Compensação de Ausências com Duplicatas:**\n**> ERRADO <**\nAusência é ausência. Duplicata é fraude. Você NUNCA abate buracos sequenciais estritos puros analíticos puristas da fita original local mascarando no saldo somatório global cego impuro com lixo injetado nela.\n\n!Regra de Bolso!\n~Lógica~\n**1) SE** é Simulação Paralela, **ENTÃO** você tem no seu notebook purista cego estrito analítico o c(Programa Autoral Seu) espelhando a fraude.\n\n!Break para Respirar!\n~Otávio~\n- Memorizou a diferença? As bancas vivem no looping eterno de te empurrar CAATs com os nomes trocados."
    },
    {
      "type": "normal",
      "id": "ti_ce6_q177",
      "subject": "Inglês Técnico - Interpretação",
      "source": "Banca Águia - Q177",
      "timer_override": 180,
      "front": "**Questão 177:**\n\nTEXT — Read the text below and answer questions 177 to 179.\n\nElectronic invoicing has changed the way tax administrations follow economic activity. Each invoice issued by a registered business is transmitted to the tax authority before the goods leave the warehouse, so auditors no longer wait for periodic returns to learn what was sold. This flow of data, however, does not audit itself. Invoices may be cancelled shortly after authorization, issued to companies that have no real activity, or split into small amounts to stay below the thresholds that would trigger a closer review.\n\nDetecting such patterns requires models that combine invoice data with registration records, payment information and, increasingly, data shared by other states. Analysts warn that the volume of alerts can become a problem in its own right. A model that flags too many transactions overwhelms the audit teams, who end up choosing cases almost at random.\n\nFor this reason, several administrations now rank alerts by expected revenue and record the outcome of every review. The aim is to feed those outcomes back into the models, so that they are recalibrated with real results rather than with the assumptions of whoever designed them.\n\nAccording to the text, the main point made about electronic invoicing is that:",
      "stem": [],
      "options": [
        "A) it has replaced the work of audit teams, since every transaction now reaches the tax authority before the goods are shipped.",
        "B) its main weakness is the delay between the sale and the transmission of the invoice to the tax authority.",
        "C) it requires models designed to raise the number of alerts and reduce the irregular invoices that escape review.",
        "D) it has made companies with no real activity the main source of irregular invoices in other states.",
        "E) the data it generates is valuable, but effective audits depend on analytical models and on keeping alerts manageable."
      ],
      "answer": 4,
      "back": "Gabarito: E.\n\n!Otávio!\n~Teoria~\n**A Ideia Central (Main Point):**\nTextos de Inglês Técnico na SEFAZ não pedem tradução solta; pedem síntese. O texto diz: a nota eletrônica jorra dados geniais, MAS (\"however\") o volume brutal estrangula a auditoria sem um modelo que afine os alarmes.\n\n~Gabarito~\n**E) the data it generates is valuable, but effective audits depend on analytical models and on keeping alerts manageable.**\n**> CERTO <**\n(O dado é valioso, mas auditorias eficazes dependem de modelos e de manter os alertas gerenciáveis). É a resenha perfeita do parágrafo 1 (\"does not audit itself\") e 2 (\"volume of alerts can become a problem\").\n\n~Gentalha~\n**A) it has replaced the work of audit teams...**\n**> ERRADO <**\n(Substituiu o trabalho humano). O texto diz exatamente o contrário, a nota não se audita sozinha, exigindo fortemente o escrutínio e trabalho fino estrito da equipe de revisão de campo analítica.\n\n**B) its main weakness is the delay...**\n**> ERRADO <**\n(Fraqueza principal é o atraso). O texto glorifica o fato de que a nota c(NÃO tem atraso) e chega na veia \"before the goods leave the warehouse\" (antes da mercadoria sair do chão de fábrica estrito local).\n\n**C) it requires models designed to raise the number of alerts...**\n**> ERRADO <**\n(Aumentar o número de alertas). A tese é o c(inverso); alertas demais em massa \"overwhelms the audit teams\" (esmagam o time), forçando avaliações desleixadas na ponta nativa randômica aleatória solta limítrofe.\n\n**D) it has made companies with no real activity the main source...**\n**> ERRADO <**\nNão cita em lugar nenhum a métrica exclusivista quantitativa limítrofe brutal purista exata de que empresas-fantasma são a c(maior fonte) principal. Apenas aponta como um dos subpadrões de sonegação local solta atrelada original.\n\n!Regra de Bolso!\n~Lógica~\n**1) SE** você tem um texto com um \"However\" (Entretanto/Mas) logo no primeiro parágrafo, **ENTÃO** a Tese Principal/Main Point é c(SEMPRE) a ressalva que vem logo depois dele (a máquina de dados não se audita sozinha, precisa ser domada).\n\n!Interpretando a Banca!\n~Gatilho~\nA banca joga os extremismos no Inglês (\"replaced work\", \"main weakness\", \"raise alerts\") para ver se você traduz o macro em vez de bater palavra-chave cega. Leia os tópicos frasais estritos."
    },
    {
      "type": "normal",
      "id": "ti_ce6_q178",
      "subject": "Inglês Técnico - Idioms",
      "source": "Banca Águia - Q178",
      "timer_override": 180,
      "front": "**Questão 178:**\n\nIn the second paragraph, the expression “in its own right” indicates that the volume of alerts:",
      "stem": [],
      "options": [
        "A) results from invoices cancelled shortly after being authorized by the tax authority.",
        "B) solves the problem of audit teams that choose cases almost at random.",
        "C) matters less than the patterns described in the first paragraph of the text.",
        "D) is a problem in itself, distinct from the irregularities the models try to detect.",
        "E) belongs to the audit teams, who are responsible for designing the models."
      ],
      "answer": 3,
      "back": "Gabarito: D.\n\n!Otávio!\n~Teoria~\n**Expressões Idiomáticas (Idioms):**\nO termo \"in its own right\" significa literal e abstratamente \"por si só\" ou \"por conta própria\". No texto: \"the volume of alerts can become a problem in its own right\" = o próprio excesso brutal purista nativo de avisos vira a doença principal contínua da repartição.\n\n~Gabarito~\n**D) is a problem in itself, distinct from the irregularities the models try to detect.**\n**> CERTO <**\n(É um problema por si mesmo, distinto das irregularidades base). A montanha de alarmes se desprende da fraude e passa a ser, ela mesma (in its own right), um gargalo catastrófico isolado exato formal contínuo limítrofe no colo do fiscal.\n\n~Gentalha~\n**A) results from invoices cancelled...**\n**> ERRADO <**\nAtribui causa estrita a apenas uma fraude limpa original isolada; contudo a expressão refere-se ao volume de barulho sonoro geral nativo.\n\n**B) solves the problem of audit teams...**\n**> ERRADO <**\nIsso agrava e destrói (overwhelms) os times, e não resolve absolutamente nada no chão fabril bruto da agência orgânica.\n\n**C) matters less than the patterns...**\n**> ERRADO <**\n(Importa menos). A expressão idiomatizada dá peso autoral limítrofe e grandeza bruta ao assunto, igualando o peso do barulho à fraude e não o inferiorizando no pátio contábil.\n\n**E) belongs to the audit teams...**\n**> ERRADO <**\nTenta forçar uma tradução literal esdrúxula cega formal boba rasteira de \"right\" como posse de direitos estrita autorizada legal limítrofe amarrada (Pertencer).\n\n!Regra de Bolso!\n~Lógica~\n**1) SE** vir a expressão estrita fina amarrada c(in its own right), **ENTÃO** saiba que ela afasta a hierarquia secundária formal e grita que o objeto ganha peso c(por seu próprio mérito / por si próprio) no enquadramento purista abstrato unificado original.\n\n!Interpretando a Banca!\n~Gatilho~\nA banca adora essas locuções. \"Own right\" pega pela ideia de direito jurídico de posse (belong) em tradução literal de aluno sem base, o que fataliza a questão de quem acha que inglês é verbo to be."
    },
    {
      "type": "normal",
      "id": "ti_ce6_q179",
      "subject": "Inglês Técnico - Compreensão V/F",
      "source": "Banca Águia - Q179",
      "timer_override": 180,
      "front": "**Questão 179:**\n\nCom base no texto, julgue as afirmativas a seguir em verdadeiras (V) ou falsas (F).\n\nA sequência correta, de cima para baixo, é:",
      "stem": [
        "vf(I. Segundo o texto, a nota fiscal eletrônica é transmitida ao fisco antes de a mercadoria sair do depósito.)",
        "vf(II. O texto menciona a divisão de valores em montantes menores para ficar abaixo dos limites que levariam a uma revisão mais detida.)",
        "vf(III. De acordo com o texto, o excesso de alertas leva as equipes de auditoria a escolher os casos quase ao acaso.)",
        "vf(IV. O texto informa que várias administrações passaram a registrar o resultado de cada revisão, para recalibrar os modelos com resultados reais.)"
      ],
      "options": [
        "A) V, V, F, F.",
        "B) F, V, V, F.",
        "C) V, F, V, V.",
        "D) V, V, V, V.",
        "E) V, V, V, F."
      ],
      "answer": 3,
      "back": "Gabarito: D.\n\n!Otávio!\n~Teoria~\n**Análise de Varredura Fina (Scanning):**\nCada afirmação se apoia numa sentença direta, crua e explícita das linhas matrizes espelhadas no parágrafo.\n\n~Gabarito~\n**D) V, V, V, V.**\n\n**I. (V)** \n**> CERTO <**\n\"...transmitted to the tax authority before the goods leave the warehouse...\" = antes da mercadoria sair do armazém/depósito estrito.\n\n**II. (V)** \n**> CERTO <**\n\"...split into small amounts to stay below the thresholds that would trigger a closer review.\" = fragmentados abaixo dos limites que disparam investigação dura fina purista.\n\n**III. (V)** \n**> CERTO <**\n\"...overwhelms the audit teams, who end up choosing cases almost at random.\" = esmaga a equipe, que escolhe casos quase na roleta aleatória russa cega.\n\n**IV. (V)** \n**> CERTO <**\n\"...rank alerts by expected revenue and record the outcome of every review... to feed those outcomes back into the models...\" = guardam os retornos puros pra jogar na matriz calibradora final.\n\n!Regra de Bolso!\n~Lógica~\n**1) SE** a banca pedir tradução crua exata de \"Warehouse\", **ENTÃO** vá seco em Depósito ou Armazém fiscal purista.\n**2) SE** vier \"Almost at random\", **ENTÃO** associe a Aleatoriedade brutal cega sem critério purista lógico limítrofe no texto em inglês.\n\n!Interpretando a Banca!\n~Gatilho~\nÉ o tradicional caça-palavras da FGV/CEBRASPE. Traduzir as palavras centrais (thresholds, warehouse, random) quebra as afirmativas perfeitamente alinhadas."
    },
    {
      "type": "normal",
      "id": "ti_ce6_q180",
      "subject": "Inglês Técnico - Conjunções",
      "source": "Banca Águia - Q180",
      "timer_override": 180,
      "front": "**Questão 180:**\n\nConsider the sentence from a software contract specification: “The contractor shall ensure that service level indicators are measured and reported on a monthly basis, regardless of any change in the underlying infrastructure.” The expression “regardless of” introduces, in relation to the rest of the sentence, an idea of:",
      "stem": [],
      "options": [
        "A) cause, indicating the reason why the contractor must measure and report the service level indicators on a monthly basis throughout the term of the contract.",
        "B) purpose, indicating the objective that the monthly measurement and reporting of the indicators is intended to achieve for the contracting party.",
        "C) concession, indicating that the obligation to measure and report on a monthly basis holds even if the underlying infrastructure is changed.",
        "D) condition, indicating that the obligation to measure and report the indicators applies for as long as the underlying infrastructure remains unchanged.",
        "E) consequence, indicating the result produced by a prior change in the underlying infrastructure of the service that is being contracted."
      ],
      "answer": 2,
      "back": "Gabarito: C.\n\n!Otávio!\n~Teoria~\n**Regardless of (Independentemente de / Concessão):**\nA partícula indica que uma regra impositiva limítrofe permanecerá de pé e implacável bruta amarrada pura isolada mesmo que algo muito adverso no ambiente aconteça ou tente atrapalhá-la (a infraestrutura mudar). Isso é C(Concessão).\n\n~Gabarito~\n**C) concession, indicating that the obligation to measure and report on a monthly basis holds even if the underlying infrastructure is changed.**\n**> CERTO <**\nConcessão (Concession). O contrato não liga para desculpas. Tem que medir mensalmente, mesmo se o servidor queimar e ser substituído pela infraestrutura amanhã. É a oposição a uma possível dificuldade.\n\n~Gentalha~\n**A) cause (Causa)...**\n**> ERRADO <**\nNão é uma causa e efeito do nível de serviço; a infraestrutura não forçou e motivou o fiscal a criar relatórios, o relatório já era uma ordem cravada.\n\n**B) purpose (Objetivo)...**\n**> ERRADO <**\n\"Regardless of\" jamais indica finalidade (in order to, so that).\n\n**D) condition (Condição)...**\n**> ERRADO <**\nA restrição condicional de \"as long as remains unchanged\" aniquila o sentido. A condição de limite derrubaria a ordem, enquanto a concessão original de c(regardless) manda continuar a aferição a qualquer custo.\n\n**E) consequence (Consequência)...**\n**> ERRADO <**\nNão é um resultado produzido cego analítico por força atrelada da máquina nova limítrofe, não encabeça oração consecutiva formal bruta (\"therefore\", \"thus\").\n\n!Regra de Bolso!\n~Lógica~\n**1) SE** você cruzar com *Regardless of*, *Despite* ou *In spite of*, **ENTÃO** você tem implacavelmente e irremediavelmente e eternamente a ideia e aura linguística densa purista cega da c(Concession / Concessão).\n\n!Interpretando a Banca!\n~Gatilho~\nA confusão clássica no inglês formal: achar que \"regardless\" exige condicional de trava dura (\"só faça isso se...\") quando na verdade é um libertador impositivo bruto cravado (\"faça a qualquer custo e dane-se se chover\")."
    },
    {
      "type": "normal",
      "id": "ti_ce6_boss_final",
      "subject": "Auditoria de TI - Chefe Final",
      "source": "Banca Águia - Boss Final",
      "timer_override": 400,
      "front": "**[Chefe Final] - Resenha Geral de Fechamento**\n\n- Otávio: (recolhendo as peças puras do quebra-cabeça na mesa) - Encerrou o turno, estrategista. Valide a chave final do pátio para ir para casa:\n\nA sequência correta, de cima para baixo, é:",
      "stem": [
        "vf(I. A manipulação cega e orgânica de strings limítrofes preserva o esqueleto numérico purista e zeros primários lógicos para cruzar pontes estritas reais analíticas no JOIN robusto entre tabelas orçamentárias nativas contínuas isoladas.)",
        "vf(II. A concessão estrita inglesa purista no documento burocrático (Regardless of) destrói as desculpas condicionais, cobrando o SLA numérico relacional contínuo puro mesmo sob o colapso e troca atrelada isolada analítica cega bruta da base orgânica do hardware contínuo unificado formal.)",
        "vf(III. A fita cassete velha amarrada do contador sequencial bruto contínuo numérico deduz duplicatas e vazios puros lógicos em via algébrica de via única estrita somada, sem diferenciar a fraude limítrofe contínua da omissão do papel.)",
        "vf(IV. A IA de análise solta contínua nativa e geradora viva é prova material contábil estrita atrelada e finaliza implacável e amarrada cega bruta formal brutal no relatório nativo de escore o fim absoluto formal contábil do exame material purista da fraude cravada estrita limítrofe no papel estático.)"
      ],
      "options": [
        "A) V, V, F, F.",
        "B) F, F, V, V.",
        "C) V, F, V, F.",
        "D) V, V, V, V.",
        "E) F, F, F, F."
      ],
      "answer": 0,
      "back": "Gabarito: A.\n\n!Otávio!\n~Teoria~\n**Checagem Final Absoluta:**\nVocê agora lida com SQL e semântica juntos. É o teste do fiscal pleno e inquestionável do imposto.\n\n~Gabarito~\n**A) V, V, F, F.**\n\n**I. (V) STRING/Texto para JOIN:**\n**> CERTO <**\nPreservar CNPJ como String (Texto/Varchar) garante que o zero à esquerda resista e os Joins e chaves conectem o cofre das planilhas puros analíticos puristas locais de forma imaculada atrelada formal.\n\n**II. (V) Regardless of = Concessão/Implacável:**\n**> CERTO <**\nA concessão não perdoa obstáculo. O SLA vai ser medido c(independentemente de) (\"regardless of\") troca de servidor e infraestrutura no colo cego purista analítico purista local atrelado formal amarrado contínuo unificado originário nativo bruto da contratada.\n\n**III. (F) Teste de Sequência em Via Única Subtrativa:**\n**> ERRADO <**\nAs falácias algébricas enganam. Duplicata é repetição, omissão/furo é número ausente. Você nunca mistura a sujeira das lacunas com a poluição extra purista das dobras estritas limítrofes. A numeração ausente crua isolada é obtida deduzindo os números c(únicos originais) atrelados formais vivos orgânicos estritos brutos do escopo total cego abstrato nativo esperado puro analítico lógico amarrado formal limítrofe unificado original.\n\n**IV. (F) IA Pura gera Prova cabal absoluta final:**\n**> ERRADO <**\nA IA ou o Escore atua na ponta limítrofe cega fina de triagem, levantando alarme purista relacional estrito. O laudo vivo nativo autoral final só fecha com a mão material humana relacional abstrata formal limítrofe cega crua orgânica fina da auditoria batendo com a nota em papel real vivo puro no pátio estrito contínuo purista estático cravado numérico.\n\n!Regra de Bolso!\n~Lógica~\n**1) SE** a banca afirmar que a IA, ou escore e modelos analíticos puristas nativos orgânicos assumem responsabilidade final cega e terminativa sobre o julgamento contábil puro amarrado estrito lógico, **ENTÃO** você esmaga a afirmativa. A IA sempre será apenas uma C(Lanterna) apontando para onde o fiscal orgânico deve chutar a porta contínua analítica pura estrita cravada limítrofe local formal.\n\n!Break para Respirar!\n~Otávio~\n- MISSÃO CUMPRIDA, ESTRATEGISTA! O bloco todo caiu. Suas junções batem, seus algoritmos respiram e as falácias da banca inglesa sumiram no vento da sua auditoria. O selo da glória fiscal agora pertence ao seu perfil."
    }
  ]
}

with open("Conhecimentos específicos 6 (FIM).json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
