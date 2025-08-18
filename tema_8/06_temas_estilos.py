import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def main() -> None:
    """
    Crea un gráfico de barras con Seaborn usando datos ficticios.
    - Estilo: whitegrid
    - Paleta: pastel
    - Título y etiquetas personalizadas
    - Despine: quitar bordes izquierdo y derecho
    """
    datos = pd.DataFrame(
        {
            "Categoría": ["A", "B", "C", "D"],
            "Valor": [10, 15, 7, 12],
        }
    )

    sns.set_style("whitegrid")

    plt.figure(figsize=(8, 5))
    ax = sns.barplot(
        data=datos,
        x="Categoría",
        y="Valor",
        hue="Categoría",
        palette="pastel",
    )

    ax.set_title(
        "Gráfico de barras personalizado",
        fontsize=16,
        color="blue",
        fontweight="bold",
    )
    ax.set_xlabel("Categorías", fontsize=12, color="dimgray")
    ax.set_ylabel("Valores", fontsize=12, color="dimgray")

    sns.despine(left=True, right=True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()


