# Backlog de Desenvolvimento - Trivia Otávio (App)

## 📝 1. Renderização de Texto, Markdown e Marcações
- [ ] **Desacoplar o caractere de exclamação (`!`) das Tags Primárias:** Criar uma nova lógica (preferencialmente via JSON estruturado, ver seção 4) para identificar tags, permitindo o uso livre de `!` como pontuação (interjeições, fatorial) sem quebrar o texto.
- [ ] **Implementar Suporte a LaTeX:** Adicionar biblioteca de renderização LaTeX (ex: KaTeX ou MathJax) para suportar notações matemáticas e de exatas complexas dentro das questões e explicações.
- [ ] **Corrigir Regex/Parser da marcação "Pintar de Roxo" (`c(...)`):** A lógica atual quebra quando há parênteses aninhados (ex: digressões dentro do texto roxo). Alterar a mecânica de captura para suportar parênteses internos sem fechar o bloco de cor prematuramente.
- [ ] **Isolamento de Bloco `Stem`:** Criar mecânica de fechamento do bloco Stem. O aplicativo deve permitir a seguinte estrutura contínua: `[Enunciado Normal] -> [Abertura do Stem] -> [Fechamento do Stem] -> [Continuação do Enunciado Normal]`. Atualmente, tudo após o Stem fica preso dentro dele.

## 🖼️ 2. Regras de Inserção de Imagens
- [ ] **Definição de Escala de Imagem:** Estabelecer que sempre que a IA gerar/inserir uma imagem no card (front ou back), um parâmetro de tamanho deve ser definido (de `70%` a `100%`). Se não for especificado pelo gerador, o aplicativo deve aplicar o `width` padrão de `70%`.

## 🖱️ 3. Interação com Alternativas (Mouse)
- [ ] **Ciclo de Estados com Botão Direito:** Manter os botões atuais (Alfinete/Azul e Tesoura/Vermelho), mas adicionar um Event Listener de clique direito (`contextmenu`) diretamente sobre a alternativa.
- [ ] **Lógica do Ciclo:** 
  - Estado 0 (Neutro) -> `Right Click` -> Estado 1 (Vermelho / Errado)
  - Estado 1 (Vermelho) -> `Right Click` -> Estado 2 (Azul / Certo)
  - Estado 2 (Azul) -> `Right Click` -> Estado 0 (Neutro)
- [ ] **Sincronização de Estado:** O estado do botão direito deve ler e respeitar o estado atual definido pelos botões pequenos (se o usuário usou a tesoura e ficou vermelho, o próximo clique direito deve ir para o azul).

## ✏️ 4. Ferramenta de Rascunho / Riscador (Canvas)
- [ ] **Correção da Área Útil (Hitbox do Canvas):** Expandir a área riscável para 100% do interior da `div` do enunciado. Atualmente, há uma "margem morta" de ~10% próxima às bordas onde o risco não é processado.
- [ ] **Correção de Coordenadas no "Consultar Texto":** Ao consultar um texto base em uma questão filha, os riscos feitos anteriormente carregam desajustados (ex: acima da palavra). Corrigir o mapeamento do Canvas/Viewport para que as marcações preservem as coordenadas exatas relativas ao texto.
- [ ] **Nova Ferramenta - Caixa de Texto:** Adicionar um ícone de "T" na barra de ferramentas superior do rascunho. Permitir que o usuário clique no canvas e digite textos. 
- [ ] **Isolamento de Camadas (Texto vs. Desenho):** Garantir que a camada de desenho (caneta/borracha) e a camada de texto coexistam independentes. A borracha não deve apagar o texto digitado e um não deve sobrepor destrutivamente o outro.
- [ ] **Paginação do Rascunho:**
  - Adicionar um botão `[+ Página]` para criar novas folhas de rascunho em branco.
  - Adicionar indicador de página atual semi-transparente no canto da tela (ex: `1`, `2`).
  - Adicionar setas de navegação (`<-` e `->`) para transitar entre as páginas criadas.

---

## 🏗️ 5. [BLOCO ISOLADO] Refatoração da Estrutura JSON

*(Nota para o Cursor: Esta task altera a arquitetura de como os dados são lidos pelo front-end e resolve conflitos de caracteres especiais na formatação do texto).*

- [ ] **Migrar marcações de metadados do texto bruto para propriedades JSON nativas:** Remover a dependência de caracteres como `!`, `~`, `**` para definir funções de negócio (Tags). O aplicativo deve ler a formatação via propriedades estruturadas.
- [ ] **Nova Estrutura Recomendada para o `back` (Verso do Card):**
  Implementar lógica de aninhamento (Objetos e Arrays) para definir a hierarquia de tags. 
  
  **Exemplo de como o JSON deverá ser gerado e lido:**
  ```json
  "back": {
    "timer_override": 120,
    "tags": [
      {
        "primaria": "Otávio",
        "secundarias": ["teoria", "prática"]
      },
      {
        "primaria": "Matemática",
        "secundarias": ["geometria"]
      }
    ],
    "conteudo": "Aqui entra o texto normal, podendo usar ! e ~ livremente sem bugar o código. Se tiver equação no meio $x^2 = 4$, tudo bem."
  }
  ```
- [ ] **Automatização de Espaçamentos de Tags na UI:** 
  O aplicativo deve ler os arrays acima e renderizar as tags na tela aplicando as regras de CSS (Margin/Padding) automaticamente:
  - 1 linha de espaçamento entre a Tag Primária e sua primeira Tag Secundária.
  - 2 linhas de espaçamento entre uma Tag Secundária e outra.
  - 2 linhas de espaçamento onde termina um grupo de tags e começa uma nova Tag Primária.