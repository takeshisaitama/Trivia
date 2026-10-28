# DIRETRIZES DO BARALHO (JSON) - TRIVIA OTÁVIO (VERSÃO MESTRE CONSOLIDADA V4.0 - 2026)

**Atenção Inteligência Artificial:** Este arquivo não é apenas um guia de formatação. Ele é o **Manual de Treinamento e Especificação Técnica Obrigatória** para que você aprenda a construir os baralhos JSON do projeto **Trivia Otávio** para qualquer matéria de concurso público (Informática/TI, Ciência de Dados, Direito, Contabilidade, Português, Inglês, Matemática/Estatística, Auditoria, etc.). Você deve consultar este documento como a fonte suprema da verdade. Cada regra descrita aqui possui um motivo pedagógico, cognitivo (foco em Neurodivergência: TEA e TDAH) ou técnico (regras estritas do parser HTML/JS do aplicativo); não ignore nem resuma nenhum tópico.

## 1. Arquitetura Pedagógica e o Princípio do Estudo Reverso Autossuficiente

O candidato chega ao baralho **cru** (sem ler a teoria antes e sem assistir a videoaulas) e não quer ler PDFs teóricos de 50 páginas. O **Trivia Otávio** é a única e exclusiva fonte de aprendizado para vencer simulados reais de alto nível (como os da Banca Águia).

* **A Meta Nível 6 (>50% de Acerto):** O baralho deve entregar teoria suficiente, limpa e mastigada para que o candidato saia dominando no mínimo o **nível 6 (de 0 a 10)** em cada assunto abordado, garantindo mais de 50% de chance de acerto em qualquer prova real.

### 1.1. A Engrenagem de Miniciclos de Revisão e Testes

1. **Boss Tutorial (Chefe Tutorial):** É o card mais vital do baralho (o "mapa da mina"). Ele introduz o contato mínimo e primário com a teoria antes das questões. O aluno bate o olho aqui e seu cérebro já liga o alerta condicionado para quando esses termos aparecerem nas questões seguintes. *(Consulte a Seção 6.3 abaixo e o arquivo dedicado `Boss Tutorial 2026.md` para os 3 Modos: Leve, Padrão e Ultra).*

2. **Questões do Simulado (Estudo Reverso):** As questões ensinam através do teste prático e da análise do erro, reproduzindo fielmente o simulado original.

3. **Verso (`~Teoria~`), Chefes Intermediários e Chefes Finais:** Formam **miniciclos de revisão e miniciclos de teste** dentro da mesma sessão (já que a regra é fazer o baralho inteiro no mesmo dia). O conceito é apresentado no Boss Tutorial, aprofundado no verso da questão onde cai, testado no Chefe Intermediário após 3 a 4 questões e consolidado no Chefe Final.

### 1.2. Hierarquia de Tags no Verso (O Mapeamento Ocular do Candidato)

O verso (`back`) deve obrigatoriamente seguir esta ordem imutável de tags e subtags, pois reflete exatamente a sequência da "sede de olhar" do candidato:

1. **`!Otávio!` -> `~Teoria~` (1º lugar absoluto):** É o primeiro lugar para onde o olho vai quando o aluno não sabe a questão, erra ou acerta com dúvida. A `~Teoria~` deve funcionar como a explicação de um professor na lousa que já resolve a dúvida de 9 em cada 10 alunos da sala antes mesmo de lerem o gabarito.

2. **`~Gabarito~` (2º lugar):** Lido logo em seguida por quem errou ou quer confirmar o passo a passo do acerto.

3. **`~Gentalha~` (3º lugar):** Consulta pontual. Quem acerta geralmente não lê todas as erradas — lê apenas a alternativa específica que o deixou em dúvida.

4. **`!Regra de Bolso!` -> `~Lógica~` (4º lugar):** Local de fixação rápida dos conceitos-chave usando regras condicionais curtas (`SE ... ENTÃO ...`), onde cada item representa uma única decisão ou operação mental independente.

5. **`!Interpretando a Banca!` -> `~Gatilho~` e `!Break para Respirar!` -> `~Otávio~` (5º lugar):** Fechamento com a malícia da banca examinadora e o respiro estratégico/macetes de memorização do Otávio.

## 2. Adaptação Rigorosa para Neurodivergência (TDAH e TEA) e Clareza de Linguagem

O aluno tem **TDAH e Autismo (TEA)**. Explicações labirínticas, truncadas ou cheias de palavras difíceis exigem 2 ou 3 leituras da mesma frase, gerando exaustão mental imediata e desmotivação ("custo cognitivo alto"). O texto deve ter **custo de aprendizado zero na primeira leitura**.

### 2.1. Simplicidade Extrema, Literalidade e Banimento da "Sopa de Adjetivos"

* **PROIBIDO ("Sopa de Adjetivos" e Jargões Empilhados):** É estritamente proibido empilhar adjetivos desconexos ou floreios robóticos (ex: NUNCA escreva *"fita biológica contígua fotográfica estrita original ativa limítrofe amarrada"*).

* **Fórmula de Redação:** Use **Sujeito + Verbo + Complemento direto**, como um colega inteligente explicando a matéria de forma simples e motivadora.

* **Tradução Imediata de Termos Técnicos e Siglas ("Lacuna Zero" — Presunção Zero de Conhecimento Prévio):**

  * Nunca jogue um termo técnico, número de camada ou jargão sem traduzi-lo imediatamente entre parênteses em linguagem humana (ex: `Camada 4 (Camada de Transporte da pilha de protocolos TCP/IP)`, `registros esparsos (pontos isolados, longe da maioria)`, `volume denso / core (região com muitos pontos juntos)`).

  * **Regra das Siglas Obrigatórias e Exceção no Limite de Palavras:** Sempre que citar uma sigla técnica na primeira ocorrência (ex: `ML — Machine Learning (aprendizado de máquina)`, `SQL — Structured Query Language (linguagem de consulta estruturada)`, `ITF — Integrated Test Facility (Instalação de Teste Integrado)`, `CAATs — técnicas de auditoria assistidas por computador`), expanda a sigla e traduza seu sentido para o português. Termos técnicos que um iniciante não domina (*concessão*, *agregação*, *produção*, *entidade fictícia*, *teste de gaps/lacunas*) devem ser brevemente esclarecidos em linguagem literal, evitando metáforas ambíguas (*"sistema vivo"*, *"passa um rodo"*, *"conjunto sobrevivente"*). **Exceção explícita de extensão:** o texto usado exclusivamente para expandir siglas e traduções terminológicas obrigatórias não consome a cota de palavras da explicação; porém, explicações comuns, exemplos e esclarecimentos de conceitos contam normalmente no limite de palavras, mesmo quando colocados entre parênteses. Em questões de interpretação de texto e Inglês Técnico, o Boss Tutorial deve ensinar apenas as ferramentas linguísticas (vocabulário, expressões idiomáticas como *in its own right* e conectivos como *however* e *regardless of* com exemplos genéricos), sendo **terminantemente proibido** resumir os parágrafos do texto da prova ou antecipar o gabarito.

  * **Proibição de Abreviações Ambíguas (Ex: `IV`):** Nunca escreva apenas `IV` para *Initialization Vector* (pois o olho humano e o leitor de voz leem `IV` como o algarismo romano `4`); escreva sempre `vetor de inicialização (*nonce*)`.

  * **Exemplos Visuais para Falsos Positivos e Falsos Negativos:** Ao explicar erros de classificação, deixe explícito quem é quem: *Falso Negativo* = é uma fraude real (deveria dar positivo no alarme), mas o robô errou dizendo que era normal (negativo) e deixou o bandido escapar; *Falso Positivo* = é um cidadão inocente (deveria dar negativo), mas o alarme tocou falso dizendo que era fraude (positivo). Use analogias concretas e literais que funcionem para autistas (como a analogia do **cobertor curto** ao mudar o limiar de alerta: cobriu a cabeça diminuindo falsos negativos, descobriu o pé aumentando falsos positivos).

### 2.2. Preenchimento de Lacunas do PDF Original (O "Como" e o "Porquê") e Conceitos Abstratos

Você **nunca pode alterar o gabarito nem contrariar a lógica do professor do PDF**, mas quando o comentário original for vago ou pular etapas mentais, você **DEVE obrigatoriamente complementar** a explicação mostrando o mecanismo concreto de **COMO** e **POR QUE** aquilo funciona na prática:

* *Exemplo no RMSE:* Não diga apenas *"eleva ao quadrado, tira a média e extrai a raiz"*. Explique o **porquê**: quando você eleva um erro pequeno ao quadrado (ex: 1 ao quadrado = 1), ele quase não muda; mas quando eleva um erro grande ao quadrado (ex: 5 ao quadrado = 25), ele explode de tamanho, fazendo com que a nota final do RMSE denuncie e puna severamente os erros grandes.

* *Exemplo no KNN (k = 1 vs. k grande):* Deixe claro para o aluno a dúvida clássica: `k` é o número de vizinhos consultados (não existe `k = 0`, pois com 0 vizinhos não há ninguém para consultar). Com **`k = 1`** (olha só 1 vizinho colado), o modelo decora o ruído e sofre **Sobreajuste (*Overfitting*)**; já com um **`k` exageradamente grande** (ex: `k = 500`), o modelo mistura todo mundo na média geral e sofre **Subajuste (*Underfitting*)**.

* **Fórmula de Evocação para Conceitos Abstratos (Nome -> Pergunta/Função -> Consequência da Falha -> Contraste):**
  Para que o estudante consiga recuperar conceitos abstratos sozinho na hora da prova (e não apenas reconhecê-los ao ler o verso), ensine usando pistas de evocação e consequência prática:

  * *Exemplo (Sondas do Kubernetes):* A sonda de **vivacidade** (*liveness*) pergunta *"Está vivo?"* -> se falhar, c(reinicia o contêiner). A sonda de **prontidão** (*readiness*) pergunta *"Está pronto para trabalhar?"* -> se falhar, c(retira o Pod do balanceamento) sem reiniciar.

  * *Exemplo (Contêiner vs. Máquina Virtual):* O **contêiner** compartilha o c(mesmo núcleo/kernel do hospedeiro); a **máquina virtual** possui um c(kernel próprio) para cada instância.

### 2.3. Matemática, Estatística e Exatas (Nível Iniciante Absoluto / Operação Antes da Conversão)

Para qualquer questão com cálculo (Lei de Benford, Binomial, MAE/RMSE, RAG Chunking, RAID, Vazão TCP, Chaves Criptográficas, Matemática Financeira, Contabilidade, etc.), assuma que o leitor é **100% leigo naquela conta ("explique de um jeito que até um macaco entenderia")**.

* **Hierarquia Didática em Fórmulas (Estrutura/Operação Principal ANTES da Conversão de Unidades):**
  Jamais misture a escolha da operação matemática com a conversão de unidades (ex: multiplicar ou dividir por 8 para converter bytes em bits) na mesma frase inicial! Siga sempre esta ordem mental:

  1. **1º Passo — O que a questão pede e qual é a Operação Principal:** Ensine primeiro a relação principal limpa (ex: *"No TCP, para achar a **Vazão máxima**, dividimos a Janela pelo tempo RTT. Já para achar a **Janela ideal** que ocupa toda a banda, fazemos a operação inversa: multiplicamos a Banda pelo RTT"*).

  2. **2º Passo — Conversão de Unidades (se houver):** Em linha separada, mostre a conversão necessária (ex: *"Como a janela vem em Bytes e a banda vem em bits, lembre que 1 Byte = 8 bits: multiplique os Bytes por 8 antes de dividir"*).

  3. **3º Passo — Substituição Passo a Passo (`\n`) e Alerta do Erro Provável:** Mostre a conta linha por linha usando rótulos `**Passo 1 — ...:**`, `**Passo 2 — ...:**` e aponte explicitamente qual etapa o candidato costuma esquecer (ex: no *chunking* do RAG, lembrar de separar e contar o **1º bloco inteiro** antes de dividir o restante pelo avanço `L - S`).

### 2.4. Metodologia Obrigatória "Identificando os Sujeitos" (Para Conceito-Pai com Conceitos-Filhos ou Siglas Parecidas)

Sempre que uma questão ou card envolver um **Conceito-Pai / Tema Guarda-Chuva** do qual derivam vários conceitos relacionados, famílias de siglas parecidas ou múltiplos agentes interagindo (ex: *Vulnerabilidades Web: SQLi, XSS, CSRF e SSRF*; *Cifração Envelopada: DEK e KEK*; *Sondas: Liveness e Readiness*; *Registros DNS: A, AAAA e MX*; *Modalidades de Lançamento Tributário*; *Espécies de Atos Administrativos*), é **OBRIGATÓRIO** aplicar a metodologia **Identificando os Sujeitos** no verso do card (`~Teoria~`, `~Gentalha~` e `~Lógica~`):

1. **Etapa 1 — Apresentar o Conceito-Pai (Guarda-Chuva) em 1 linha:** Explique qual é a categoria geral antes de falar das siglas (cuidando da precisão conceitual: não diga que *CSRF* deriva de *XSS*, e sim que ambos são ataques distintos dentro da família de *Segurança de Aplicações Web*).

2. **Etapa 2 — Identificar cada Sujeito ("Dar Nome aos Bois" e Isolar o Alvo):** Trate cada conceito ou sigla como um personagem com papel próprio em item separado, respondendo:

   * **Quem é ele?** (Sigla + tradução clara entre parênteses).

   * **Quem ele manipula ou ataca?** (Qual é o **alvo/intermediário exato**: é o `__navegador do usuário__`? É o `__próprio servidor interno__`? É a `__chave pequena DEK__` ou o `__arquivo pesado__`?).

   * **O que ele faz?** (Ação característica em linguagem direta).

3. **Etapa 3 — Contrastar os Sujeitos Rivalizando os Alvos (`__Alvo A__` vs. `__Alvo B__`):** Explicite a diferença em 1 frase curta usando sublinhado duplo (ex: *"O **CSRF** manipula o **navegador da vítima logada** para enviar uma requisição; já o **SSRF** manipula o **próprio servidor** para que ele faça uma requisição interna"*).

4. **Etapa 4 — Conectar a Defesa/Especialidade Logicamente ao Sujeito:** Só apresente a defesa ou regra técnica **depois** de separar os sujeitos, amarrando a defesa ao alvo (ex: se o *CSRF* usa o navegador que envia cookies sozinho, a defesa exige `c(token anti-CSRF no corpo ou cabeçalho)`; se o *SSRF* parte de dentro do servidor, fechar portas de entrada no firewall não resolve — exige `c(lista de destinos permitidos)` na saída do servidor).

5. **Etapa 5 — Consolidar 1-para-1 na `!Regra de Bolso!` (`~Lógica~`):** Crie 1 item `SE ... ENTÃO ...` separado para cada sujeito. *(Consulte o guia complementar `Metodologia_Identificando_os_Sujeitos.md` para exemplos completos).*

## 3. Regras Críticas de Sintaxe JSON, Diagramação no Olho e Caracteres Reservados (ANTI-BUG DE TELA)

O aplicativo HTML do Trivia Otávio possui um parser próprio que converte símbolos específicos em elementos visuais. **Usar esses símbolos fora das tags permitidas QUEBRA O LAYOUT DO CARD NA TELA!**

### 3.1. Os 4 Caracteres Reservados (REGRAS DE FERRO)

1. **Ponto de Exclamação (`!`) — EXCLUSIVO PARA TAGS PRIMÁRIAS:**

   * O caractere `!` é reservado **estritamente** para abrir e fechar as 4 Tags Primárias do verso: `!Otávio!`, `!Regra de Bolso!`, `!Interpretando a Banca!` e `!Break para Respirar!`.

   * **PROIBIDO** usar `!` no final de frases empolgantes (use ponto final `.`), na frente do card ou em fatorial matemático (escreva `FAT(5)`).

2. **Til (`~`) — EXCLUSIVO PARA SUBTAGS DO VERSO (PROIBIDO USAR PARA "APROXIMADAMENTE"):**

   * **ATENÇÃO CRÍTICA:** No parser do Trivia Otávio, tudo que fica entre dois tils (`~texto~`) é transformado em um **Título de Subtag com quebra de linha** (como `~Teoria~`, `~Gabarito~`, `~Gentalha~`, `~Lógica~`, `~Gatilho~`, `~Otávio~`, `~Aprofundamento Gold~`, `~Aprofundamento Ultra~`).

   * Se você usar o símbolo `~` duas vezes no mesmo parágrafo para dizer "aproximadamente" (por exemplo: `log(2) ~ 30,1% e log(3) ~ 47,7%`), o aplicativo acha que o trecho entre os dois `~` é uma Subtag e **rasga o parágrafo no meio com letras gigantes!**

   * **REGRA OBRIGATÓRIA:** **JAMAIS use o caractere `~` dentro do texto explicativo ou nas fórmulas!** Para indicar valor aproximado, use sempre o símbolo **`≈`** (ex: `log(2) ≈ 0,301` ou `≈ 30,1%`) ou escreva `aprox. 30,1%`.

3. **Sublinhado Duplo (`__`) — EXCLUSIVO PARA PARES RIVAIS (PROIBIDO USAR EM CÓDIGO PYTHON COMO `__saldo` ou `__init__`):**

   * **ATENÇÃO CRÍTICA:** No parser do Trivia Otávio, dois sublinhados seguidos (`__texto__`) ativam a tag de **Sublinhado Visual (`<u>texto</u>`)**.

   * Se você escrever dois atributos Python com duplo sublinhado no mesmo parágrafo (por exemplo: `o atributo __saldo vira _Conta__saldo`), o aplicativo interpreta tudo que está entre o primeiro `__` e o segundo `__` como um grande texto sublinhado, **sublinhando frases inteiras por acidente e gerando poluição visual grave!**

   * **REGRA OBRIGATÓRIA:**

     * Só use `__palavra1__ vs. __palavra2__` dentro do texto explicativo (nunca nos títulos dos itens!) quando quiser sublinhar intencionalmente dois conceitos rivais/antagônicos que cumprem papéis opostos e não podem ser confundidos (ex: `__TCP__` vs. `__UDP__`; `__lotes__` vs. `__época__`; `__Vazão__` vs. `__Janela Ideal__`; `__Horizontal__` vs. `__Vertical__`; `__sessão__` vs. `__seção__`).

     * **NUNCA escreva dois `_` colados (`__`) para representar nomes de variáveis ou métodos Python!** Quando precisar explicar *Name Mangling* ou métodos especiais do Python, escreva por extenso (`duplo sublinhado saldo`) ou separe com espaço/símbolo seguro que não acione o parser (ex: `duplo underscore (*_ _saldo*)` -> `*_Conta_ _saldo*`).

4. **Crases / Backticks (`` ` ``), LaTeX (`$`, `\times`) e Aspas Simples (`'`) — BANIDOS:**

   * O uso de crases/backticks (`` ` `` ou ```` ``` ````), tabelas Markdown (`| col |`) e comandos LaTeX (`$`, `\times`, `\frac`) é **100% proibido** em todo o JSON.

   * **Proibição de Aspas Simples para Destaque:** NUNCA use aspas simples (`'groupby'`) para destacar comandos ou termos técnicos; use obrigatoriamente **itálico** (`*groupby*`) ou roxo (`c(groupby)`).

   * **Símbolos Matemáticos Padrão:** Para multiplicação, use obrigatoriamente a estrela **`⋆`** (ex: `4 ⋆ 0,1 ⋆ 0,9^3`) ou escreva *"vezes"*; para potência, use `^` (ex: `2^20`); para divisão, use `/`. Use colchetes `[...]` quando necessário para deixar a ordem da conta 100% inequívoca (ex: `*[N ⋆ (N - 1)] / 2*`).

### 3.2. Sintaxe JSON Legível no Olho (`\n` Espaçado, `**` Colados e Quebra de Parágrafos)

Como o próprio usuário inspeciona e edita o código-fonte JSON diretamente no editor de texto, é **OBRIGATÓRIO** formatar todas as strings JSON seguindo estas regras:

1. **Colagem Estrita dos Asteriscos de Negrito (`**`):** Os dois asteriscos de abertura ficam **colados** no primeiro caractere do trecho em negrito, e os dois asteriscos de fechamento ficam **colados** no último caractere (como os dois-pontos `:`).

2. **Isolamento Visual do `\n` com Espaços (`\n` e `\n\n`):** Sempre coloque **um espaço antes do `\n` e um espaço depois do `\n`** (`\n`). Nunca deixe o `\n` grudado nas palavras (como `):**\nO`), pois isso impede de enxergar as quebras de linha no olho sem usar `Ctrl + F`.

   * *Exemplo Padrão Ouro no JSON:*
     `"**40) Criptografia: AES vs. RSA e Resumo SHA-256 (Q169):** \n O __AES__ (simétrico) é super veloz e serve para c(cifrar arquivos grandes); já o __RSA__ (assimétrico) é pesado e lento, servindo apenas para c(proteger a troca da chave do AES). \n E lembre: o __SHA-256__ é apenas um resumo (*hash*) que confere a c(integridade), mas c(não esconde o conteúdo) do arquivo."`

3. **Quebra de Linha ao Final de Cada Parágrafo (`\n`) e Evitar Ponto e Vírgula (`;`):**

   * Sempre que terminar um parágrafo ou uma ideia completa dentro de uma explicação e for iniciar uma observação complementar (ex: *"E lembre: ..."*, *"Com eles, o auditor pode..."*), pule uma linha com `\n`.

   * Nos textos de nossa autoria (Boss Tutorial, Chefes e Verso dos cards), **evite usar ponto e vírgula (`;`)** quando houver alternativa mais limpa (como ponto final ou quebra de linha `\n`), para não poluir visualmente frases que já tenham parênteses e porcentagens. *(Nas frentes das questões reais do simulado, mantém-se a pontuação literal do PDF).*

### 3.3. Preenchimento Obrigatório do Campo `"subject"` em Todos os Cards

No aplicativo do Trivia Otávio, o campo `"subject"` do JSON é exibido em uma **etiqueta roxa no topo do card** (logo acima da fonte).

* **Regra:** Em **TODOS** os cards do baralho, preencha `"subject"` com o nome exato da matéria e dos tópicos abordados (ex: `"subject": "IA, Redes, Nuvem e Segurança"`), sem jamais errar ou deixar genérico, para que o candidato saiba em qual matéria está acertando ou errando.

## 4. A Ciência do Destaque em Roxo (`c(...)`) e Condicionamento

### 4.1. Função Primária: Condicionamento Comportamental e Números por Extenso

O objetivo nº 1 de pintar palavras de roxo (`c(...)`) é criar um **reflexo condicionado** no olho do candidato. Ao treinar vendo os núcleos decisivos em roxo no Trivia, no dia da prova real ele baterá o olho no papel e focará automaticamente nas palavras que matam a questão.

* **Regra Obrigatória para Números por Extenso no Enunciado (`front`):** Sempre que o enunciado original da questão trouxer um número ou quantidade importante escrita por extenso (ex: `c(seis discos)`, `c(duas falhas)`, `c(oito pontos consecutivos)`, `c(cinquenta servidores)`), envolva-o obrigatoriamente em `c(...)` para treinar o olho do candidato a não perder variáveis camufladas no texto.

### 4.2. A Regra da "Soma dos Roxos" no Verso (Na `~Teoria~`, `~Gabarito~` e `~Gentalha~`)

Muitas vezes o candidato faz uma leitura dinâmica lendo **apenas o que está pintado de roxo** em um item para ganhar tempo.

* **Regra:** Se o aluno ler apenas os trechos dentro de `c(...)` em uma explicação (inclusive dentro da `~Teoria~`!), a junção dessas palavras roxas precisa formar o resumo lógico completo daquele item.

* *Exemplo prático:* Na `~Teoria~` sobre o operador *in*, não deixe o texto todo preto; pinte `c(Listas e Tuplas)` + `c(busca sequencial lenta O(n))` e `c(Conjuntos e Dicionários)` + `c(busca instantânea O(1) via Tabela de Dispersão)`.

### 4.3. Fidelidade da Frente vs. Nova Mecânica Oficial nos Chefes (23/10/2026 às 23:22)

* **Frente das Questões Reais do Simulado (`front` e `options`):** NUNCA altere as palavras originais da banca. Apenas aplique `c(...)` nos termos-âncora e números por extenso do enunciado (`front`) para guiar o olho.

* **Roxo Obrigatório no `stem` dos Chefes Intermediários e Finais (Mecânica de 23/10/2026 às 23:22):** Como os Chefes são de autoria própria, é **OBRIGATÓRIO** usar `c(...)` dentro das afirmativas `vf(I. ...)`, `vf(II. ...)` do `stem` dos Chefes para destacar os 2 a 4 gatilhos principais de cada frase.

## 5. Regras Estruturais das Tags no Verso (`back`)

### 5.1. O Papel da `~Teoria~` (Unidade Conceitual, Regra de Agrupamento e Equilíbrio de Pareto)

* **PROIBIDO Agrupar Conceitos Independentes ou de Tópicos Distintos no Mesmo Item da `~Teoria~`:** Nunca misture, em um mesmo item teórico, conceitos de tópicos ou famílias conceituais diferentes — por exemplo, misturar **Kubernetes** (sondas *Liveness* e *Readiness*) com **Inteligência Artificial** (algoritmos *KNN* e *DBSCAN*), ou misturar *"Lei de Benford, Floresta de Isolamento, DBSCAN e Autocodificador"* num bloco só — **mesmo que eles apareçam juntos na mesma questão ou no mesmo simulado**. A simples presença conjunta em uma questão jamais justifica agrupar famílias conceituais distintas. Cada conceito ou tópico independente deve ter o seu próprio item numerado (`**1) ...**`, `**2) ...**`, `**3) ...**`), dando uma explicação clara e individual para cada um (e enumerando na `~Teoria~` as 6 fases do CRISP-DM sempre que o tema cair).

* **Exceção Harmônica — Agrupamento Permitido de Até 3 Conceitos Relacionados e Simples (Em Concordância com a Seção 4.1 do `Boss Tutorial 2026.md`):** É permitido agrupar **até 3 conceitos relacionados e simples** em um único item da `~Teoria~` (especialmente no Boss Tutorial), desde que todos pertençam ao **mesmo tópico ou família conceitual**, que o agrupamento facilite a compreensão e a comparação entre eles, e que cada modalidade tenha sua característica distintiva explicada com clareza (ex: agrupar *RAID 5*, *RAID 6* e *RAID 10* sob um título abrangente de *RAID — Comparação entre níveis*, ou contrastar *AES*, *RSA* e *SHA-256* em *Ferramentas Criptográficas*).

* **As 4 Condições Obrigatórias de Divisão em Itens Separados:** Mesmo havendo proximidade temática, o agrupamento **DEVE ser dividido** em itens distintos sempre que ocorrer qualquer uma destas 4 situações:

  1. Os conceitos pertencem a **famílias conceituais ou tópicos diferentes** (ex: *Kubernetes* vs. *IA* ou *RAID*);

  2. Há **mais de 3 conceitos** (ex: 4 mecanismos distintos de detecção de anomalias);

  3. Mesmo com até 3 conceitos, a **complexidade** exige explicações individuais para ensinar definições, mecanismos, alvos, diferenças ou defesas (ex: *"Época, Lote e Retropropagação"* ou *"XSS, CSRF e SSRF"* quando exigirem detalhar sujeito, alvo e defesa);

  4. O agrupamento **prejudica a compreensão individual ou a recuperação mental** de cada conceito na hora da prova.

* **Preservação da Atomicidade na `!Regra de Bolso!` (`~Lógica~`):** Mesmo quando um item teórico agrupar até 3 conceitos simples da mesma família (como *RAID 5, RAID 6 e RAID 10*), a seção `!Regra de Bolso!` (`~Lógica~`) continua sendo **100% atômica por decisão**, exigindo uma regra `SE ... ENTÃO ...` própria e separada para cada conceito que demande decisão independente (conforme a Seção 5.3).

* **Calibragem de Profundidade (Pareto + Proporcionalidade):**

  * Dedique a explicação mais completa ao **conceito central** que resolve a questão (e, quando a questão contrastar dois conceitos principais como *Supervisionado vs. Não-Supervisionado*, explique ambos com a mesma proporção).

  * Para os **conceitos secundários** que aparecem apenas nas alternativas erradas, dê uma explicação enxuta e contrastiva (focando na função central e na diferença que elimina a alternativa), sem transformar cada distrator periférico em uma aula gigante.

* **Numeração e Sub-listas:** Só use `**1) ...**`, `**2) ...**` se houver mais de um conceito na `~Teoria~` (se houver apenas 1 conceito, não numere). Caso precise abrir uma sub-lista dentro de um item numérico, use obrigatoriamente letras maiúsculas (`**A) ...**`, `**B) ...**`).

* **Quebras de Linha (`\n` vs. `\n\n`):** Após qualquer subtítulo em negrito no verso, use um único `\n` para começar a explicação na linha de baixo. Use `\n\n` apenas para deixar uma linha vazia entre blocos distintos.

### 5.2. Formato Imutável de `~Gabarito~` e `~Gentalha~`

* **1ª linha:** Reescreva **INTEIRAMENTE** o texto exato da alternativa ou assertiva em negrito (é **TERMINANTEMENTE PROIBIDO** usar reticências `...` para cortar ou abreviar alternativas no verso!).

* **2ª linha (após `\n`):** Escreva `**> CERTO <**` ou `**> ERRADO <**`.

* **3ª linha (após `\n`):** Apresente a explicação clara e direta, antecipando o erro cognitivo provável que levaria o candidato a marcar aquela alternativa.

### 5.3. CLÁUSULA PÉTREA da `!Regra de Bolso!` -> `~Lógica~` (1 Conceito / 1 Operação Mental por Item `SE ... ENTÃO ...`)

* **Regra Matemática 1-para-1 (Uma Operação Mental por Item):** Crie **1 item `SE ... ENTÃO ...` separado para CADA conceito ou operação mental** presente na questão ou no Chefe. Cada item deve funcionar como uma unidade de recuperação curta, direta e independente (1 a 2 linhas).

* **Separação de Operações Inversas em Cálculos:** Se uma questão cobra dois sentidos de uma fórmula (ex: calcular a *Vazão limitada pela janela TCP* dividindo pelo RTT vs. calcular a *Janela Ideal* multiplicando a banda pelo RTT), crie **2 itens separados** na `~Lógica~` (um para a divisão e outro para a multiplicação) para o candidato nunca misturar as duas operações na hora da prova.

* **PROIBIDO misturar 2, 3 ou 4 conceitos dentro do mesmo `SE ... ENTÃO ...`:** Separe cada conceito em seu próprio número (`**1)**`, `**2)**`, `**3)**`...).

### 5.4. Separação Estrita: `!Interpretando a Banca!` (`~Gatilho~`) vs. `!Break para Respirar!` (`~Otávio~`)

* **`!Interpretando a Banca!` (`~Gatilho~`):** Exclusivo para denunciar a malícia/armadilha da banca naquela questão e os erros cognitivos mais prováveis (ex: esquecer de contar o 1º bloco no *chunking* ou trocar cálculo histórico por meta da chefia). Obrigatório nas questões comuns; não vai nos Chefes (salvo se o Chefe focar numa pegadinha clássica da banca).

* **`!Break para Respirar!` (`~Otávio~`):** Obrigatório em todos os Chefes e nas questões difíceis. Serve para três funções de alto valor:

  1. Dar analogias concretas do mundo real (como a conta de luz de R\$ 20 no calor vs. R$ 1.000 de fio cortado).

  2. Fazer **Foreshadowing** (adiantar uma regra teórica importante que vai cair no próximo card, sem entregar a letra do gabarito).

  3. Fazer **Resgate de Detalhe Escondido**: lembrar o candidato daquele detalhe técnico específico que todo mundo esquece (ex: *"Lembre-se: o operador in só é O(1) em Conjuntos e Dicionários"*).

## 6. Dinâmica e Regras de Construção dos "Chefes" (Tutorial, Intermediários e Finais)

### 6.1. Estrutura do Enunciado (`front`) e Gramática Cênica do Otávio nos Chefes

Siga a gramática cênica oficial do personagem **Otávio** na frente (`front`) dos Chefes:

1. **1ª Linha (Título do Chefe):**

   * No **Boss Tutorial**: `**Boss Tutorial (Modo Leve):**` (ou `Modo Padrão` / `Modo Ultra`). Como o campo `"subject"` já mostra os tópicos na etiqueta roxa do topo, **não repita** a lista de matérias na 2ª linha do Boss Tutorial.

   * Nos **Chefes Intermediários e Finais**: `**Chefe Intermediário 1:**` ou `**Chefe Final 3/6:**` na 1ª linha, seguido na 2ª linha (`\n`) por `**[Assunto Claro com Nomes Reais dos Tópicos Revisados naquele Chefe]**`.

2. **Linha em branco (`\n\n`) seguida da Persona em Negrito:** `**- Otávio:**` (obrigatoriamente em **negrito** com o hífen).

3. **Linha de Gesto Físico (`\n` — Parênteses Simples `(...)`):** `(abre o painel de arquitetura da nuvem)`.

4. **Linha de Pensamento Interno (Opcional, `\n` — Parênteses Duplos `((...))`):** Se houver pensamento interno do Otávio, coloque entre parênteses duplos em linha própria: `((Hora de ver se eles realmente dominaram a camada de transporte...))`.

5. **Linha da Fala Direta (`\n` — Sem Parênteses, Sem Hífen e Enxuta):** Escreva a fala direta do Otávio em **1 frase curta, direta e motivadora**, **SEM hífen no começo** e **SEM frases óbvias/redundantes** como *"Leia cada regra abaixo"* ou *"Terceira etapa da revisão final"*.

6. **Última linha nos Chefes Intermediários e Finais (`\n`):** `Julgue:`

### 6.2. Regra de Ouro das Afirmativas (`stem`) nos Chefes Intermediários e Finais: ATOMICIDADE

* **PROIBIDO criar "Afirmativas Frankenstein" (juntar 2, 3 ou 4 conceitos diferentes na mesma frase `vf(...)`):**

  * **REGRA OBRIGATÓRIA DE ATOMICIDADE:** **Cada afirmativa (`I`, `II`, `III`, `IV`, `V`, `VI`) de um Chefe deve testar APENAS UM ÚNICO CONCEITO ou UM ÚNICO PROBLEMA!**

  * **Capacidade por Card e Liberdade para Criar Mais Partes no Chefe Final:** Cada card de Chefe comporta **até 6 afirmativas (`I` a `VI`)**. O Chefe Final pode ser dividido em **4, 5, 6 ou quantas partes forem necessárias** (`Chefe Final 1/6` a `6/6`) até cobrir 100% dos conceitos do simulado sem espremer dois assuntos na mesma frase.

  * Nos **Chefes Intermediários**, inclua pelo menos 1 afirmação relevante para cada questão anterior do bloco revisado, testando a compreensão real (e não a simples decoreba literal de uma frase).

### 6.3. Regras Gerais do Boss Tutorial (`ti_ceX_boss_tutorial` — Especificação Completa em `Boss Tutorial 2026.md`)

Para construir ou editar qualquer **Boss Tutorial**, consulte e aplique integralmente o arquivo **`Boss Tutorial 2026.md`**, respeitando seus pilares centrais:

1. **Pergunta Obrigatória sobre os 3 Modos Antes de Gerar:**

   * **Modo Leve:** Aborda apenas os **2 conceitos-chave** que resolvem cada questão. Na frente (`stem`), usa explicação conversada direta (média de **38 palavras ±35%**, ou seja, **25 a 51 palavras** / ≈ 36 a 74 tokens), sem blocos *Impacto/Exemplo/Resultado*. Quando houver sub-itens internos na frente (ex: `**RAID 5:**`, `**RAID 10:**`), cada sub-item começa em uma nova linha (`\n`), mas sua explicação segue **na mesma linha** logo após os dois-pontos.

   * **Modo Padrão:** Aborda **no mínimo 2 conceitos por questão** (2 nas simples, todos os 4–5 nas difíceis). Na frente (`stem`), traz definição + mecanismo seguidos de `**Impacto:**`, `**Exemplo:**` e `**Resultado:**` (em negrito, sem hífen, pulando linha `\n` após os dois-pontos).

   * **Modo Ultra:** Aborda **100% de todos os conceitos e distratores** de todas as questões. Na frente (`stem`), divide cada item em `**A) DEFINIÇÃO:**`, `**B) MECANISMO:**` e `**C) GATILHO DE PROVA:**` separados por `\n\n`, e no verso traz `~Aprofundamento Ultra~` com `**Simulador de banca:**`.

2. **Dimensionamento do Lote e Duas Camadas de Profundidade:**

   * Até **12 questões** geram até **20 itens** no Boss Tutorial (menos de 12 questões geram menos de 20 itens).

   * Quando cobrir conceitos principais e secundários: o **Conceito Principal** recebe **45 a 70 palavras** (≈ 65 a 100 tokens) e o **Conceito Secundário** recebe **20 a 35 palavras** (≈ 30 a 50 tokens), ambos com **Lacuna Zero**.

3. **Delimitação de Escopo (Agrupar vs. Dividir — Seção 4.1 do `Boss Tutorial 2026.md` e Seção 5.1) e Atomicidade Obrigatória da `!Regra de Bolso!` (`~Lógica~`):**

   * **Quando agrupar vs. dividir no item teórico (`stem` e `~Teoria~`):** É permitido agrupar **até 3 conceitos relacionados e simples** em um único item do Boss Tutorial desde que todos pertençam ao **mesmo tópico ou família conceitual** e o agrupamento facilite a comparação, explicando cada modalidade com clareza (ex: *RAID 5, RAID 6 e RAID 10* em *RAID*). Porém, é **obrigatório dividir em itens separados** nas 4 situações: (1) quando pertencerem a famílias conceituais ou tópicos independentes — como misturar *Kubernetes (sondas Liveness e Readiness)* com *Inteligência Artificial (KNN, DBSCAN)* ou *RAID*, mesmo que apareçam na mesma questão; (2) quando houver **mais de 3 conceitos**; (3) quando, mesmo com até 3 conceitos, a complexidade exigir explicações individuais de definições, mecanismos, alvos, diferenças ou defesas; ou (4) quando o agrupamento prejudicar a compreensão individual ou a recuperação mental.

   * **Atomicidade por Decisão na `!Regra de Bolso!` (`~Lógica~`):** Mesmo quando o item teórico agrupar 2 ou 3 conceitos relacionados (como *RAID 5, RAID 6 e RAID 10*), a seção `~Lógica~` **DEVE separar cada decisão independente em sua própria regra `SE ... ENTÃO ...`** (ex: 1 regra para RAID 5, 1 para RAID 6 e 1 para RAID 10). A quantidade de regras de bolso acompanha a quantidade de decisões independentes exigidas pelo conteúdo.

4. **Sem Spoiler Numérico e Diagramação do Verso:**

   * Ao exemplificar fórmulas no Boss Tutorial, prefira usar números fictícios redondos (ou focar na estrutura algébrica) para não entregar o resultado numérico pronto das questões seguintes.

   * No verso (`back`), cada item da `~Teoria~` / `~Aprofundamento Gold~` tem média de **36 palavras ±35%** (**23 a 49 palavras**, ou até 75 palavras em cálculos), colocando cada fórmula ou implicação da `**Decisão:**` em sua própria linha (`\n`).

### 6.4. Clareza Obrigatória das Pegadinhas (`**Pegadinha:**`) e Banimento de Frases Telegráficas ou LaTeX (`\times`)

* **Regra da Pegadinha Explicativa (Zero Frases Telegráficas):** Toda `**Pegadinha:**` (no verso do Boss Tutorial) ou `!Interpretando a Banca!` (`~Gatilho~`) deve ser **clara, específica e pedagogicamente explicativa**. É **PROIBIDO** escrever frases telegráficas que jogam um número solto entre parênteses obrigando o estudante a adivinhar de onde saiu aquele valor (ex: NUNCA escreva *"Esquecer de descontar 1 disco no RAID 5 (24 TB)"* ou *"Ignorar a sobreposição (9)"*).

* **Como Redigir Pegadinhas de Cálculo:** Sempre que a pegadinha envolver um cálculo, você deve obrigatoriamente explicitar os **3 elementos**:

  1. **Qual é a conta ou raciocínio incorreto** (ex: multiplicar todos os 6 discos direto por 4 TB achando a capacidade bruta);

  2. **Qual é o resultado incorreto que aparece na alternativa falsa** (ex: `6 ⋆ 4 = 24 TB`);

  3. **Por que está errado / qual é a distinção conceitual** (ex: esquecer que a capacidade bruta não é a capacidade útil, pois o RAID 5 reserva 1 disco inteiro para paridade, sobrando `6 - 1 = 5 discos úteis`, logo `5 ⋆ 4 = 20 TB úteis`).

* **Linguagem Humana nas Contas (PROIBIDO LaTeX como `\times`):** Ser humano não fala nem lê `\times`! Jamais use comandos LaTeX (`\times`, `\div`, `$`) ou fórmulas coladas sem espaço. Mostre o raciocínio na ordem mental natural em que uma pessoa faz a conta na cabeça, usando o símbolo padrão **`⋆`** (ou escrevendo *"vezes"*) e nomeando o que cada número representa:

  * *Exemplo Padrão Ouro (RAID — Item 19):*

    * **Pegadinha:** Multiplicar todos os 6 discos direto por 4 TB (`6 ⋆ 4 = 24 TB`, que é a **capacidade bruta**, e não a **capacidade útil**), esquecendo que o RAID 5 reserva 1 disco para paridade; ou confundir o espaço útil do RAID 10 (`12 TB`) com o do RAID 6 (`16 TB`).

    * **Decisão:** Faça `(quantidade de discos menos a reserva) ⋆ tamanho do disco`:
      RAID 5 (`N - 1`): `6 - 1 = 5 discos úteis`, logo `5 ⋆ 4 TB` = c(20 TB úteis).
      RAID 6 (`N - 2`): `6 - 2 = 4 discos úteis`, logo `4 ⋆ 4 TB` = c(16 TB úteis) (suporta c(2 discos queimarem juntos)).
      RAID 10 (`N / 2`): metade vira espelho (`6 / 2 = 3 discos úteis`), logo `3 ⋆ 4 TB` = c(12 TB úteis).