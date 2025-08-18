import seaborn as sns
import matplotlib.pyplot as plt


def main() -> None:
    """
    Visualización multigrid (FacetGrid) del dataset 'penguins':
    - Columnas por especie (species)
    - Filas por sexo (sex)
    - Dispersión: flipper_length_mm vs body_mass_g
    - hue por isla (island) con leyenda
    - Límites de ejes consistentes, ajuste de tamaño y espaciado
    """
    penguins = sns.load_dataset("penguins")

    # Límites consistentes de ejes (ignorando valores NaN)
    x_data = penguins["flipper_length_mm"].dropna()
    y_data = penguins["body_mass_g"].dropna()
    if not x_data.empty and not y_data.empty:
        x_min, x_max = x_data.min(), x_data.max()
        y_min, y_max = y_data.min(), y_data.max()
        # Margen del 5%
        x_pad = (x_max - x_min) * 0.05
        y_pad = (y_max - y_min) * 0.05
        x_lim = (x_min - x_pad, x_max + x_pad)
        y_lim = (y_min - y_pad, y_max + y_pad)
    else:
        # Valores por defecto si el dataset está vacío
        x_lim = (160, 240)
        y_lim = (2500, 6500)

    g = sns.FacetGrid(
        data=penguins,
        col="species",
        row="sex",
        hue="island",
        height=3.6,
        aspect=1.15,
        margin_titles=True,
        despine=False,
    )

    g.map_dataframe(
        sns.scatterplot,
        x="flipper_length_mm",
        y="body_mass_g",
        alpha=0.7,
    )

    g.add_legend(title="Isla")
    g.set_axis_labels("Longitud de aleta (mm)", "Masa corporal (g)")
    g.set(xlim=x_lim, ylim=y_lim)

    # Ajuste de espacios y título general
    g.fig.subplots_adjust(top=0.90, wspace=0.15, hspace=0.25)
    g.fig.suptitle(
        "Relación entre longitud de aleta y masa corporal por especie y sexo",
        fontsize=14,
        fontweight="bold",
    )

    plt.show()


if __name__ == "__main__":
    main()


