# Resumo Definitivo: Como montar um baralho do Trivia Otávio (TO)

Este documento contém as diretrizes **estritas** de formatação, layout e conteúdo para a criação de baralhos JSON do aplicativo Trivia Otávio. O desrespeito a qualquer uma destas regras gera degradação visual e educacional no aplicativo.

## 1. Estrutura do Baralho e dos Bosses
- O primeiro card de um bloco de matéria é **SEMPRE o Chefe Tutorial** ("Boss Tutorial").
- O Boss Tutorial ensina a teoria, ele não testa o usuário. O *stem* é apenas a lista enumerada de conceitos.
- **Boss Intermediário**: A cada X questões (ex: 3), cria-se um Chefe Intermediário. Ele testa V/F dos conceitos das questões anteriores, exigindo formatação `vf(...)` no *stem*.
- **Boss Final**: Ao fim de uma matéria, testa todos os principais conceitos revisados. Máximo de 6 afirmativas por card (se houver mais, crie Parte 1, Parte 2, etc).

## 2. A Regra de Ouro (Cláusula Pétrea das Alternativas)
- **NUNCA, JAMAIS abrevie ou corte o texto de uma alternativa no verso do card.**
- O uso de reticências (`...`) ou cortes (ex: `A) .texto...`) nas seções `~Gabarito~` e `~Gentalha~` é **estritamente proibido**.
- A alternativa (seja de V/F ou múltipla escolha) DEVE ser transcrita na **íntegra**, exatamente como apareceu na frente do card. Não importa se o card ficar longo, a transcrição completa é exigência pedagógica para não gerar desinformação.

## 3. Formatação da Teoria em Cards Normais (O Maior Erro Histórico)
- Na subtag `~Teoria~` de um card normal, **NÃO USE** títulos genéricos e inúteis como `**1) Fundamento da Questão:**`.
- O título do item na Teoria DEVE ser o **nome do conceito** ou a citação do artigo (ex: `**1) Art. 84, XXIV:**` ou `**1) Papel do Congresso Nacional:**`).
- A explicação/texto de lei desse conceito NÃO fica na mesma linha. Ela deve vir na **linha de baixo**, sem negrito.
- Não faça explicações vazias como "É o teor do art. 5º". Traga o texto da lei ou a explicação substantiva.
- Entre um conceito e outro (ex: do item 1 para o item 2), pule uma linha em branco (`\n\n`).
  *Exemplo Correto para a Teoria de cards normais (notem os `\n` literais):*
  ```json
  "**1) Art. 84, XXIV:**\nCompete-lhe prestar, anualmente, ao Congresso Nacional, dentro de sessenta dias...\n\n**2) Art. 84, XXVIII:**\nAtribui ao Presidente a proposta de decretação do estado de calamidade pública..."
  ```

## 4. O Boss Tutorial - Regras Estritas de Layout
- O verso do Boss Tutorial **NÃO** possui as tags `~Gabarito~` nem `~Gentalha~`.
- A `~Teoria~` do Boss Tutorial espelha exatamente a numeração do *stem*.
- Para cada item na Teoria, utilize as três marcações obrigatórias: `**Como aparece:**`, `**Pegadinha:**` e `**Decisão:**`.
- **Formatação Crítica (Atenção redobrada):**
  1. NÃO coloque hífen (`-`) antes dessas marcações.
  2. A explicação de cada marcação DEVE ser colocada na **linha seguinte** (um `\n`). Não escreva na mesma linha.
  *Exemplo Correto (mostrando os `\n` literais para a string JSON):*
  ```json
  "**1) Princípio da Moralidade:**\n**Como aparece:**\nA banca diz que...\n**Pegadinha:**\nTentar confundir com legalidade...\n**Decisão:**\nMarque a alternativa que...\n\n**2) Próximo Conceito:**"
  ```
- A `~Lógica~` do Boss Tutorial também deve espelhar a numeração, com exatamente uma frase de formato "**X) SE... ENTÃO...**" para cada item, separadas por `\n\n`.

## 5. Tags Secundárias Obrigatórias
- **!Regra de Bolso!** (com `~Lógica~`): Obrigatória em TODOS os cards.
- **!Break para Respirar!**: Obrigatória em **TODOS os Bosses** (Tutorial, Intermediários e Final) e em questões normais muito difíceis ou longas. O texto começa direto, sem hífen (ex: `~Otávio~\nRespire fundo...`).
- **!Interpretando a Banca!**: Obrigatória nas questões normais. Fornece gatilhos específicos ou "fumaças" (armadilhas) sobre como aquela banca específica atua na matéria.

## 6. Layout de Gabarito e Gentalha
- A explicação do erro/acerto de uma afirmativa vem **sempre abaixo** da transcrição (íntegra) da afirmativa.
- Use `**> CERTO <**` e `**> ERRADO <**`. Esse marcador deve ficar **sozinho** na sua própria linha. A explicação vem logo abaixo dele.
  *Exemplo de string JSON para Gabarito:*
  ```json
  "**A) O Estado responde objetivamente pelos danos...**\n**> ERRADO <**\nA regra correta, segundo o STF, estabelece que..."
  ```
- Cuidado com o *casing*: ao copiar trechos de lei ou alternativas, preserve a capitalização original (não transforme numerais romanos como XXIV em "xxiv").

## 7. Outras Limitações Técnicas
- As alternativas V/F no *stem* (em bosses ou questões normais) devem ser envolvidas na função `vf()` (ex: `vf(I. A empresa responde objetivamente.)`).
- Use a marcação `c(texto)` para pintar palavras-chave de roxo (cloze). Não use chaves como Anki tradicional.
- Imagens usam sintaxe própria: `{{img:CAMINHO|LARGURA|LEGENDA}}`.
- Sem suporte a LaTeX. Fórmulas devem ser convertidas para texto puro estruturado.
