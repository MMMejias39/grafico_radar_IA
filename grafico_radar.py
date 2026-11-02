import numpy as np
import matplotlib.pyplot as plt

# Dimensões (modelo revisado)
labels = [
    "Linguística", "Lógico-Matemática", "Espacial", "Musical",
    "Naturalista", "Corporal-Cinestésica",
    "Autoconsciência", "Autorregulação", "Empatia",
    "Habilidades Sociais", "Adaptabilidade", "Gestão de Estresse",
    "Sabedoria / Julgamento Moral"
]

ia =     [9, 9, 7, 6, 6, 3, 2, 3, 4, 4, 3, 2, 2]
humano = [8, 8, 7, 7, 8, 9, 9, 8, 9, 9, 8, 8, 9]

N = len(labels)
angles = np.linspace(0, 2*np.pi, N, endpoint=False).tolist()
angles += angles[:1]

ia += ia[:1]
humano += humano[:1]

fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))
ax.plot(angles, ia, color="crimson", linewidth=2, label="IA")
ax.fill(angles, ia, color="crimson", alpha=0.25)
ax.plot(angles, humano, color="steelblue", linewidth=2, label="Humano")
ax.fill(angles, humano, color="steelblue", alpha=0.20)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=9)
ax.set_ylim(0, 10)
ax.set_yticks([2,4,6,8,10])
ax.set_yticklabels(["2","4","6","8","10"], fontsize=8)
ax.set_title("Radar: IA vs Humano — Gardner + Inteligência Emocional/Sabedoria", pad=20)
ax.legend(loc="upper right", bbox_to_anchor=(1.25, 1.1))
plt.tight_layout()
plt.show()