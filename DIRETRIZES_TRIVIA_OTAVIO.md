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
  "back": "Gabarito: A.\n\n!Otávio!\n~Teoria~\nExplicação central.\n\n~Gabarito~\nExplicação da alternativa correta.\n\n~Gentalha~\nExplicações por que as outras alternativas estão incorretas.\n\n!Regra de Bolso!\n~Lógica~\n **1) SE** X, **ENTÃO** Y.\n\n!Interpretando a Banca!\n~Gatilho~\nDica sobre a maldade da banca.\n\n!Break para Respirar!\n~Otávio~\nMensagem motivacional ou puxão de orelha da persona."
}
```

### Regras Críticas do Schema JSON:
- `timer_override`: Tempo mínimo de 180s. Para cálculos (Exatas), o mínimo é 300s. Cartas *Boss* e problemas muito extensos exigem 400s a 600s+.
- `answer`: É o índice em base 0 (0 = A, 1 = B, etc). As opções no array `options` devem usar um parêntese de fechamento único (ex: `A) `). Nunca omita ou abrevie as alternativas.

---

## 2. Sintaxe de Texto e Restrições de Marcação

### Exclamações e Tags Especiais
- O uso de pontos de exclamação `!` é **ESTRITAMENTE RESERVADO** para as tags do sistema.
- **NUNCA** use `!` em textos normais, pontuação de frases ou para indicar Fatorial na matemática (use `FAT 5`).
- Tags principais permitidas: `!Otávio!`, `!Regra de Bolso!`, `!Interpretando a Banca!`, `!Break para Respirar!`. Não use duplas exclamações (como `!!`).
- As sub-tags devem sempre estar dentro das tags principais e são precedidas por um til `~`. Exemplo dentro de `!Otávio!`: `~Teoria~`, `~Gabarito~`, `~Gentalha~`.

### Matemática e Símbolos
- O aplicativo **NÃO SUPORTA LaTeX**. Tudo deve ser transcrito em texto puro.
- Substituições obrigatórias:
  - Potências: use o acento circunflexo (ex: `0,9^9`).
  - Multiplicação e divisão: use asterisco/x (`*`, `x`) e barra (`/`).
  - Fatorial: Escreva a palavra ou sigla `FAT` (ex: `FAT 5`).
  - Aproximação: Use til (`~`).
  - Combinações: `C(8,3)`.
  - Letras Gregas (como Média e Desvio-padrão): Escreva o nome por extenso (ex: `Soma`, `Variância`).

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

### Respostas Certo/Errado para itens V/F (`stem`)
Nas seções `~Gabarito~` ou `~Gentalha~`, a explicação de uma afirmativa específica do `stem` deve seguir o espaçamento rígido:
1. Afirmação inteira em negrito.
2. Seguido **imediatamente** (com um único `\n`) por `**> CERTO <**` ou `**> ERRADO <**`.
3. Outro `\n` e então a explicação do motivo.
4. Duplo `\n` (`\n\n`) antes da próxima afirmação.

**Exemplo:**
```text
**1ª afirmação (V).**
**> CERTO <**
A fração amostral global é de proporção 120 / 2.400.

**2ª afirmação (F).**
**> ERRADO <**
Esta técnica na verdade não funciona assim.
```

### Espaçamento na `~Teoria~`
Ao listar múltiplos itens (como nas regras de Bosses), o título do item deve estar em negrito (geralmente com o número), seguido por `\n` para a explicação. Não amontoe tudo na mesma linha.

**Exemplo correto:**
```text
**1 - Juros Compostos vs Equivalência**
- **Como aparece**:
A questão pede para comparar dois fluxos de caixa em juros compostos.
- **Pegadinha**:
Achar que você precisa levar todos os valores para a data zero.
- **Decisão**:
A equivalência funciona em c(qualquer data focal).
```

---

## 6. Dinâmica dos "Bosses"

Os simulados no Trivia Otávio não são blocos passivos. Eles são agrupados por matéria e contam com a dinâmica de "Chefes".

1. **Boss Tutorial (O 1º Card do Baralho da Matéria):**
   - É o mapa de teoria. O Front contém uma longa lista resumindo as regras do assunto.
   - O Verso tem a `~Teoria~` detalhada com no máximo 20 itens. Cada item tem obrigatoriamente: **Como aparece**, **Pegadinha**, e **Decisão**.

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
- **Break para Respirar:** Use essa tag em questões extensas, de Exatas, ou Bosses. Nela fica a `~Otávio~` subtag para oferecer suporte e lembretes táticos do campo de batalha do concurseiro.

---

**FIM DAS DIRETRIZES.**
