# DIRETRIZES DO BARALHO (JSON) - TRIVIA OTÁVIO

**Atenção Inteligência Artificial:** Este arquivo não é apenas um guia de formatação. Ele é o **Manual de Treinamento e Especificação Técnica Obrigatória** para que você aprenda a construir os baralhos do projeto. Você deve consultar este documento como a fonte suprema da verdade. Cada regra descrita aqui possui um motivo pedagógico e cognitivo associado à Neurodivergência (TEA/TDAH); não ignore nem resuma nenhum tópico.

## 1. Arquitetura Pedagógica e o Princípio do Estudo Reverso Autossuficiente
O candidato chega ao baralho **cru** (sem ler a teoria antes) e se recusa a ler PDFs de 50 páginas. O **Trivia Otávio** é a única fonte de aprendizado.
*   **A Meta Nível 6:** O baralho deve entregar teoria suficiente e mastigada para que o candidato atinja o nível 6 de 10 em conhecimento daquele assunto, garantindo mais de 50% de chance de acerto em qualquer prova real.

### A Engrenagem de Miniciclos de Revisão
*   **Boss Tutorial:** É o card mais vital. Ele introduz a teoria primária. O aluno bate o olho aqui e seu cérebro já liga o alerta para as questões seguintes.
*   **Questões do Simulado (Estudo Reverso):** As questões ensinam através do erro e do teste da teoria abordada no Tutorial.
*   **Verso (`~Teoria~`) e Chefes Finais:** Formam miniciclos de revisão e testes repetidos na mesma sessão, consolidando a memória espaçada ativamente.

### Hierarquia de Tags no Verso (O Mapeamento Ocular do Candidato)
O verso deve obrigatoriamente seguir esta estrutura de leitura, pois reflete a "sede de olhar" de quem está estudando:
1.  **`!Otávio!` -> `~Teoria~`:** (O primeiro lugar para onde o olho vai, seja acertando ou errando).
2.  **`~Gabarito~`:** (Lido logo em seguida por quem errou).
3.  **`~Gentalha~`:** (Consulta pontual para eliminar dúvidas sobre opções erradas específicas).
4.  **`!Regra de Bolso!` -> `~Lógica~`:** (O local de fixação rápida de conceitos-chave usando regras condicionais SE/ENTÃO).
5.  **`!Interpretando a Banca!` e `!Break para Respirar!`.**

## 2. A Adaptação Rigorosa para Neurodivergência (TDAH e TEA)
O aluno tem TDAH e TEA. Explicações labirínticas com linguagem difusa exigem múltiplas leituras e causam exaustão mental e abandono ("custo cognitivo alto"). O aprendizado deve ter **custo de aprendizado zero na leitura**.


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

### Simplicidade Extrema, Literalidade e Português do Dia a Dia (Banimento da "Sopa de Adjetivos")
A linguagem do verso **NÃO PODE** ser robótica, rebuscada ou pedante. Você deve explicar como se fosse um colega de estudos conversando em uma mesa de bar, focando no **Por Que** de forma utilitária.
- **PROIBIDO ("Sopa de Adjetivos" e Jargões Empilhados):** É estritamente proibido criar frases aglomerando múltiplos adjetivos sem sentido apenas para o texto parecer rico (ex: *Não escreva* "fita biológica contígua fotográfica estrita original ativa limítrofe amarrada").
- Use a fórmula: Sujeito + Verbo + Complemento. Traduza IMEDIATAMENTE qualquer jargão técnico invocado na explicação (ex: se usar a palavra "esparsos" ou "core", explique que significa "espalhados" e "região densa" logo em seguida).

### Matemática, Estatística e Exatas (O Nível Iniciante Absoluto / Totalmente Mastigado)
- Assuma que o leitor é **100% leigo ("explique de um jeito que até um macaco entenderia")**.
- **NÃO PULE ETAPAS MENTAIS.** Explique de onde surgiu a fórmula, o que significa cada letra (ex: *o que é o 'd' na Lei de Benford?*) e mostre a conta linha por linha. Em Exatas, é permitido e exigido que o verso seja mais longo, separando cada passagem matemática com `
` e rótulos do tipo **Passo 1**, **Passo 2**.

### A Regra da Integralidade do Boss Tutorial
- O "Boss Tutorial" é a fundação do bloco de questões. Quando solicitado para criar ou revisar um Boss Tutorial, a IA deve **SEMPRE gerar o card completo**, do primeiro ao último item solicitado (geralmente entre 10 e 20 itens). 
- **Nunca interrompa ou entregue o card pela metade** sob a justificativa de "usar como exemplo". Se o usuário forneceu 16 conceitos, a frente (`stem`) deve listar os 16 conceitos, e o verso (`~Aprofundamento Gold~` ou similar) deve expandir e detalhar os 16 conceitos. 
- O alinhamento estrutural deve ser simétrico: a quantidade de tópicos na frente deve corresponder exatamente à quantidade de explicações no verso.

### A Tag "!Break para Respirar!" e Relevância do Otávio
- A tag secundária `~Otávio~` que reside dentro do `!Break para Respirar!` não pode ser uma frase genérica inútil de motivação barata (ex: "Continue estudando e você vai passar!").
- Ela deve OBRIGATORIAMENTE entregar uma **Dica Estratégica de Alto Valor (High-Yield)** sobre a natureza da prova, o estilo da banca, a mecânica da matéria ou como resolver aquele problema em ambiente de pressão. O conteúdo deve ser tão valioso que a sua remoção causaria perda educacional real para o aluno.

---

## 6. Regras de Arquivo e de Enunciado e Formatação de Chefes

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

### A Regra do Verso do Boss Tutorial (Literalidade Radical e Fórmulas)
O verso do Boss Tutorial (`ti_ceX_boss_tutorial`) não deve utilizar a tag `~Front-Loading do Tutorial~`. Deve ir direto para `~Aprofundamento Gold~` seguindo estas regras de espaçamento e conteúdo:
1. **Quebra de Linha (Obrigatório):** Após os rótulos secundários OBRIGATORIAMENTE EM NEGRITO (`**Como aparece:**`, `**Pegadinha:**`, `**Decisão:**`), deve-se usar os dois pontos e em seguida pular de linha OBRIGATORIAMENTE com um único `\n` antes de iniciar a explicação. Não escreva a explicação na mesma linha do rótulo.
2. **A Decisão:** A "Decisão" deve ser focada exclusivamente na postura do candidato na prova. Não repita teoria aqui; entregue o comando final ou norte prático ("Viu a palavra X, associe a Y").

## 3. A Ciência do Destaque em Roxo (`c(...)`) e Condicionamento
### Função Primária: Condicionamento Comportamental
O objetivo nº 1 de pintar palavras de roxo (`c(...)`) é treinar o olho do candidato. No dia da prova real, ele precisa bater o olho nas mesmas palavras no enunciado e acionar a memória instantânea. Sempre aplique roxo naquilo que o candidato precisaria grifar para resolver a questão.

### A Regra da "Soma dos Roxos" no Verso
Se o candidato ler **apenas** os trechos pintados de roxo dentro de um parágrafo de explicação, a soma dessas palavras deve formar o resumo lógico daquele conceito. Não pinte palavras soltas sem sentido; pinte os núcleos conceituais (ex: `c(não supervisionada)` e `c(cortar aleatoriamente)`).

### Fidelidade da Frente vs. Liberdade no Verso
- **Frente (`front` e `options` de simulados):** NUNCA altere as palavras originais da banca. Apenas aplique `c(...)` nas palavras-chave do enunciado para guiar o olho (ex: `c(lei de Benford)`).
- **Verso (`back`):** Liberdade total para fatiar, numerar, criar "Passo 1 / Passo 2" e simplificar o idioma.

### NOVA MECÂNICA OFICIAL: Roxo no `stem` dos Chefes
A partir de 23/10/2026, é **OBRIGATÓRIO** usar a tag de cor roxa `c(...)` dentro das assertivas I, II, III (dentro da tag `vf()`) nos Chefes Intermediários e Finais.
*Exemplo:* `vf(I. Agrupamentos c(desprovidos de rótulos) ocorrem com o Aprendizado c(Supervisionado).)`

## 4. Regras Estruturais das Tags no Verso

### O Papel da `~Teoria~` ("A Explicação da Professora")
A Teoria serve para explicar o conceito do zero antes de o aluno ler por que ele errou.
- **Proporcionalidade:** Se a questão fala de A e B, a Teoria deve explicar A e B com a mesma profundidade.
- **Nos Chefes:** É **PROIBIDO** deixar a Teoria apenas citando os temas (ex: "Revisão de Benford e Clustering"). Você deve enumerar e **explicar rapidamente** cada conceito cobrado no Chefe.
- **Numeração:** Só use `**1) ...**`, `**2) ...**` se houver mais de um conceito. Se houver apenas 1, não numere.
- **Quebras de Linha (`
` vs `

`):** Após o título em negrito de um subtópico na Teoria, aplique um único `
` para que a explicação comece na linha de baixo (nunca na mesma linha). Use `

` apenas para separar blocos distintos.

### Formato Imutável de `~Gabarito~` e `~Gentalha~`
- **1ª linha:** Reescreva o texto exato da alternativa/assertiva. (Evita que o aluno precise voltar o card para ler).
- **2ª linha:** Pule uma linha (`
`) e escreva `**> CERTO <**` ou `**> ERRADO <**`.
- **3ª linha:** Pule uma linha (`
`) e forneça a explicação clara.
- Nos Chefes, separe claramente as análises de cada item (I, II, III, IV) para consulta rápida.
### CLÁUSULA PÉTREA da `!Regra de Bolso!` -> `~Lógica~` (Quantidade 1-para-1)
É **Rigorosamente Proibido** fazer apenas 1 item genérico na Lógica se a questão cobrou vários conceitos.
- **A Regra Matemática:** Você deve criar no mínimo 1 regra "SE... ENTÃO..." para CADA conceito presente na questão. Se as alternativas da questão (incluindo as erradas) citam 4 conceitos diferentes, você fará **4 itens na Lógica**.
- As frases da Lógica devem ser curtas, diretas e autossuficientes.

### Separação Estrita: `!Interpretando a Banca!` vs `!Break para Respirar!`
- **`!Interpretando a Banca!` (`~Gatilho~`):** Serve **EXCLUSIVAMENTE** para denunciar a pegadinha específica daquela questão ("A banca tentou te enganar trocando X por Y"). Usa-se nas questões comuns. Em Chefes, só use se o Chefe focar numa armadilha clássica.
- **`!Break para Respirar!` (`~Otávio~`):** Serve para o Otávio dar macetes, analogias ricas do cotidiano (ex: "Causa Especial é como ter a luz cortada") e **Foreshadowing** (ensinar uma regra sem dar o gabarito explícito para preparar o candidato para o card seguinte). Deve ser mais usado em questões muito difíceis e Chefes.

### Padronização de Idioma e Calibragem de Relógio
- **Idioma:** Sempre acompanhe o idioma cobrado na questão. Se houver dualidade, escreva ambos na primeira menção: `Floresta de Isolamento (Isolation Forest)`. Não fique oscilando de um para outro ao longo do texto.
- **Relógio (`timer_override`):** A menos que explicitamente solicitado o contrário, sempre aplique uma "folga de leitura" de **+60 segundos** acima da média das questões comuns para evitar estresse desnecessário no TDAH.

### 5. Regras de Fórmulas Matemáticas e Formatação Adicional

**Fórmulas Matemáticas:** Sempre que um conceito matemático for ensinado (ex: Probabilidade Binomial, RMSE, Variância, Fórmulas de Engenharia), a fórmula deve ser transcrita de modo acessível, destrinchando o significado de cada letra (N, K, P).
   - **Sinal de Multiplicação:** Para indicar contas de multiplicação, OBRIGATORIAMENTE utilize o caractere estrela/asterisco especial `⋆` (e não o asterisco normal `*` ou `x`). Exemplo: `Combinação(N, K) ⋆ p^K ⋆ (1-p)^(N-K)`.
**Proibição de Aspas Simples para Destaque:** NUNCA utilize aspas simples (`'`) para dar destaque em jargões, nomes de ferramentas, ou comandos de código (ex: NUNCA escreva 'groupby', 'finally', 'argmax'). Para destacar comandos e termos técnicos, utilize **obrigatoriamente itálico** (`*groupby*`, `*argmax*`) ou a tag de cor roxa `c(termo)`. Aspas simples servem estritamente para figuras de linguagem literais que todos entendam ou para citações textuais. O uso de backticks (crases) (\`) continua absolutamente banido em todo o material.
