import numpy as np
import matplotlib.pyplot as plt


def main() -> None:
    """
    Genera un conjunto de datos multivariante y crea un gráfico de dispersión
    donde:
      - X, Y ~ Uniforme(0, 10)
      - Color (c) ~ Uniforme(0, 100)
      - Tamaño (s) ~ Uniforme(0, 1) * 200
    """
    rng = np.random.default_rng()

    x = rng.uniform(0, 10, 200)
    y = rng.uniform(0, 10, 200)
    colores = rng.uniform(0, 100, 200)
    tamanos = rng.random(200) * 200

    plt.figure(figsize=(9, 6))
    dispersion = plt.scatter(
        x,
        y,
        c=colores,
        s=tamanos,
        cmap="plasma",
        alpha=0.6,
    )

    plt.title("Gráfico de dispersión multivariante (color y tamaño mapeados)")
    plt.xlabel("X")
    plt.ylabel("Y")

    barra_colores = plt.colorbar(dispersion)
    barra_colores.set_label("Escala de color (0 a 100)")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()


