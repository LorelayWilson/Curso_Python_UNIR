import numpy as np
import matplotlib.pyplot as plt


def main() -> None:
    """
    Crea dos conjuntos de datos (x, y) con relación lineal con ruido,
    ajusta una regresión lineal y grafica el scatter y la línea ajustada.
    """
    rng = np.random.default_rng()
    x = rng.uniform(0, 50, 100)
    ruido = rng.normal(0, 10, 100)
    y = 2.5 * x + ruido

    pendiente, intercepto = np.polyfit(x, y, 1)

    x_linea = np.linspace(x.min(), x.max(), 100)
    y_linea = pendiente * x_linea + intercepto

    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, color="purple", s=50)
    plt.plot(x_linea, y_linea, color="green", linewidth=2)
    plt.grid(True, linestyle="--", alpha=0.4)

    plt.title("Dispersión con regresión lineal (y ≈ 2.5x + ruido)")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()


