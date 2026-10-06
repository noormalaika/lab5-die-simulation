
import numpy as np
import matplotlib.pyplot as plt

rolls = np.random.randint(1, 7, size=1000)

print("First 10 rolls:", rolls[:10])

faces, counts = np.unique(rolls, return_counts=True)

print("\nFace  Count  Empirical P  Theoretical P")

for face, count in zip(faces, counts):
    empirical_p = count / 1000
    theoretical_p = 1 / 6

    print(
        f"{face:<6}{count:<7}"
        f"{empirical_p:<13.3f}{theoretical_p:.4f}"
    )

plt.figure(figsize=(8, 5))

plt.hist(
    rolls,
    bins=np.arange(0.5, 7.5, 1),
    edgecolor="black",
    rwidth=0.8
)

plt.xticks(range(1, 7))
plt.xlabel("Die Face")
plt.ylabel("Frequency")
plt.title("Histogram of 1000 Die Rolls")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()

plt.savefig("die_rolls.png", dpi=300)

plt.show()

print("\nSaved die_rolls.png")
