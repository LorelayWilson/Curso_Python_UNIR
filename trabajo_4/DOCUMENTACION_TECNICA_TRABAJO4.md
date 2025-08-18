# Documentación técnica — Trabajo 4

Análisis sencillo de ventas minoristas con pandas, Matplotlib y Seaborn. Documento alineado al script real `trabajo_4/analisis_ventas_minoristas.py`.

### Dataset y entorno
- Dataset: `trabajo_4/superstore_dataset2012.csv` (incluido en el proyecto)
- Dependencias: `pandas`, `matplotlib`, `seaborn`

### Ejecución rápida
```bash
cd trabajo_4
python analisis_ventas_minoristas.py
```

### Qué hace el script
1. Carga el CSV con codificación `latin-1`.
2. Exploración inicial: dimensiones, columnas, tipos y nulos por columna (impresos en consola).
3. Preparación: conversión de `Order Date` y `Ship Date` a datetime (formato día/mes/año); crea `Order Month`.
4. Visualizaciones:
   - Univariantes (Matplotlib): histograma de `Sales`.
   - Univariantes (Seaborn): barras de frecuencia por `Category`.
   - Bivariantes (Seaborn): boxplot de `Profit` por `Category`.
   - Bivariantes (Matplotlib): dispersión `Sales` vs `Profit`.
   - Bivariante extra (Seaborn): `regplot` `Sales` vs `Profit`.
   - Temporal (Matplotlib): línea mensual de ventas (resample `MS`).
   - Multivariante (Seaborn): heatmap de correlaciones (`Sales`, `Profit`, `Quantity`, `Discount`, `Shipping Cost`).
5. Subplots: figura 2x2 con 4 visualizaciones y título general.
6. Guardado: `trabajo_4/fig_resumen_subplots.png` (la figura 2x2). El resto de gráficos se muestran en pantalla.

### Personalización aplicada
- Estilo: `sns.set_theme(style="whitegrid", palette="Set2")`.
- Títulos y etiquetas en todos los ejes; rotación de categorías donde aplica.

### Conclusiones breves (ejemplos)
- Ventas con asimetría positiva (pocas transacciones muy altas).
- Variabilidad notable del beneficio por categoría, con outliers.
- Relación general positiva entre ventas y beneficio, con pedidos en pérdida.
- Patrones de ventas con picos mensuales (según la serie agregada).
- Correlaciones útiles entre métricas numéricas visibles en el heatmap.

### Estructura relevante
```
trabajo_4/
├── analisis_ventas_minoristas.py
├── superstore_dataset2012.csv
├── requirements.txt
└── fig_resumen_subplots.png   # generado al ejecutar
```

### Notas
- El script no descarga datos ni genera dashboards complejos. Trabaja con el CSV local y produce la figura de subplots, además de otras visualizaciones mostradas en pantalla.

### Reproducibilidad mínima
```txt
pandas>=1.3
matplotlib>=3.5
seaborn>=0.11
```
