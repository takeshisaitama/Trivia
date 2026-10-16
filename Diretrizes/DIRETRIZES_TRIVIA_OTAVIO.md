
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
