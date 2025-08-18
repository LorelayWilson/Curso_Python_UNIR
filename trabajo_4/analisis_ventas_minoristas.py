import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def main() -> None:
    # Configuración de estilo
    sns.set_theme(style="whitegrid", palette="Set2")

    # Ruta del dataset
    base_dir = os.path.dirname(__file__)
    csv_path = os.path.join(base_dir, "superstore_dataset2012.csv")

    # Carga de datos
    df = pd.read_csv(
        csv_path,
        encoding="latin-1",  # Maneja caracteres especiales del archivo
    )

    # Exploración inicial
    print("Dimensiones:", df.shape)
    print("Columnas:", list(df.columns))
    print("\nTipos de datos:")
    print(df.dtypes)
    print("\nValores nulos por columna:")
    print(df.isna().sum())

    # Preparación: conversión de fechas y columnas auxiliares
    # Nota: el dataset usa formato d/m/yyyy (ej: 1/6/2012 -> 1 de junio)
    for col in ["Order Date", "Ship Date"]:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], dayfirst=True, errors="coerce")

    if "Order Date" in df.columns:
        df["Order Month"] = df["Order Date"].dt.to_period("M").astype(str)

    # Selección de columnas comunes del dataset
    numeric_cols = [c for c in ["Sales", "Profit", "Quantity", "Discount", "Shipping Cost"] if c in df.columns]

    # -------- Visualizaciones univariantes (Matplotlib) --------
    # Histograma de ventas (Matplotlib)
    fig, axes = plt.subplots(2, 2, figsize=(14, 9))
    axes = axes.ravel()

    if "Sales" in df.columns:
        axes[0].hist(df["Sales"].dropna(), bins=30, color="#4C72B0", edgecolor="white")
        axes[0].set_title("Distribución de Ventas (histograma)")
        axes[0].set_xlabel("Ventas")
        axes[0].set_ylabel("Frecuencia")
        # Conclusión: ventas con asimetría positiva y presencia de transacciones altas.

    # -------- Visualizaciones univariantes (Seaborn) --------
    # Frecuencia por categoría (Seaborn)
    if "Category" in df.columns:
        cat_counts = df["Category"].value_counts().sort_values(ascending=False)
        sns.barplot(x=cat_counts.index, y=cat_counts.values, ax=axes[1], hue=None)
        axes[1].set_title("Frecuencia por Categoría")
        axes[1].set_xlabel("Categoría")
        axes[1].set_ylabel("Número de pedidos")
        axes[1].tick_params(axis="x", rotation=15)
        # Conclusión: algunas categorías concentran más pedidos.

    # -------- Gráfico bivariante (Seaborn) --------
    # Boxplot de beneficio por categoría (Seaborn)
    if "Profit" in df.columns and "Category" in df.columns:
        sns.boxplot(data=df, x="Category", y="Profit", ax=axes[2])
        axes[2].set_title("Beneficio por Categoría (boxplot)")
        axes[2].set_xlabel("Categoría")
        axes[2].set_ylabel("Beneficio")
        axes[2].tick_params(axis="x", rotation=15)
        # Conclusión: hay variabilidad y outliers de beneficio por categoría.

    # -------- Gráfico bivariante (Matplotlib) --------
    # Dispersión Ventas vs Beneficio (Matplotlib)
    if "Sales" in df.columns and "Profit" in df.columns:
        axes[3].scatter(df["Sales"], df["Profit"], alpha=0.4, color="#55A868")
        axes[3].set_title("Relación Ventas vs Beneficio (dispersión)")
        axes[3].set_xlabel("Ventas")
        axes[3].set_ylabel("Beneficio")
        # Conclusión: tendencia general positiva con algunos pedidos en pérdida.

    fig.suptitle("Resumen de visualizaciones univariantes y bivariantes")
    fig.tight_layout(rect=[0, 0, 1, 0.97])

    # Guardado de la figura principal
    fig_path = os.path.join(base_dir, "fig_resumen_subplots.png")
    fig.savefig(fig_path, dpi=150)
    print(f"Figura guardada en: {fig_path}")

    # -------- Bivariantes adicionales con Seaborn --------
    # Dispersión con regresión (regplot) Ventas vs Beneficio
    if "Sales" in df.columns and "Profit" in df.columns:
        plt.figure(figsize=(7, 5))
        sns.regplot(data=df, x="Sales", y="Profit", scatter_kws={"alpha": 0.3})
        plt.title("Ventas vs Beneficio con regresión (Seaborn)")
        plt.xlabel("Ventas")
        plt.ylabel("Beneficio")
        plt.tight_layout()

    # Línea temporal mensual (Matplotlib) si existe fecha
    if "Order Date" in df.columns and "Sales" in df.columns:
        sales_by_month = (
            df.dropna(subset=["Order Date"]).set_index("Order Date")["Sales"].resample("MS").sum()
        )
        plt.figure(figsize=(8, 4))
        plt.plot(sales_by_month.index, sales_by_month.values, marker="o", color="#C44E52")
        plt.title("Evolución mensual de Ventas (Matplotlib)")
        plt.xlabel("Mes")
        plt.ylabel("Ventas")
        plt.tight_layout()
        # Conclusión: se observan meses con picos de ventas.

    # -------- Multivariante (Seaborn) --------
    if numeric_cols:
        corr = df[numeric_cols].corr(numeric_only=True)
        plt.figure(figsize=(6, 5))
        sns.heatmap(corr, annot=True, cmap="vlag", fmt=".2f", square=True)
        plt.title("Mapa de calor de correlaciones (variables numéricas)")
        plt.tight_layout()
        # Conclusión: identifica relaciones lineales (positivas/negativas) entre métricas.

    # Mostrar todo
    plt.show()


if __name__ == "__main__":
    main()


