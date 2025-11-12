# main.py

import pandas as pd
from funciones import (
    cargar_datos, calcular_promedios, filtrar_datos, normalizar,
    grafico_max_por_procedencia, grafico_porcentaje,
    grafico_max_por_isla, grafico_linea
)
from variables import ELIMINAR, AÑOS

# 1️⃣ Cargar datos
df = cargar_datos("../data/gastoxturistaxdia.csv")

# 2️⃣ Calcular promedios
df = calcular_promedios(df)

# 3️⃣ Filtrar filas no deseadas
df_filtrado = filtrar_datos(df, ELIMINAR)

# 4️⃣ Normalizar texto
df = normalizar(df)

# 5️⃣ Datos de ejemplo para visualizaciones
data = {
    "Año": [2025, 2024, 2023, 2022, 2021, 2020, 2019, 2018],
    "Procedencia": ["reino unido", "reino unido", "países nórdicos", "países nórdicos",
                    "países nórdicos", "países nórdicos", "países nórdicos", "países nórdicos"],
    "Valor_max": [186.33, 191.38, 182.03, 184.89, 172.43, 158.48, 152.05, 155.32]
}
df_demo = pd.DataFrame(data)

# 6️⃣ Generar y guardar gráficos
grafico_max_por_procedencia(df_demo, save_path="grafico_max_procedencia")
# grafico_porcentaje(df_long, save_path="grafico_porcentaje")
# grafico_max_por_isla(df_max_por_anio, save_path="grafico_max_isla")
# grafico_linea(df_long, save_path="grafico_linea")

print("✅ Análisis completado. Las imágenes se guardaron en 'EDA/img'.")