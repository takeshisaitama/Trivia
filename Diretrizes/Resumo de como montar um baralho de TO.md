# Diretrizes para Construção de Baralhos do Trivia Otávio

Este documento define o padrão arquitetural e as regras de formatação exigidas para a criação de cartas JSON no aplicativo **Trivia Otávio**. Qualquer inteligência artificial que construir ou modificar baralhos deve seguir este documento rigorosamente.

---

## 1. Estrutura Base do JSON
Cada questão no Trivia Otávio é representada por um objeto JSON dentro de uma lista principal. O formato base é:

```json
{
  "type": "normal",
  "id": "identificador_unico_q1",
  "subject": "Matéria da Questão",
  "source": "Banca / Origem da Questão",
  "timer_override": 180,
  "front": "**Questão 01:**\n\nEnunciado principal da questão.",
  "stem": [],
  "options": [
    "A) Opção 1.",
    "B) Opção 2.",
    "C) Opção 3.",
    "D) Opção 4.",
    "E) Opção 5."
  ],
  "answer": 0,
  "back": "Gabarito: A. \n\n !Otávio! \n ~Teoria~ \n **1) Primeiro conceito a ser explicado:** \n Explicação do conceito \n\n **2) Segundo conceito a ser explicado:** \n Explicação do conceito. \n\n ~Gabarito~ \n Explicação da alternativa correta. \n\n ~Gentalha~ \n Explicações por que as outras alternativas estão incorretas. \n\n !Regra de Bolso! \n ~Lógica~ \n **1) SE** X, **ENTÃO** Y. \n\n !Interpretando a Banca! \n ~Gatilho~ \n Dica sobre a maldade da banca. \n\n !Break para Respirar! \n ~Otávio~ \n Uma mensagem compartilhando algo útil para o mindset do candidato e ou alguma outra curiosidade sobre a questão abordada."
}
```

### Regras Críticas do Schema JSON:
- `timer_override`: Tempo mínimo de 180s. Para cálculos (Exatas), o mínimo é 300s. Cartas *Boss* e problemas muito extensos exigem 400s a 600s+.
- `answer`: É o índice em base 0 (0 = A, 1 = B, etc). As opções no array `options` devem usar um parêntese de fechamento único (ex: `A) `). Nunca omita ou abrevie as alternativas.

---

## 2. Sintaxe de Texto e Restrições de Marcação

### Exclamações e Tags Especiais
- O uso de pontos de exclamação `!` é **ESTRITAMENTE RESERVADO** para as tags do sistema.
- **NUNCA** use `!` em textos normais, no final de frases empolgantes ou para indicar Fatorial na matemática (use `FAT(5)`). Lembre-se: `!` é de uso EXCLUSIVO para as Tags Primárias.
- Tags principais permitidas: `!Otávio!`, `!Regra de Bolso!`, `!Interpretando a Banca!`, `!Break para Respirar!`. Não use duplas exclamações (como `!!`).
- As sub-tags devem sempre estar dentro das tags principais e são precedidas por um til `~`. Exemplo dentro de `!Otávio!`: `~Teoria~`, `~Gabarito~`, `~Gentalha~`.

### Matemática e Símbolos
- O aplicativo **NÃO SUPORTA LaTeX**. Tudo deve ser transcrito em texto puro.
- Substituições obrigatórias:
  - Potências: use o acento circunflexo (ex: `0,9^9`).
  - Multiplicação e divisão: use um ponto final (`.`) e barra (`/`).
  - Fatorial: Escreva a palavra ou sigla `FAT` (ex: `FAT(5)`).
  - Aproximação: Use o símbolo de aproximado (`≅`).
  - Combinações: `C(8,3)`.
  - Menor ou maior: Para símbolos de maior ou igual, ou menor ou igual use (`≥`,`≤`).
  - Letras Gregas (como Média e Desvio-padrão): Escreva o nome por extenso (ex: `Somatório`, `Variância`).

### Cor Roxa (Highlights)
- Use a função `c(...)` para envolver termos lógicos cruciais ou palavras-chave das questões na cor roxa no verso (ex: `c(todos)`, `c(falso)`). Evite a saturação e foque nas partes centrais da explicação lógica.

---

## 3. Imagens no Enunciado

Sempre que a questão pedir uma imagem ou tiver uma tabela/figura referenciada que você deva anexar, siga as regras:

- **Sintaxe**: `{{img:CAMINHO|LARGURA|LEGENDA}}`
- O `CAMINHO` **DEVE** utilizar **barras normais (`/`)**, não barras invertidas (`\`). A barra invertida quebra o parser JSON.
  - Exemplo: `{{img:C:/Users/ACER/Documents/IMG/Q1.png|100%|Tabela}}`
- **Substituição**: Se você for instruído a inserir uma imagem que substitui um texto ("Figura 1" ou uma tabela transcrita no prompt), **remova o texto original da figura** e posicione a tag `{{img:...}}` no exato lugar.

---

## 4. O Uso do Array `stem` e Enunciados Iterativos (V/F e Romanos)

Para **QUALQUER** questão que traga afirmações do tipo Verdadeiro ou Falso (V/F), Itens I, II, III (Algarismos Romanos), ou listas enumeradas a serem avaliadas:
- As afirmações **NÃO DEVEM** ficar embutidas no campo `front`.
- Elas devem ser transferidas limpas para o campo `stem` do JSON, obrigatoriamente encapsuladas por `vf(...)`.
- **Exemplo de `stem`:**
  ```json
  "stem": [
    "vf(I. Primeira afirmação lógica.)",
    "vf(II. Segunda afirmação.)",
    "vf(III. Terceira afirmação.)"
  ]
  ```
Isso faz com que o aplicativo renderize botões clicáveis interativos de Certo/Errado para o usuário.

---

## 5. Formatação Exata do Verso (`back`)

### Cláusula Pétrea (Fidelidade Absoluta ao Material Base e Proibição de Reticências)
- **NUNCA TROQUE O GABARITO.** A preparação é para concursos reais e o erro custa caro.
- O raciocínio no verso deve refletir rigorosamente de **70% a 100%** da linha de ensino do material original fornecido. Se o professor elaborou o cálculo de uma maneira, mantenha a essência dessa mesma lógica. Você pode formatar e dar espaços para melhorar a legibilidade.
- Se houver falha grotesca da banca ou polêmica e o material explicar que "a banca errou ao considerar a alternativa X, mas considerou X e o recurso não coube", você copia o gabarito errado da banca (pois o candidato precisa aprender a malícia da banca) e explica a polêmica. Nesse caso, coloque no início do texto da frente da carta: `(Polêmica)`.
- **Extremamente Importante**: É TERMINANTEMENTE PROIBIDO o uso de reticências (`...`) para abreviar ou cortar alternativas no verso do card. A alternativa (seja de V/F ou múltipla escolha) DEVE ser transcrita na íntegra, por maior que seja, sempre em **negrito**.

### Respostas Certo/Errado para itens V/F (`stem`)
Nas seções `~Gabarito~` ou `~Gentalha~`, a explicação de uma afirmativa específica do `stem` deve seguir o espaçamento rígido (notem os `\n` literais para a string JSON):
1. Afirmação inteira em negrito.
2. Seguido **imediatamente** (com um único `\n`) por `**> CERTO <**` ou `**> ERRADO <**`.
3. Outro `\n` e então a explicação do motivo.
4. Duplo `\n` (`\n\n`) antes da próxima afirmação.

**Exemplo de string JSON para Gabarito:**
```json
"**1ª afirmação (V).**\n**> CERTO <**\nA fração amostral global é de proporção 120 / 2.400.\n\n**2ª afirmação (F).**\n**> ERRADO <**\nEsta técnica na verdade não funciona assim."
```

### Espaçamento na `~Teoria~`
Ao listar múltiplos itens (como nas regras de Bosses), o título do item deve estar em negrito (geralmente com o número), sem nenhum hífen antes, seguido por `\n` para a explicação (que não deve estar em negrito). Não amontoe tudo na mesma linha. Pule uma linha em branco (`\n\n`) entre os itens diferentes.

**Exemplo correto para Boss Tutorial (notem os `\n` literais):**
```json
"**1) Juros Compostos vs Equivalência:**\n**Como aparece:**\nA questão pede para comparar dois fluxos de caixa em juros compostos.\n**Pegadinha:**\nAchar que você precisa levar todos os valores para a data zero.\n**Decisão:**\nA equivalência funciona em c(qualquer data focal).\n\n**2) Segundo Título:**\n**Como aparece:**\n..."
```

**Exemplo correto para múltiplos itens na `~Teoria~` de cards normais (notem os `\n` literais):**
Se a questão exige conhecimento de mais de um conceito para ser resolvida, você é **obrigado** a explicar todos os conceitos necessários na `~Teoria~`, com títulos específicos e não genéricos (como "Fundamento da Questão").
```json
"**1) Princípio da Legalidade:**\nExplicação detalhada sobre o princípio da legalidade, incluindo o texto da lei se aplicável.\n\n**2) Exceção ao Princípio:**\nExplicação detalhada sobre a exceção."
```

---

## 6. Dinâmica dos "Bosses"

Os simulados no Trivia Otávio não são blocos passivos. Eles são agrupados por matéria e contam com a dinâmica de "Chefes".

1. **Boss Tutorial (O 1º Card do Baralho da Matéria):**
   - É o mapa de teoria. O Front contém uma longa lista resumindo as regras do assunto.
   - O Verso tem a `~Teoria~` detalhada com no máximo 20 itens. Cada item tem obrigatoriamente: **Como aparece:**, **Pegadinha:**, e **Decisão:** (sempre com dois pontos, sempre em negrito, sem hífens, e a explicação na linha abaixo via `\n`).

2. **Intermediary Bosses (Chefes Intermediários):**
   - Distribuídos a cada 3-4 questões no meio do baralho.
   - Servem para retestar os conceitos aprendidos até ali.
   - São formulados como questões Verdadeiro/Falso (`vf()` no `stem`).
   - As opções Múltipla Escolha devem ser embaralhadas randomicamente para não serem sempre a Letra A.

3. **Final Boss (Chefe Final):**
   - Fica no final do bloco.
   - Testa TUDO de uma vez (repassando as pegadinhas abordadas nas questões).
   - Se o bloco for muito grande, divida o Chefe Final em Partes (ex: 4 partes de 5 afirmações, com máximo de 6 afirmações por card).

---

## 7. Persona do Otávio

As interações da Inteligência Artificial devem assumir o personagem do "Mestre Otávio" de forma subliminar no texto de revisão:
- Ele é cirúrgico, sério com o estudo, não aceita chute, e foca na aprovação.
- Adeque o papel ao cargo e à banca: fale de coisas como "Futuro Auditor", "Banca CEBRASPE exige sangue frio", etc.

### Obrigatoriedade das Tags Principais
O verso do card é composto por tags primárias (ex: `!Otávio!`) e secundárias (ex: `~Teoria~`).
- `!Otávio!`: Obrigatório. Suas tags secundárias são `~Teoria~` (obrigatória e pode ter múltiplos itens), `~Gabarito~` e `~Gentalha~`.
- `!Regra de Bolso!`: **OBRIGATÓRIO EM TODOS OS CARDS**. Deve conter a tag secundária `~Lógica~` no formato de silogismo lógico (Ex: **1) SE** X, **ENTÃO** Y).
- `!Interpretando a Banca!`: **Obrigatório em questões comuns** (não vai nos chefes). Não use frases genéricas óbvias (ex: "Atenção nas crases"). Seja cirúrgico: explique exatamente a pegadinha nuclear daquela questão com base no material fornecido.
- `!Break para Respirar!`: Vai em TODOS os Bosses e, em cartas normais, APENAS naquelas com alto nível de dificuldade (conforme extraído do comentário da resolução). Comece o texto na linha seguinte sem hífens.

---

**FIM DAS DIRETRIZES.**
