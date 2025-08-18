import seaborn as sns
import matplotlib.pyplot as plt


def main() -> None:
    """
    Visualización bivariante con Seaborn sobre el dataset 'tips':
    - Dispersión total_bill vs tip con hue por sexo y paleta 'coolwarm'.
    - Línea de regresión superpuesta (sin puntos) en el mismo eje.
    """
    sns.set_style("whitegrid")
    tips = sns.load_dataset("tips")

    fig, ax = plt.subplots(figsize=(9, 6))

    sns.scatterplot(
        data=tips,
        x="total_bill",
        y="tip",
        hue="sex",
        palette="coolwarm",
        alpha=0.6,
        ax=ax,
    )

    sns.regplot(
        data=tips,
        x="total_bill",
        y="tip",
        scatter=False,
        color="black",
        line_kws={"linewidth": 2},
        ax=ax,
    )

    ax.set_title("Relación entre Total Bill y Tip por Sexo (con línea de regresión)")
    ax.set_xlabel("Total Bill")
    ax.set_ylabel("Tip")
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()


