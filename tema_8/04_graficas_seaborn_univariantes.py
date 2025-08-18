import seaborn as sns
import matplotlib.pyplot as plt


def main() -> None:
    """
    Histograma de la variable 'tip' del dataset 'tips' usando Seaborn.
    - 40 bins
    - Se muestra densidad (no frecuencia)
    - KDE superpuesta en color azul
    - Estilo 'darkgrid'
    """
    sns.set_style("darkgrid")
    tips = sns.load_dataset("tips")

    plt.figure(figsize=(8, 5))
    sns.histplot(
        data=tips,
        x="tip",
        bins=40,
        stat="density",
        kde=True,
        kde_kws={"color": "blue", "linewidth": 2},
    )

    plt.title("Distribución de 'tip' con densidad y KDE (Seaborn)")
    plt.xlabel("Tip")
    plt.ylabel("Densidad")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()


