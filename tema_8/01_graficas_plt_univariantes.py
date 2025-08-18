import numpy as np
import matplotlib.pyplot as plt


def main() -> None:
    """
    Genera 1500 datos con distribución normal (media=5, desviación estándar=2)
    y dibuja su histograma con 40 bins, barras verdes semi-transparentes y
    bordes rojos.
    """
    datos = np.random.normal(loc=5, scale=2, size=1500)

    plt.figure(figsize=(8, 5))
    plt.hist(
        datos,
        bins=40,
        color="green",
        alpha=0.5,
        edgecolor="red",
    )

    plt.title("Histograma de datos ~ N(μ=5, σ=2), n=1500")
    plt.xlabel("Valor")
    plt.ylabel("Frecuencia")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()


