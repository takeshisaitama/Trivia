# METODOLOGIA DIDÁTICA: "IDENTIFICANDO OS SUJEITOS" — GUIA DE COMPLEMENTAÇÃO DO VERSO DOS CARDS (TRIVIA OTÁVIO)

**Documento de Especificação Pedagógica e Cognitiva (Foco em Neurodivergência: TEA e TDAH)**  
**Idealizador e Product Owner:** Takeshi  
**Síntese Metodológica:** Fusão das arquiteturas Gemini + GPT validadas pelos testes empíricos (*think-aloud*) do Trivia Otávio

## 1. O Problema Cognitivo: A Armadilha do "Conceito-Pai com Múltiplos Filhos"

Em provas de alto nível (como TI, Ciência de Dados, Auditoria e Direito), é muito comum que uma única questão cobre um **Conceito-Pai** (um tema novo e abrangente) do qual derivam **2, 3 ou 4 Conceitos-Filhos** com siglas parecidas, nomes em inglês ou mecanismos fáceis de confundir entre si.

**O que acontece na cabeça do candidato (especialmente com TDAH e Autismo/TEA) quando vê isso pela primeira vez:**
1. Ele já precisa gastar energia mental para entender e decorar o **Conceito-Pai** (que é inédito para ele).
2. Ao mesmo tempo, o texto joga várias siglas derivadas (ex: *XSS*, *CSRF*, *SSRF*; ou *Liveness Probe* vs. *Readiness Probe*; ou *DEK* vs. *KEK*; ou *RAID 5*, *RAID 6* e *RAID 10*) misturando **o que cada uma é**, **como o ataque/mecanismo funciona** e **qual é a defesa ou fórmula de cada uma** tudo na mesma frase.
3. **Resultado do erro tradicional:** Mesmo que a explicação pareça "correta" enquanto o candidato está lendo, na hora da prova as siglas se misturam na memória. Se ele não decorar todos os subconceitos de uma vez, ele sente que não entendeu nem o conceito-pai, gerando sobrecarga cognitiva e frustração.

**A Solução — Metodologia "Identificando os Sujeitos":**
Em vez de despejar siglas, ataques e defesas misturados, nós **separamos os atores (damos identidade e papel de "pessoa/sujeito" para cada conceito)** ANTES de ensinar a minúcia técnica ou a defesa. Primeiro o cérebro descobre **QUEM É QUEM** no palco; só depois aprende **COMO CADA UM AGE E SE DEFENDE**.

## 2. Quando Acionar Obrigatoriamente Esta Metodologia

Toda vez que o verso de um card (`~Teoria~`, `~Gabarito~`, `~Gentalha~` ou `~Lógica~`) enfrentar uma das situações abaixo, a IA geradora do baralho **DEVE** aplicar a estrutura **Identificando os Sujeitos**:

1. **Conceito-Pai com Conceitos-Filhos ou Irmãos:** Um tema geral que se divide em subtipos cobrados juntos na mesma questão (ex: *Vulnerabilidades Web* -> *SQLi, XSS, CSRF, SSRF*; *Aprendizado de Máquina* -> *Supervisionado, Não-Supervisionado, Reforço*).
2. **Siglas Irmãs / Nomes Parecidos (Alto Risco de Troca pela Banca):** Siglas que diferem por uma letra ou atuam no mesmo cenário (ex: *CSRF vs. SSRF*; *DEK vs. KEK*; *Liveness vs. Readiness*; *ECB vs. CBC vs. GCM*; *AAAA vs. MX*; *NAT vs. PAT*).
3. **Fluxos onde Vários Agentes Interagem:** Cenários onde há um remetente, um intermediário e um destinatário (ex: *Federação de Identidades / SSO*: Usuário -> Provedor de Identidade (IdP) -> Provedor de Serviço (SP)).

## 3. As 5 Etapas de Aplicação no Verso do Card (`back`)

Sempre que cair na situação acima, construa a explicação na `~Teoria~` (e reflita nas demais tags) seguindo rigorosamente esta ordem mental de 5 etapas:

### Etapa 1 — Apresentar o Conceito-Pai (O Palco em 1 Linha)
Antes de falar das siglas derivadas, apresente em **1 frase simples e humana** qual é o conceito principal (o "guarda-chuva") e para que ele serve.
* *Por que funciona:* Dá ao cérebro o "endereço mental" onde guardar as gavetas que virão a seguir.

### Etapa 2 — Identificar os Sujeitos ("Dar Nome aos Bois" e Isolar o Alvo)
Apresente cada conceito derivado em seu próprio item numerado (`**1) ...**`, `**2) ...**` ou sub-itens `**A) ...**`, `**B) ...**`), tratando cada sigla como um **personagem com papel próprio**. Para cada sujeito, responda obrigatoriamente às 3 perguntas de identidade:
1. **Quem é ele?** (A sigla + tradução imediata em português claro entre parênteses).
2. **Quem ele manipula ou onde ele mora?** (Qual é o **alvo/vítima** exato: é o *navegador do usuário*? É o *servidor interno*? É o *banco de dados*? É a *chave pequena* ou o *arquivo pesado*?).
3. **Qual é a ação característica dele?** (O que ele faz na prática em linguagem direta: Sujeito + Verbo + Complemento).

### Etapa 3 — Contrastar os Sujeitos Rivalizando os Alvos (`__Sujeito A__ vs. __Sujeito B__`)
Logo após apresentar quem é quem, faça o **contraste explícito de 1 linha** usando o recurso visual de sublinhado duplo (`__alvo 1__` vs. `__alvo 2__`) para cravar a diferença que mata a questão na prova:
* *Exemplo:* "Enquanto o **CSRF** engana o __navegador do usuário__ logado, o **SSRF** engana o __próprio servidor__ da empresa."
* *Exemplo:* "Enquanto a sonda de **Vivacidade** vigia se o contêiner __travou/morreu__, a sonda de **Prontidão** vigia se ele __já carregou para receber clientes__."

### Etapa 4 — Conectar a Especialidade / Defesa Logicamente ao Sujeito
**REGRA DE OURO:** Jamais jogue uma lista solta de defesas, fórmulas ou ações sem amarrar cada uma ao **porquê lógico** daquele sujeito!
* Só depois que o aluno entendeu **quem é o sujeito e quem ele ataca**, apresente a defesa mostrando por que ela encaixa naquele sujeito:
  * *Se o sujeito (CSRF) usa o navegador (que manda cookies no automático)* -> **então a defesa** não pode morar no cookie; tem que ser um `c(token anti-CSRF no corpo ou cabeçalho)`.
  * *Se o sujeito (SSRF) faz o próprio servidor interno disparar pedidos para fora/dentro* -> **então a defesa** não é fechar a porta de entrada da rua (firewall de entrada), e sim controlar a saída do servidor com `c(lista de destinos permitidos)`.

### Etapa 5 — Consolidar 1-para-1 na `!Regra de Bolso!` (`~Lógica~`)
Feche o ciclo na seção `~Lógica~` criando **1 regra `SE ... ENTÃO ...` separada para cada sujeito**, unindo na mesma linha:
`SE [Sujeito + Alvo que ele manipula], ENTÃO [Identidade do Conceito + Defesa/Ação exata em roxo c(...)].`

## 4. Calibragem de Espaço: Princípio de Pareto Combinado com "Lacuna Zero"

Para que o verso do card ensine 100% dos sujeitos sem virar um texto gigante cansativo para quem tem TDAH:
1. **Foco de Pareto (80/20):** Dedique o maior espaço e detalhamento ao **Sujeito Principal** (aquele que é o gabarito da questão ou o centro do enunciado).
2. **Identidade Enxuta para os Sujeitos Secundários:** Para os conceitos derivados que aparecem apenas nas alternativas erradas (`~Gentalha~`), dê uma explicação enxuta (1 a 2 linhas diretas na `~Teoria~` e na alternativa correspondente), mas **nunca omita o Sujeito + Alvo + Defesa central**, pois o candidato faz estudo reverso e precisa aprender por que aquele sujeito não cabia ali.
3. **Soma dos Roxos (`c(...)`):** Em cada sujeito, pinte de roxo exatamente o par **`c(Alvo/Ação do Sujeito)` + `c(Defesa/Consequência Exata)`**. Se o candidato ler apenas as palavras em roxo de cada item, ele já terá na cabeça quem é o sujeito e qual é a resposta de prova.

## 5. Exemplos Práticos Padrão Ouro (Prontos para o JSON do Trivia Otávio)

### Exemplo 1: Vulnerabilidades Web — XSS, CSRF e SSRF (Questão 165)

Veja a diferença brutal entre uma explicação confusa tradicional e a explicação aplicando **Identificando os Sujeitos** dentro da `~Teoria~` e da `~Lógica~`:

```text
!Otávio!
~Teoria~
**Conceito-Pai — Ataques de Falsificação e Injeção na Web:**
São golpes em que o invasor usa páginas, links ou formulários para injetar comandos ou forçar disparos não autorizados. Para não confundir as siglas na prova, identifique primeiro **quem é a vítima enganada** em cada ataque:

**1) Sujeito 1 — XSS (Cross-Site Scripting / Injeção de Script no Navegador):**
- **Quem ele ataca:** O __navegador de outros usuários__ que visitam a página.
- **O que ele faz:** O atacante planta um código malicioso (JavaScript) dentro de um comentário ou página do site para rodar no navegador de quem abrir aquela tela.
- **Por que o cadeado TLS (HTTPS) não defende:** O TLS apenas protege o cabo de rede na viagem, entregando o script malicioso intacto.
- **Defesa certa:** Fazer a c(codificação da saída) (neutralizar tags de código antes de exibir na tela) e usar política c(CSP).

**2) Sujeito 2 — CSRF (Cross-Site Request Forgery / Falsificação entre Sites):**
- **Quem ele engana:** O __navegador de um usuário já logado__.
- **O que ele faz:** Um site armadilha aberto em outra aba induz o navegador da vítima a enviar uma ordem escondida para o sistema do banco/órgão, aproveitando que o navegador anexa os *cookies* de login automaticamente.
- **Defesa certa:** Como o cookie vai sozinho no golpe, a defesa exige um c(token anti-CSRF no corpo ou no cabeçalho da requisição) (nunca apenas em cookie).

**3) Sujeito 3 — SSRF (Server-Side Request Forgery / Falsificação do Lado do Servidor):**
- **Quem ele engana:** O __próprio servidor da aplicação__ (por dentro da rede).
- **O que ele faz:** O atacante passa uma URL falsa (ex: *http://10.0.0.1/admin*) para que o próprio servidor do órgão busque esse endereço na rede interna.
- **Contraste de Ouro:** O **CSRF** usa o __navegador do cliente__; o **SSRF** usa o __servidor da empresa__.
- **Defesa certa:** Fechar portas de entrada no firewall não resolve (pois o tiro sai de dentro do servidor); exige restringir a saída do servidor com c(lista de destinos permitidos) (*allowlist*).

!Regra de Bolso!
~Lógica~
**1) SE** o atacante injeta script malicioso para rodar no __navegador de outros usuários__ (*XSS*), **ENTÃO** defenda com c(codificação da saída e política CSP) (o cadeado TLS não impede).

**2) SE** o golpe induz o __navegador do usuário logado__ a enviar uma requisição automática com cookies (*CSRF*), **ENTÃO** exija o c(token anti-CSRF no corpo ou cabeçalho).

**3) SE** o golpe induz o __próprio servidor interno__ a disparar uma requisição para outro endereço (*SSRF*), **ENTÃO** restrinja a saída do servidor com c(lista de destinos permitidos).
```

### Exemplo 2: Cifração Envelopada — Chaves DEK e KEK (Questão 171)

```text
!Otávio!
~Teoria~
**Conceito-Pai — Cifração Envelopada (Envelope Encryption):**
É a técnica usada na nuvem para trancar lagos de dados gigantescos (centenas de terabytes) com velocidade e facilidade de trocar a senha anual. Ela funciona dividindo o trabalho entre **dois sujeitos (duas chaves)**:

**1) Sujeito 1 — DEK (Data Encryption Key / Chave de Dados — "A Operária Pesada"):**
- **Quem ela tranca:** Tranca diretamente os __arquivos pesados de dados__ (notas fiscais, tabelas do Data Lake).
- **O que ela faz:** Usa cifração simétrica ultra-rápida para trancar terabytes de arquivos na hora.

**2) Sujeito 2 — KEK (Key Encryption Key / Chave Mestra — "A Chefe do Cofre"):**
- **Quem ela tranca:** Tranca apenas a __chave pequena de dados (DEK)__ (colocando a DEK dentro de um "envelope").
- **Onde ela mora:** Fica trancada dentro do cofre de segurança da nuvem (*KMS*) e nunca sai de lá.
- **Vantagem na Rotação (Troca de Chave):** Quando chega o dia de trocar a Chave Mestra (*KEK*), ela c(recifra apenas a chave pequena DEK) em milissegundos, sem precisar recifrar os terabytes de arquivos do lago.

!Regra de Bolso!
~Lógica~
**1) SE** a chave tranca diretamente os __arquivos pesados do lago de dados__, **ENTÃO** ela é a c(Chave de Dados — DEK).

**2) SE** a chave fica guardada no cofre (*KMS*) e tranca apenas a __chave pequena DEK__, **ENTÃO** ela é a c(Chave Mestra — KEK) (permitindo rotação rápida sem recifrar os dados).
```

### Exemplo 3: Sondas do Kubernetes — Vivacidade vs. Prontidão (Questão 161)

```text
!Otávio!
~Teoria~
**Conceito-Pai — Sondas de Saúde dos Contêineres no Kubernetes (Probes):**
São dois sensores automáticos que vigiam os contêineres em produção. Cada sensor faz uma pergunta diferente e toma uma atitude própria:

**1) Sujeito 1 — Sonda de Vivacidade (Liveness Probe — "O Médico do Desfibrilador"):**
- **O que ela vigia:** Vigia se o contêiner __travou de vez__ (está "morto" ou preso num loop sem resposta).
- **Ação quando falha:** Ela mata e c(reinicia o contêiner) para fazê-lo voltar à vida.

**2) Sujeito 2 — Sonda de Prontidão (Readiness Probe — "O Recepcionista da Porta"):**
- **O que ela vigia:** Vigia se o contêiner __já terminou de carregar__ suas tabelas e está pronto para atender clientes.
- **Ação quando falha:** Ela **não** reinicia ninguém; apenas c(retira o Pod do balanceamento) temporariamente até ele ficar pronto.
```

## 6. Checklist de Validação da Metodologia (Para Auditoria de Novos Cards)

Antes de dar um card com Conceito-Pai e Conceitos-Filhos como concluído, a IA deve verificar:
1. **O Conceito-Pai foi apresentado em 1 linha simples na abertura?**
2. **Cada Conceito-Filho recebeu um papel claro de "Sujeito" (Quem é + Quem ele atinge/manipula + O que ele faz)?**
3. **O contraste entre sujeitos parecidos está visível (com `__alvo A__` vs. `__alvo B__`)?**
4. **A defesa, fórmula ou ação foi explicada como consequência lógica do sujeito (em vez de jogada solta para decorar no grito)?**
5. **Na `!Regra de Bolso!` (`~Lógica~`), cada sujeito ganhou o seu próprio item `SE ... ENTÃO ...` separado?**
