
### Preenchimento de Lacunas de Materiais de Terceiros (A Regra do "Como" e "Por Quê")
Quando a explicação original do PDF for vaga, assumir conhecimento prévio ou não explicar o *mecanismo prático* de um conceito (ex: "Canary Release lança para 5% do tráfego", mas sem explicar *como* esses 5% são escolhidos ou o que acontece depois), a IA **DEVE OBRIGATORIAMENTE**:
1. Copiar a base da explicação do professor (para manter a fidelidade).
2. Adicionar um parágrafo extra (geralmente dentro da `~Teoria~` ou detalhando a alternativa) explicando o passo a passo concreto de **COMO** a tecnologia/lei funciona no mundo real, utilizando analogias mecânicas ou do dia a dia.
*Exemplo prático de falha:* Dizer "Feature Toggles são variáveis de ambiente (If/Else) já em produção". 
*Exemplo prático corrigido:* "Feature Toggles funcionam como um 'Interruptor de Luz' escondido no código. O código novo já foi enviado para o celular de todos os usuários, mas está 'desligado' (If = False). Quando o diretor aprova, o programador aperta um botão no servidor, a variável muda para 'True', e a funcionalidade acende instantaneamente no celular de todo mundo, sem precisar enviar uma nova atualização na loja de aplicativos."

### A Função dos Chefes Intermediários (Revisão Ativa)
Os Chefes Intermediários não são meras pausas na jornada; eles exercem o papel fundamental de **Revisão Ativa**. 
O conteúdo das afirmativas de um Chefe Intermediário deve ser construído para **recuperar, testar e reforçar os conceitos-chave** que acabaram de ser ensinados no bloco de questões imediatamente anterior a ele. 
Se as questões 97 a 101 ensinaram sobre "Pontos de Função", "Canary Release" e "Event Loop", o Chefe Intermediário que as sucede deve ter afirmações que testem exatamente essas regras, forçando o cérebro do candidato a consolidar o aprendizado recente antes de avançar para os próximos tópicos.

### Neurodiversidade e Clareza de Linguagem (TEA / TDAH)
Na construção de textos, **não adote presunção de conhecimento prévio do candidato**. 
- Sempre que uma sigla secundária técnica for apresentada (ex: SMTP, HTML, IP), abra parênteses para uma explicação brutalmente simples de 3 palavras (ex: `SMTP (protocolo de e-mail)`).
- Evite metáforas altamente subjetivas. A figura de linguagem deve ser **literal e concreta**. 
- **Estruturação de Listas:** Se for necessário aninhar uma lista dentro de um item numérico (ex: `**1) Tópico**`), a sub-lista deve ser OBRIGATORIAMENTE **alfabética** (`A, B, C`), jamais usar numeração aninhada (`1, 2, 3`) para não confundir o leitor.
- **Tag Lógica (Se/Então):** Se a questão testar 4 conceitos diferentes, a tag de lógica do card correspondente **DEVE** fornecer uma frase de 'SE/ENTÃO' para **cada um** desses 4 conceitos, e não apenas para um deles. O cérebro neurodivergente precisa de regras curtas amarradas para todos os padrões da questão.

### Feedback de Desempenho e Distribuição de Chefes Finais
- Quando o usuário informar os resultados da sessão (ex: "Desempenho: 12%, Resultado: Reprovado", com os detalhes de Acertos/Erros), a IA deve analisar essas estatísticas antes de iniciar a próxima tarefa para identificar quais assuntos o usuário teve mais dificuldade e ajustar a severidade das explicações nas próximas construções.
- **Regra de Fatiamento do Chefe Final (Card Final):** Se o número de questões de um bloco for superior à capacidade máxima suportada em um único card de Chefe Final (máximo 5 afirmações ou máximo de espaço legível), o Chefe Final **DEVE OBRIGATORIAMENTE** ser fatiado em Parte 1 e Parte 2.
    *   *Exemplo Prático:* Se um bloco tem 9 questões, não crie um Chefe Final abrangendo apenas as 4 primeiras questões e omitindo as restantes. Crie dois cards: "Chefe Final - Parte 1" (cobrindo as questões 1 a 5) e "Chefe Final - Parte 2" (cobrindo as questões 6 a 9). **O fechamento da matéria deve recuperar ativamente 100% das questões do simulado.**

### Literalidade e Analogias Concretas (Neurodidática Avançada)
1. **Termos Subjetivos e Poéticos SÃO PROIBIDOS:** Nunca utilize adjetivos ou metáforas que exijam abstração interpretativa (ex: usar "tesoura fria" para *Coalesce*, "furacão" para *Repartition*, "ajusante/downstream" para *Linhagem*, ou "panaceia mastodôntica"). O cérebro neurodivergente (TEA/TDAH) precisa da imagem mecânica e literal: 
   - *Correto:* "Coalesce junta blocos vizinhos sem gastar rede da internet. Repartition reorganiza todos os blocos enviando dados pela rede."
2. **Definição de Jargões Embutidos:** Se para explicar um conceito você precisa usar outro conceito complexo, **defina-o imediatamente em parênteses ou em uma frase anexa**.
   - *Incorreto:* "Arquitetura Kappa descarta a via Lote/Batch."
   - *Correto:* "Processamento em Lote (Batch) analisa pacotes grandes de dados antigos. A Arquitetura Kappa descarta essa via..."
   - *Incorreto:* "Inmon centraliza o Data Warehouse."
   - *Correto:* "Um Data Warehouse é um banco de dados gigante para análises da diretoria. Inmon defende centralizá-lo..."
3. **Mecânica das Tabelas (O "Como"):** Ao falar de junções (Joins) ou cruzamentos, deixe explícito *quantas vezes* ou *como* ocorre matematicamente. Se ocorre multiplicação de linhas repetidas (Produto Cartesiano), esclareça que é "uma única vez para cada par correspondente", para não deixar o candidato achando que a multiplicação é infinita.
4. **Alinhamento de Impacto, Exemplo e Resultado:** Na frente do Boss Tutorial, utilize a trinca explicativa sempre alinhada com a realidade corporativa:
   - **Impacto:** Qual o ganho ou prejuízo sistêmico? (Ex: Economiza internet).
   - **Exemplo:** O cenário técnico exato e tangível.
   - **Resultado (Resolução):** O que o código produz de fato, quantificando se possível.

### A Regra da Integralidade do Boss Tutorial
- O "Boss Tutorial" é a fundação do bloco de questões. Quando solicitado para criar ou revisar um Boss Tutorial, a IA deve **SEMPRE gerar o card completo**, do primeiro ao último item solicitado (geralmente entre 10 e 20 itens). 
- **Nunca interrompa ou entregue o card pela metade** sob a justificativa de "usar como exemplo". Se o usuário forneceu 16 conceitos, a frente (`stem`) deve listar os 16 conceitos, e o verso (`~Aprofundamento Gold~` ou similar) deve expandir e detalhar os 16 conceitos. 
- O alinhamento estrutural deve ser simétrico: a quantidade de tópicos na frente deve corresponder exatamente à quantidade de explicações no verso.

### A Tag "!Break para Respirar!" e Relevância do Otávio
- A tag secundária `~Otávio~` que reside dentro do `!Break para Respirar!` não pode ser uma frase genérica inútil de motivação barata (ex: "Continue estudando e você vai passar!").
- Ela deve OBRIGATORIAMENTE entregar uma **Dica Estratégica de Alto Valor (High-Yield)** sobre a natureza da prova, o estilo da banca, a mecânica da matéria ou como resolver aquele problema em ambiente de pressão. O conteúdo deve ser tão valioso que a sua remoção causaria perda educacional real para o aluno.

---

## 8. Novas Regras de Enunciado e Formatação de Chefes

### Uso do `stem` para Itens Enumerados com ou sem V/F
A regra geral é **SEMPRE** utilizar o botão de Verdadeiro ou Falso (`vf()`) para itens enumerados (I, II, III).
- Se a questão avaliar se os itens são verdadeiros ou falsos (ex: nas alternativas diz "Apenas I e II estão corretas", ou "I é verdadeira e II é falsa", ou "V, V, F, F"), os itens **DEVEM** obrigatoriamente ser encapsulados com `vf()` dentro do `stem`.
- O único caso em que os itens enumerados devem ser colocados no `stem` **sem** a tag `vf()` é quando a questão não tem relação com certo/errado, mas sim pede uma correlação direta (Ex: "A ocorrência 1 configura falha de X, a ocorrência 2 configura falha de Y"). Apenas neste cenário muito específico de correlação/associação, a tag `vf()` é dispensada.

### Estrutura do Enunciado (`front`) para Chefes (Intermediários e Finais)
O título e a apresentação dos Chefes (com exceção do Tutorial) no campo `front` devem seguir um padrão rígido de espaçamento e negrito, abandonando a linha única contínua.
Exemplo de formato obrigatório (note as quebras de linha `\n` separando cada elemento):

```json
"**Chefe Final 3:**\n**DAX, Power Query e BI Analytics**\n\n- Otávio:\n(Digita as métricas da dashboard)\n- O front-end da nossa inteligência. Aqui as medidas decidem o repasse tributário de SC.\nJulgue:"
```

- **Primeira linha:** `**[Tipo do Chefe] [Número/Parte]:**`
- **Pula linha (ir para linha de baixo):** `\n`
- **Assunto:** `**[Assunto]**`
- **Pula linha (deixa uma linha em branco inteira de distância):** `\n\n`
- **Persona:** `- Otávio:`
- **Pula linha (ir para linha de baixo):** `\n`
- **Ação:** `(Ação descritiva do personagem entre parênteses)`
- **Pula linha (ir para linha de baixo):** `\n`
- **Fala:** `- Fala do personagem.`
- **Pula linha (ir para linha de baixo):** `\n`
- **Encerramento:** `Julgue:` (ou similar, terminando com dois pontos).
