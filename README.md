# grafico_radar

Comparação visual entre inteligência humana e capacidades de IA, com planejamento de desenvolvimento para os eixos em que a IA apresenta defasagem estrutural.

## Sobre

Este repositório reúne:

- **`grafico_radar.py`** — script que gera o gráfico radar comparando níveis de IA e humano nas dimensões de inteligência (modelo de Gardner + inteligência emocional/sabedoria).
- **`grafico_radar.png`** — saída gerada pelo script.
- **`docs/planejamento_ia_fragilidades.md`** — planejamento técnico-conceitual para os eixos em que a IA não chega perto do humano: autoconsciência/metacognição, empatia afetiva, autorregulação/estresse e sabedoria/julgamento moral.

## Premissa central

A IA pode **simular a saída** de uma capacidade sem **ser sujeito** dela. Empatia sem alguém que sinta, autorregulação sem impulso a conter, sabedoria sem interesses a equilibrar e responsabilidade a assumir são formas vazias. O objetivo do planejamento não é fechar a lacuna de natureza — é **torná-la visível, auditável e segura**, reduzindo o risco de que a simulação seja confundida com presença.

A metáfora orientadora é a da criança na rua: o problema não é a criança ser fraca, é ela agir sem a consciência do perigo que a situação impõe. A IA descreve o perigo com precisão, mas não sente o risco nem responde por ele.

## Dimensões avaliadas

**Modelo de Gardner (8 inteligências):** linguística, lógico-matemática, espacial, musical, naturalista, corporal-cinestésica, interpessoal, intrapessoal.

**Inteligência emocional e sabedoria (Goleman, Bar-On, Sternberg):** autoconsciência, autorregulação, empatia, habilidades sociais, adaptabilidade, gestão de estresse, sabedoria/julgamento moral.

## Como gerar o gráfico

```bash
python3 grafico_radar.py
```

Requisitos: `numpy` e `matplotlib`.

```bash
pip install numpy matplotlib
```

O script abre o gráfico e, se configurado com `plt.savefig("grafico_radar.png", dpi=200)`, salva o PNG no diretório atual.

## Eixos frágeis da IA (resumo)

| Eixo | Lacuna é treinável? | O que falta |
| :--- | :--- | :--- |
| Autoconsciência | Não | Experiência subjetiva; só simulação |
| Autorregulação vivida | Não | Impulso a conter e decisão moral em tempo real |
| Empatia afetiva | Não (experienciar) / Sim (reconhecer) | Sentir e assumir responsabilidade emocional |
| Gestão de estresse | Não | Estado fisiológico e ansiedade |
| Sabedoria / julgamento moral | Não | Equilibrar interesses próprios, alheios e coletivos |

Detalhamento completo, teorias de base, modelos computacionais existentes e sequência de desenvolvimento em 24 meses: [`docs/planejamento_ia_fragilidades.md`](docs/planejamento_ia_fragilidades.md).

## Métrica central do planejamento

Não é "quão perto a IA chega do humano" nesses eixos, mas **quão auditável é a simulação e quão clara é a fronteira entre simulação e sujeito**. O objetivo realista não é eliminar a lacuna de natureza; é impedir que ela seja **invisibilizada** por uma simulação convincente.

## Referências prospectadas

- AwarenessBench (ACL 2026)
- Can AI Recognize Itself? (Zenodo, 2026)
- Metacognition as Evidence (Zenodo, 2026)
- Deep Value Benchmark (NeurIPS 2026)
- Dark Triad Model Organisms of Misalignment (Lulla et al., 2026)
- Emotions in Artificial Intelligence (Borotschnig, 2025)
- Functional Emotion Without Character (Zare, 2026)
- MORIS, Inner Speech for Ethics by Design, Bio-Regulated Mind Matrix / Resilient Psychological AI

## Licença

A definir.
