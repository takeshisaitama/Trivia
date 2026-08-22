import json

data = {
  "title": "Português: Sintaxe e Morfologia (Foco Dataprev)",
  "messages": {
    "reprovado": "Otávio: ((Com olhar analítico de auditor)) - Seu desempenho foi sintaticamente inconsistente. Confundir futuro do presente com futuro do pretérito na Dataprev é falha de sistema crítica. Volte para a gramática básica.",
    "reserva": "Otávio: ((Digitando no terminal)) - Seu resultado ficou na média de quem resolve por intuição e cai nas pegadinhas das funções do SE. Está no cadastro de reserva da Dataprev. Precisa de mais rigor linguístico.",
    "call4": "Otávio: ((Ajustando os óculos)) - Desempenho satisfatório. Mostrou que sabe diferenciar pronomes demonstrativos, mas hesitou na sintaxe do adjunto. Passou no limiar da classificação.",
    "call3": "Otávio: ((Sorrindo levemente)) - Muito bom. Sua base morfológica está bem estruturada. Você identificou as partículas corretamente e evitou as armadilhas das bancas.",
    "call2": "Otávio: ((Impressionado)) - Excelente aproveitamento. Você domina a partícula apassivadora e os tempos verbais em sentenças complexas. A nomeação na Dataprev está muito próxima.",
    "call1": "Otávio: ((Entrega um relatório técnico aprovado)) - PROFICIÊNCIA LINGUÍSTICA ABSOLUTA. Você decifrou todas as regras de coesão, sintaxe e morfologia sem cair em nenhuma casca de banana da banca. A vaga de analista é sua. Use a caneta para assinar o termo de posse."
  },
  "cards": [
    {
      "type": "normal",
      "id": "portugues_dataprev_boss_tutorial",
      "subject": "Língua Portuguesa - Teoria Geral",
      "source": "Dataprev - Boss Tutorial de Português",
      "timer_override": 5000,
      "front": "(BOSS TUTORIAL) - Otávio:\n(acessa o mainframe do sistema e aponta para o terminal de logs)\n- Futuro Analista, a linguagem é o código-fonte da comunicação. Um erro de sintaxe aqui não gera apenas um alerta, ele compromete toda a segurança da rede. Para este lote, você precisa dominar as nuances verbais, a precisão dos pronomes e a anatomia das orações. Memorize este protocolo linguístico antes de inspecionar os pacotes de dados:",
      "stem": [
        "**1) Tempos Verbais - Futuro do Presente vs Futuro do Pretérito:** \n O Futuro do c(Presente) indica uma ação que com certeza ocorrerá em relação ao momento atual (ex: eles c(correrão)). O Futuro do c(Pretérito) indica uma ação hipotética ou dependente de uma condição (ex: eles c(correriam)). Não confunda a certeza com a hipótese.",
        "**2) Pronomes Demonstrativos - Catafórico vs Anafórico:** \n O pronome c(ISTO) (ou este/esta/nisto) possui função c(catafórica): aponta para algo que c(ainda vai ser dito) no texto (geralmente introduzido por dois-pontos). Já o pronome c(ISSO) (ou esse/essa/nisso) possui função c(anafórica): retoma algo que c(já foi dito).",
        "**3) Sintaxe - Adjunto Adnominal:** \n O adjunto adnominal é o termo satélite que determina, especifica ou caracteriza o c(núcleo de um substantivo). Um adjetivo que qualifica diretamente um objeto dentro de uma oração (ex: coleira c(invisível)) exerce obrigatoriamente essa função.",
        "**4) Funções da partícula SE - Partícula Apassivadora (PA):** \n Quando associada a um Verbo Transitivo c(Direto) (VTD), a partícula \"se\" funciona como apassivadora. O sujeito da oração é o elemento paciente e o verbo c(deve concordar) com ele em número (ex: c(Vendem-se) casas / processam-se dados).",
        "**5) Funções da partícula SE - Índice de Indeterminação do Sujeito (IIS):** \n Quando associada a Verbos Transitivos c(Indiretos) (VTI), Intransitivos (VI) ou de Ligação (VL), a partícula \"se\" funciona como IIS. O sujeito é indeterminado e o verbo fica c(obrigatoriamente no singular) (ex: c(Precisa-se) de peritos).",
        "**6) Funções da partícula QUE - Pronome Relativo:** \n Ocorre quando o \"que\" retoma um c(substantivo) imediatamente anterior. A prova real para confirmar é substituí-lo por c(o qual, a qual, os quais, as quais).",
        "**7) Funções da partícula QUE - Conjunção Integrante:** \n Ocorre quando o \"que\" introduz uma oração subordinada substantiva (completando o sentido de um verbo ou nome). A prova real é substituir toda a oração introduzida pelo \"que\" pela palavra c(ISSO) (ex: É necessário c(que você estude) -> É necessário c(ISSO))."
      ],
      "options": [
        "A) Protocolo recebido, Otávio. Meu sistema sintático está calibrado e pronto para a triagem de dados."
      ],
      "answer": 0,
      "back": "Gabarito: A\n\n!Otávio!\n~Teoria~\nAs regras acima são as bases para a triagem de qualquer texto institucional. Dominar a regência, a função do \"que\" e do \"se\", assim como o tempo verbal exato, garante que nenhum laudo pericial contenha ambiguidades lógicas.\n\n!Regra de Bolso!\n~Lógica~\n**SE** for algo que ainda vai ser apresentado, **ENTÃO** use c(ISTO / ESTE).\n**SE** o verbo é VTD + SE, **ENTÃO** tem Sujeito Paciente e c(concorda) com ele.\n**SE** o \"que\" pode ser trocado por c(O QUAL), **ENTÃO** é pronome relativo.\n\n!Break para Respirar!\n~Otávio~\n- Respire fundo, perito. A gramática é um banco de dados estruturado. Apenas aplique as querys corretas."
    },
    {
      "type": "normal",
      "id": "portugues_dataprev_modo_leitura",
      "subject": "Língua Portuguesa - Leitura",
      "source": "Dataprev - Simulação de Evidência",
      "timer_override": 300,
      "front": "Leia atentamente o relatório pericial abaixo para responder às questões a seguir:\n\n**Relatório de Incidentes - Dataprev**\n\nA tecnologia, c(que) prometeu liberdade, forjou uma coleira c(invisível) de vigilância. O tempo agora c(corre) em outra velocidade e nós percebemos a complexidade da rede. O fato é c(que) a solução reside c(nisto): a criptografia avançada.\nAtualmente, processam-c(se) milhares de dados sigilosos por segundo nos nossos servidores. Portanto, precisa-c(se) de novos peritos para garantir a integridade absoluta da infraestrutura.",
      "options": [
        "A) Ciente. Modo de leitura concluído."
      ],
      "answer": 0,
      "back": "Gabarito: A\n\n!Otávio!\n- Leitura biométrica concluída. Avance para a análise gramatical dos fragmentos."
    },
    {
      "type": "normal",
      "id": "portugues_dataprev_q01",
      "subject": "Língua Portuguesa - Tempos Verbais",
      "source": "Dataprev - Análise de Logs",
      "timer_override": 180,
      "front": "Questão 01:\n\nAnalise o tempo e modo verbal do trecho sublinhado: **\"O tempo agora c(corre) em outra velocidade\"**.\n\nAssinale a alternativa c(correta) em relação às flexões verbais deste verbo, prestando atenção à diferença temporal abordada por Otávio no tutorial.",
      "options": [
        "A) O verbo está no presente do indicativo. Se fosse flexionado no futuro do pretérito, a forma correta seria \"correrá\".",
        "B) O verbo está no presente do subjuntivo. Sua flexão no futuro do presente seria \"correria\".",
        "C) O verbo está no presente do indicativo. Sua flexão no futuro do presente seria \"correrá\" e no futuro do pretérito seria \"correria\".",
        "D) A forma verbal no plural para o futuro do presente é \"correriam\".",
        "E) Trata-se de um verbo no pretérito imperfeito, cuja forma no futuro do presente é \"corria\"."
      ],
      "answer": 2,
      "back": "Gabarito: C\n\n!Otávio!\n~Teoria~\nTempos do Modo Indicativo:\nO verbo \"correr\" na forma \"corre\" encontra-se no c(Presente do Indicativo) (ação habitual ou atual). O c(Futuro do Presente) descreve um fato que acontecerá com certeza (ele correrá / eles correrão). Já o c(Futuro do Pretérito) descreve algo hipotético ou que dependia de uma condição passada (ele correria / eles correriam).\n\n~Gabarito~\n**C) O verbo está no presente do indicativo. Sua flexão no futuro do presente seria \"correrá\" e no futuro do pretérito seria \"correria\".**\n**CORRETA:** Esta é a descrição morfológica exata do verbo na 3ª pessoa do singular.\n\n~Gentalha~\n**A) O verbo está no presente do indicativo. Se fosse flexionado no futuro do pretérito, a forma correta seria \"correrá\".**\n**ERRADA:** \"Correrá\" é futuro do presente. Futuro do pretérito é \"correria\".\n\n**D) A forma verbal no plural para o futuro do presente é \"correriam\".**\n**ERRADA:** \"Correriam\" (terminação em -iam) é futuro do pretérito do plural. Futuro do presente seria \"correrão\".\n\n!Regra de Bolso!\n~Lógica~\n**SE** houver certeza e projeção futura, **ENTÃO** use c(-RÁ / -RÃO) (Futuro do Presente).\n**SE** houver hipótese/condição, **ENTÃO** use c(-RIA / -RIAM) (Futuro do Pretérito).\n\n!Interpretando a Banca!\n~Gatilho~\nA banca adora tentar te confundir no plural (correrão vs correriam). Fique atento à terminação final da palavra para identificar o tempo e modo.\n\n!Break para Respirar!\n~Otávio~\n- O tempo corre, mas você tem o controle. A primeira análise foi bem sucedida."
    },
    {
      "type": "normal",
      "id": "portugues_dataprev_q02",
      "subject": "Língua Portuguesa - Pronomes e Pontuação",
      "source": "Dataprev - Análise de Logs",
      "timer_override": 180,
      "front": "Questão 02:\n\nObserve o trecho retirado do relatório pericial:\n**\"O fato é que a solução reside c(nisto): a criptografia avançada.\"**\n\nAssinale a alternativa c(correta) sobre o elemento coesivo em destaque e a pontuação empregada.",
      "options": [
        "A) O pronome \"nisto\" exerce função anafórica, pois retoma a ideia expressa na oração anterior.",
        "B) O uso de \"nisto\" está incorreto, pois para introduzir uma explicação logo a seguir, a norma padrão exige o uso de \"nisso\".",
        "C) O pronome \"nisto\" possui função catafórica, antecipando uma explicação que é adequadamente introduzida pelos dois-pontos.",
        "D) Os dois-pontos poderiam ser substituídos por ponto final sem qualquer alteração na estrutura sintática ou no sentido coesivo da frase.",
        "E) O pronome \"nisto\" funciona como pronome relativo e poderia ser substituído por \"na qual\" sem erro gramatical."
      ],
      "answer": 2,
      "back": "Gabarito: C\n\n!Otávio!\n~Teoria~\nPronomes Demonstrativos (Coesão Catafórica vs Anafórica):\nOs pronomes demonstrativos iniciados com 'T' (isTo, esTe, esTa, nisTo) possuem função c(catafórica), ou seja, servem para antecipar um termo que c(ainda será mencionado) no texto. É extremamente comum virem acompanhados de dois-pontos, pois os dois-pontos introduzem a explicação prometida pelo pronome.\n\n~Gabarito~\n**C) O pronome \"nisto\" possui função catafórica, antecipando uma explicação que é adequadamente introduzida pelos dois-pontos.**\n**CORRETA:** O elemento \"nisto\" aponta para frente (catáfora), antecipando a expressão \"a criptografia avançada\" apresentada após os dois-pontos.\n\n~Gentalha~\n**A) O pronome \"nisto\" exerce função anafórica...**\n**ERRADA:** Função anafórica é exercida pelos pronomes com 'SS' (isso, esse, nisso), que retomam termos já ditos.\n\n**B) ... a norma padrão exige o uso de \"nisso\".**\n**ERRADA:** O uso de \"nisto\" está perfeitamente correto para introduzir o que vem a seguir.\n\n!Regra de Bolso!\n~Lógica~\n**SE** o termo aponta para frente (apresentando algo), **ENTÃO** use c(ISTO) e função c(Catafórica).\n**SE** o termo aponta para trás (retomando algo), **ENTÃO** use c(ISSO) e função c(Anafórica).\n\n!Interpretando a Banca!\n~Gatilho~\nA associação entre pronome catafórico e o sinal de dois-pontos (:) é clássica. A banca testa se você sabe justificar gramaticalmente o motivo da pontuação.\n\n!Break para Respirar!\n~Otávio~\n- Excelente. Você previu o movimento antes mesmo de a banca atacar. Continue assim."
    },
    {
      "type": "normal",
      "id": "portugues_dataprev_q03",
      "subject": "Língua Portuguesa - Sintaxe",
      "source": "Dataprev - Análise de Logs",
      "timer_override": 180,
      "front": "Questão 03:\n\nNo trecho **\"...forjou uma coleira c(invisível) de vigilância.\"**, assinale a alternativa c(correta) sobre a função sintática do termo em destaque: **invisível**.",
      "options": [
        "A) Exerce a função de adjunto adnominal, pois é um adjetivo que modifica e caracteriza diretamente o núcleo do substantivo concreto \"coleira\".",
        "B) É um predicativo do objeto, pois atribui uma qualidade temporária à coleira por intermédio do verbo \"forjar\".",
        "C) Funciona como complemento nominal, pois completa o sentido abstrato do substantivo \"coleira\".",
        "D) Trata-se de um adjunto adverbial de modo, indicando a maneira como a vigilância age no sistema.",
        "E) Atua como núcleo do objeto direto da oração principal."
      ],
      "answer": 0,
      "back": "Gabarito: A\n\n!Otávio!\n~Teoria~\nAdjunto Adnominal vs Outros Termos Sintáticos:\nO c(Adjunto Adnominal) é o termo que vem junto ao nome (substantivo) para determiná-lo, qualificá-lo ou especificá-lo. Adjetivos, quando atuam diretamente ao lado de um substantivo (sem a intermediação de um verbo de ligação ou sem ser uma característica circunstancial atribuída pelo verbo transitivo), assumem obrigatoriamente essa função.\n\n~Gabarito~\n**A) Exerce a função de adjunto adnominal, pois é um adjetivo que modifica e caracteriza diretamente o núcleo do substantivo concreto \"coleira\".**\n**CORRETA:** O adjetivo \"invisível\" está intrinsecamente ligado ao substantivo \"coleira\", qualificando-o de forma permanente no contexto da frase. Ele faz parte do bloco sintático do objeto direto (uma coleira invisível de vigilância).\n\n~Gentalha~\n**B) É um predicativo do objeto...**\n**ERRADA:** O predicativo do objeto expressaria uma característica temporária ou resultante de uma ação do sujeito sobre o objeto (ex: \"Achei a coleira invisível\"), o que não ocorre aqui. \n\n**C) Funciona como complemento nominal...**\n**ERRADA:** Complementos nominais são introduzidos por preposição e completam substantivos abstratos, adjetivos ou advérbios. \"Invisível\" é o próprio adjetivo.\n\n!Regra de Bolso!\n~Lógica~\n**SE** o adjetivo qualifica diretamente o substantivo estando ao seu lado no bloco sintático, **ENTÃO** sua função é de c(Adjunto Adnominal).\n\n!Break para Respirar!\n~Otávio~\n- Análise sintática impecável. Nenhum adjetivo passou despercebido pelos seus filtros."
    },
    {
      "type": "normal",
      "id": "portugues_dataprev_q04",
      "subject": "Língua Portuguesa - Morfologia das Partículas",
      "source": "Dataprev - Análise de Logs",
      "timer_override": 300,
      "front": "Questão 04:\n\nConsidere as estruturas retiradas dos logs do sistema:\n1. \"A tecnologia, c(que) prometeu liberdade...\"\n2. \"O fato é c(que) a solução reside...\"\n3. \"Atualmente, processam-c(se) milhares de dados...\"\n4. \"Portanto, precisa-c(se) de novos peritos...\"\n\nSobre a classificação morfológica e sintática das partículas 'que' e 'se' destacadas, assinale a alternativa c(correta).",
      "options": [
        "A) Em 1 e 2, o \"que\" funciona unicamente como conjunção integrante, introduzindo orações subordinadas substantivas.",
        "B) Em 3, o \"se\" atua como índice de indeterminação do sujeito, tornando o verbo invariável (sempre na terceira pessoa do plural).",
        "C) Em 1, o \"que\" é pronome relativo. Em 4, o \"se\" é partícula apassivadora que faz o verbo concordar com \"novos peritos\".",
        "D) Em 2, o \"que\" é pronome relativo, podendo ser substituído por 'no qual'. Em 3, o \"se\" atua como pronome reflexivo.",
        "E) Em 1, o \"que\" atua como pronome relativo (a qual). Em 3, o \"se\" é partícula apassivadora, fazendo o verbo concordar no plural com o sujeito paciente \"milhares de dados\"."
      ],
      "answer": 4,
      "back": "Gabarito: E\n\n!Otávio!\n~Teoria~\nFunções do QUE e do SE:\nO c(QUE) é pronome relativo quando retoma um substantivo anterior (A tecnologia, *a qual*...). É conjunção integrante quando se pode trocar a oração toda por ISSO (O fato é *ISSO*).\nO c(SE) é Partícula Apassivadora (PA) quando ligado a Verbo Transitivo Direto (VTD). O termo sem preposição vira o sujeito e o verbo c(deve concordar) com ele (processam-se dados -> dados são processados). É Índice de Indeterminação do Sujeito (IIS) com VTI (precisar de), e o verbo fica c(no singular) (precisa-se).\n\n~Gabarito~\n**E) Em 1, o \"que\" atua como pronome relativo (a qual). Em 3, o \"se\" é partícula apassivadora, fazendo o verbo concordar no plural com o sujeito paciente \"milhares de dados\".**\n**CORRETA:** A análise descreve com exatidão as regras gramaticais. Em 1, substitui-se por 'a qual'. Em 3, \"processar\" é VTD, logo \"se\" é PA, e o sujeito \"milhares de dados\" (plural) exige o verbo no plural \"processam\".\n\n~Gentalha~\n**A) Em 1 e 2, o \"que\" funciona unicamente como conjunção integrante...**\n**ERRADA:** Em 1, o \"que\" é pronome relativo.\n\n**B) Em 3, o \"se\" atua como índice de indeterminação...**\n**ERRADA:** Processar é VTD, exigindo partícula apassivadora, que possibilita o sujeito plural.\n\n**C) ... Em 4, o \"se\" é partícula apassivadora.**\n**ERRADA:** \"Precisar\" exige preposição \"de\" (VTI). Logo, o \"se\" na frase 4 é Índice de Indeterminação do Sujeito.\n\n!Regra de Bolso!\n~Lógica~\n**SE** VTD + SE, **ENTÃO** é c(Partícula Apassivadora) (Concorda com o sujeito: vendem-se casas).\n**SE** VTI + SE, **ENTÃO** é c(Índice de Indeterminação) (Verbo no singular: precisa-se de peritos).\n**SE** QUE puder virar O QUAL, **ENTÃO** é c(Pronome Relativo).\n\n!Break para Respirar!\n~Otávio~\n- Esse foi o teste definitivo da sua inteligência linguística. Superar as funções das partículas separa o amador do perito criminal."
    },
    {
      "type": "normal",
      "id": "portugues_dataprev_boss_inter_01",
      "subject": "Língua Portuguesa - Revisão Final",
      "source": "Dataprev - Boss Final",
      "timer_override": 600,
      "front": "Revisão Geral e Veredito:\n\nJulgue as afirmações sobre as regras de sintaxe e morfologia analisadas durante a auditoria:",
      "stem": [
        "vf(I. Na flexão do verbo 'correr', 'correrão' corresponde ao futuro do presente, indicando certeza, enquanto 'correriam' indica o futuro do pretérito, denotando hipótese.)",
        "vf(II. O pronome 'isto' ou 'nisto' exerce função catafórica, devendo ser utilizado para apresentar algo que ainda será mencionado.)",
        "vf(III. Em 'coleira invisível', o termo 'invisível' atua como adjunto adnominal, pois é um adjetivo que determina diretamente o substantivo ao qual está associado na frase.)",
        "vf(IV. Na estrutura 'precisa-se de peritos', a presença da preposição torna o verbo transitivo indireto, logo o 'se' é um índice de indeterminação do sujeito e o verbo permanece no singular.)"
      ],
      "options": [
        "A) I e III são verdadeiras.",
        "B) Apenas II e IV são verdadeiras.",
        "C) I, II, III e IV são verdadeiras.",
        "D) Apenas I é verdadeira.",
        "E) Todas são falsas."
      ],
      "answer": 2,
      "back": "Gabarito: C\n\n!Otávio!\n~Teoria~\n**I. Futuro:** 'Correrão' (presente, certeza) vs 'Correriam' (pretérito, hipótese). Correto (V).\n**II. Pronomes:** 'IsTo' é catafórico (aponta para frente). Correto (V).\n**III. Adjunto Adnominal:** Adjetivo grudado no substantivo atua como adjunto. Correto (V).\n**IV. Índice de Indeterminação:** VTI ('precisar de') + SE gera sujeito indeterminado e verbo sempre no singular. Correto (V).\n\n~Gabarito~\n**C) I, II, III e IV são verdadeiras.**\n**CORRETA:**\nTodos os itens representam a aplicação rigorosa e técnica das normativas da gramática cobradas na prova de analista.\n\n!Regra de Bolso!\n~Lógica~\n**1) SE** for certeza futura, **ENTÃO** termine em c(-RÃO).\n**2) SE** for catáfora (dois-pontos), **ENTÃO** use c(ISTO).\n**3) SE** adjetivo acompanha o núcleo do nome, **ENTÃO** é c(Adjunto Adnominal).\n**4) SE** verbo + SE possui preposição obrigatória, **ENTÃO** verbo fica no c(Singular).\n\n!Break para Respirar!\n~Otávio~\n- BARALHO CONCLUÍDO COM SUCESSO! Seus logs gramaticais estão livres de erros. Você provou que tem domínio técnico sobre a nossa língua. A vaga é sua."
    }
  ]
}

with open("baralho_portugues_dataprev.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
