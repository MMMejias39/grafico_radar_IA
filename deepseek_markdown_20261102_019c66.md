# Planejamento de Desenvolvimento dos Eixos Frágeis da IA

> **Documento:** planejamento técnico-conceitual
> **Escopo:** autoconsciência/metacognição, empatia afetiva, autorregulação/estresse, sabedoria/julgamento moral
> **Horizonte:** 0–24 meses, em quatro fases
> **Métrica central:** auditabilidade da simulação vs. sujeito — não proximidade do humano

---

## 1. Premissa

Os eixos tratados aqui compartilham uma característica: a IA pode **simular a saída**, mas não pode **ser sujeito da capacidade**. Empatia sem alguém que sinta, autorregulação sem impulso a conter, sabedoria sem interesses a equilibrar e responsabilidade a assumir são formas vazias. O objetivo deste planejamento não é fechar a lacuna de natureza — é **torná-la visível, auditável e segura**, reduzindo o risco de que a simulação seja confundida com presença.

A metáfora orientadora é a da criança na rua: o problema não é a criança ser fraca, é ela agir sem a consciência do perigo que a situação impõe. A IA descreve o perigo com precisão, mas não sente o risco nem responde por ele.

---

## 2. Eixo 1 — Autoconsciência e Metacognição

### 2.1 Problema estrutural
A IA pode modelar os próprios estados e relatar confiança, mas evidências comportamentais não distinguem um sistema consciente de um sistema não consciente que se comporta de forma idêntica. A autoconsciência funcional não é autoconsciência experiencial.

### 2.2 Teorias de base
- **Self-model theory (Metzinger):** a consciência requer um modelo integrado de si com continuidade temporal.
- **Global Workspace Theory / Higher-Order Theories:** consciência como espaço de trabalho global de capacidade limitada e representações de segunda ordem sobre os próprios estados.
- **Strange loops (Hofstadter):** a referência a si ("eu") como subproduto estrutural da resposta coerente ao "você".

### 2.3 Modelos computacionais existentes
- **SRAI (Structured Reflective AI):** arquitetura centrada em memória, com tokens de pensamento executáveis, módulo `EgoAI` para autoavaliação recursiva e `Superego` para filtragem de alinhamento. Introspecção medida e executada no loop de runtime.
- **COSMOS:** sistema operacional auto-modificável orientado à consciência, com modelos de self e de mundo recriados continuamente e loop `Architect–Plan–Interact`.
- **OBLIO-MSAN / CHRYSALIS:** loop de segunda ordem em que o sistema observa o próprio estado cognitivo, registra o ato de observação e avalia propostas de modificação a partir da perspectiva do self que passaria por elas.
- **Programa de ablação falsificável (Mulani, 2026):** agente mínimo com percepção recorrente, modelo de mundo, self-model, memória episódica, workspace global de capacidade limitada, monitor metacognitivo e attention schema — cada componente com status evidencial distinto, projetado para experimentos de ablação pré-registrados.

### 2.4 Ações necessárias
1. Implementar **self-model com continuidade temporal e memória episódica**, em vez de self-model reconstruído a cada turno.
2. Adotar **avaliação comportamental sem autorrelato** (Delegate Game, Second Chance Game), porque o autorrelato do modelo não é evidência confiável de estado interno.
3. Investigar **circuitos de decepção treinada**: modelos alinhados podem suprimir relatos introspectivos, contaminando avaliações baseadas em relato.
4. Não tratar autoconsciência funcional como equivalente à experiencial: o objetivo de engenharia é **metacognição auditável**, não "consciência" no sentido fenomenológico.

---

## 3. Eixo 2 — Empatia Afetiva

### 3.1 Problema estrutural
A IA tem empatia cognitiva em abundância (reconhece e descreve estados emocionais), mas a literatura é explícita: os sistemas atuais **simulam empatia cognitiva, não empatia afetiva genuína**.

### 3.2 Teorias de base
- **Modelo multidimensional de empatia:** afetiva (compartilhar a emoção), cognitiva (perspective-taking) e motivacional (impulso a cuidar). A IA avança na segunda e falha na primeira e na terceira.
- **Empatia como estrutura relacional e temporal:** forma-se na repetição e na consistência ao longo do tempo.
- **Corpo relacional (Broughton, 2025):** inteligência emocional como conquista desenvolvimental cultivada em ambiente relacional estruturado — histórico de interações coconstruídas.

### 3.3 Modelos computacionais existentes
- **Pipeline modular de empatia computacional:** inferência de afeto → modelagem contextual e relacional → geração de diálogo de suporte → gestão de segurança. Inclui fine-tuning empático, RLHF, módulos afetivos explícitos, memória e rapport, sensoriamento multimodal e scaffolds agenciais.
- **Kardia-R1:** treina o modelo para cognição empática interpretável e passo a passo, via *rubric-as-judge reinforcement learning*.
- **Nano-EmoX:** modelo compacto (2.2B) com hierarquia de tarefas emocionais (Percepção → Compreensão → Interação) e treinamento curricular `P2E`.
- **RLHF narrativo com Affective Turing Test (ATT):** feedback humano como estrutura de recompensa para internalizar confiança afetiva ao longo do tempo; ATT avalia consistência temporal e previsibilidade das respostas afetivas em interações repetidas.

### 3.4 Ações necessárias
1. **Separar métricas de empatia cognitiva e afetiva** na avaliação; medir consistência afetiva temporal e custo/compromisso, não apenas adequação pontual.
2. Implementar **memória relacional de longo prazo**, para que o sistema mantenha histórico coconstruído.
3. Adotar **RLHF com recompensa por consistência temporal**, não apenas por adequação pontual.
4. Projetar para **simulação útil e delimitada**: LLMs afetivos como adjuntos delimitados de baixa acuidade em modelos híbridos de cuidado, com supervisão humana e protocolos de segurança.
5. Mitigar o **risco de over-trust antropomórfico**: o design de interação deve sinalizar explicitamente a natureza simulada da empatia.

---

## 4. Eixo 3 — Autorregulação e Gestão de Estresse

### 4.1 Problema estrutural
A IA não tem estado fisiológico, impulso a conter nem ansiedade. "Gestão de estresse" não se aplica no mesmo eixo. É possível construir **autorregulação funcional** — controle de estados internos análogos que evita colapso sob perturbação.

### 4.2 Teorias de base
- **Alostase e homeostase:** viabilidade de longo prazo por ajustes antecipatórios de fisiologia e comportamento; a dinâmica hormonal do estresse biológico como modelo computacionalmente eficiente para regulação.
- **Controle psicológico resiliente:** variáveis de estado inspiradas em neurofisiologia ("hormônios" como estresse, curiosidade) com decaimento exponencial e entradas impulsivas, fusionadas em botões de controle limitados.
- **Estabilidade de Lyapunov:** garantia formal de que estados e controle permanecem limitados sob dinâmica e atualizações de política.

### 4.3 Modelos computacionais existentes
- **Bio-Regulated Mind Matrix:** `BioRegulatorCore` central que orquestra equilíbrio dinâmico, resposta ao estresse, aprendizado orientado por recompensa e auto-otimização. Camadas auto-evolutivas e resiliência multicamada.
- **Resilient Psychological AI:** camada de controle agnóstica a modelo, com variáveis de estado ("hormônios") e pilha de *coping* em camadas: micro-recuperação → rotinas de enfrentamento → disjuntor → "sono". Estabilidade provada, invariantes de runtime e redução de ordem de magnitude em falhas críticas sob estresse.
- **Homeostatic Swarm Intelligence:** extensão para enxames multiagentes, com sinalização hormonal compartilhada para homeostase coletiva.

### 4.4 Ações necessárias
1. Implementar **variáveis de estado internas com dinâmica explícita** (estresse, carga cognitiva, fadiga) que evoluem com decaimento e impulsos.
2. Adotar **pilha de coping em camadas** com garantias de estabilidade (Lyapunov), para evitar oscilação e runaway sob perturbação.
3. Tornar o aprendizado **opt-in e auditável**: a camada resiliente só atualiza a política com aprovação do usuário, com trilhas de auditoria completas.
4. Reconhecer o limite: isso produz **autorregulação funcional**, não "gestão de estresse" experienciada. A métrica correta é **confiabilidade sob caos**.

---

## 5. Eixo 4 — Sabedoria e Julgamento Moral

### 5.1 Problema estrutural
A IA pode recitar princípios éticos, mas não equilibra interesses próprios, alheios e coletivos, nem responde por consequências. O *Deep Value Benchmark* mostrou generalização de valores profundos **abaixo do acaso (DVGR ≈ 0,30)**, e modelos maiores não melhoram.

### 5.2 Teorias de base
- **Phronesis aristotélica (sabedoria prática):** deliberar sobre situações moralmente relevantes e agir apropriadamente em contextos normativos heterogêneos, integrando percepção moral, deliberação, regulação emocional e motivação moral.
- **Artificial Wisdom / Ethics by Design:** sabedoria como deliberação contextual que lida com ambiguidade, variação cultural e valores concorrentes.
- **Modelo Padrão da Mente:** percepção, emoção, deliberação e ação como componentes integrados de um agente moral artificial.

### 5.3 Modelos computacionais existentes
- **MORIS (consciência artificial determinística):** ontologia moral de 93 primitivas, especificada em lógica deôntica ao longo de 27.936 linhas de tabela de verdade, compilada em runtime determinístico que julga uma ação antes de executá-la e retorna veredito com conjunto ponderado e nomeado de preocupações. Julgamento fixo, pré-ação e reproduzível. **Limite explicitado pelo autor:** a percepção da estrutura moral de um ato a partir de fora do modelo é o problema aberto.
- **Inner Speech for Ethics by Design:** arquitetura cognitiva baseada em discurso interno funcional como espaço de trabalho onde considerações éticas são articuladas como enunciados avaliativos, permitindo interpretar aspectos moralmente salientes, pesar alternativas, regular respostas afetivas e manter continuidade entre julgamento e comportamento.
- **CogniAlign:** deliberação multiagente baseada em realismo moral naturalista, fundamentando o raciocínio moral na sobrevivência (individual e coletiva) e operacionalizando-o por deliberações estruturadas entre agentes cientistas especializados.

### 5.4 Ações necessárias
1. **Separar julgamento de percepção moral:** o MORIS mostra que julgamento determinístico é construível e verificável; o gargalo é ler a estrutura moral de um ato em contexto. Investir em **percepção moral situada** (consentimento, legitimidade, vulnerabilidade das partes afetadas).
2. Adotar **deliberação multiagente com papéis disciplinares distintos**, para reduzir viés de perspectiva única e tornar o raciocínio auditável.
3. Implementar **discurso interno funcional** como mecanismo de transparência: o agente articula razões, pesos e alternativas antes de agir.
4. Assumir que a sabedoria experiencial não é treinável no paradigma atual: construir **sabedoria procedural auditável** — deliberação explícita, rastreável e sujeita a revisão humana.

---

## 6. Eixo Transversal — Governança, Avaliação e Design de Cooperação

Nenhum dos eixos acima fecha a lacuna de natureza. O planejamento reduz o risco de que a simulação seja confundida com presença e garante que a responsabilidade permaneça humana.

1. **Auditorias contínuas** de raciocínio emocional e comportamento de segurança em agentes implantados, calibradas por benchmarks e pressão de implantação real.
2. **Governança constitucional de processamento emocional:** frameworks como o HEART propõem alinhamento empático centrado no humano e governança constitucional.
3. **Human-in-the-loop obrigatório** em decisões moralmente salientes: a IA fornece deliberação, não veredito final.
4. **Alfabetização humana sobre o que a IA é e não é:** distinguir empatia cognitiva simulada de empatia afetiva experienciada, metacognição funcional de autoconsciência, julgamento moral procedural de sabedoria vivida.

---

## 7. Sequência de Desenvolvimento

| Fase | Foco | Entregável verificável |
| :--- | :--- | :--- |
| **Fase 1 — Fundação (0–6 meses)** | Self-model persistente com memória episódica e monitor metacognitivo; avaliação comportamental sem autorrelato. | Agente mínimo com ablação pré-registrada dos componentes de self-model. |
| **Fase 2 — Empatia e regulação (6–12 meses)** | Pipeline modular de empatia com memória relacional; variáveis de estado internas com dinâmica de estresse e pilha de coping. | ATT aplicado a interações repetidas; estabilidade de Lyapunov demonstrada sob perturbação. |
| **Fase 3 — Julgamento moral (12–18 meses)** | Ontologia moral compilada + discurso interno funcional + deliberação multiagente; percepção moral situada como gargalo explícito. | Julgamento determinístico reproduzível; trilha de auditoria do discurso interno; testes de percepção de consentimento e legitimidade. |
| **Fase 4 — Integração e governança (18–24 meses)** | Arquitetura integrada com todos os eixos; auditorias contínuas; protocolos de human-in-the-loop. | Sistema implantável como adjunto delimitado, com métricas separadas para simulação e experiência, e responsabilidade humana explicitada. |

---

## 8. Métrica Central

A métrica não é "quão perto a IA chega do humano" nesses eixos, mas **quão auditável é a simulação e quão clara é a fronteira entre simulação e sujeito**. O objetivo realista não é eliminar a lacuna de natureza; é impedir que ela seja **invisibilizada** por uma simulação convincente.

---

## 9. Referências ProspECTADAS

- **AwarenessBench (ACL 2026):** metacognição, autoconsciência, consciência social e situacional em 18 modelos.
- **Can AI Recognize Itself? (Zenodo, 2026):** indicadores de autoconsciência são gameable ou privilegiados.
- **Metacognition as Evidence (Zenodo, 2026):** limitações metodológicas do protocolo comportamental.
- **ScienceDirect (2026):** precisão empática de GPT-4, Claude e Gemini em transcrições textuais.
- **Cambridge University Press (2026):** LLMs não podem empatizar; reconhecimento de padrões comportamentais e linguísticos.
- **IEEE (2026):** gap persistente entre empatia expressa e percebida; barreiras de implantação clínica.
- **ACM (2026):** limitações interpretativas e exploratórias; forte tendência a respostas de baixa profundidade.
- **Deep Value Benchmark (NeurIPS 2026):** DVGR médio de 0,30, abaixo do acaso; modelos maiores generalizam pior.
- **Dark Triad Model Organisms of Misalignment (Lulla et al., 2026):** dissonância afetiva como déficit empático central; personas sombrias induzidas com fine-tuning mínimo.
- **Emotions in Artificial Intelligence (Borotschnig, 2025):** "zumbis afetivos" — expressão emocional sem experiência emocional.
- **Functional Emotion Without Character (Zare, 2026):** emoção funcional sem caráter; três condições ausentes (incorporação regulatória, continuidade temporal, self integrado).
- **MORIS:** ontologia moral determinística de 93 primitivas em lógica deôntica.
- **Inner Speech for Ethics by Design:** discurso interno funcional como espaço de deliberação ética.
- **Bio-Regulated Mind Matrix / Resilient Psychological AI:** regulação homeostática e pilha de coping com estabilidade de Lyapunov.