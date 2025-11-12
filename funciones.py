# funciones.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from variables import *

# =======================================================
#   FUNCIONES DE CARGA Y LIMPIEZA DE DATOS
# =======================================================

def cargar_datos():
    """Carga el archivo CSV original del ISTAC y renombra las primeras columnas."""
    df = pd.read_csv(RUTA_CSV)
    df = df.rename(columns={df.columns[0]: 'gasto', df.columns[1]: 'territorio', df.columns[2]: 'procedencia'})
    return df


def limpiar_y_preparar(df):
    """Calcula promedios trimestrales y anuales, y estructura el DataFrame final."""
    cols_3T = [col for col in df.columns if "3T" in col]
    cols_4T = [col for col in df.columns if "4T" in col]

    prom_3T = df[cols_3T].mean(axis=1).round(2)
    prom_4T = df[cols_4T].mean(axis=1).round(2)

    # Eliminar si ya existen
    for col in ["2025 3T", "2025 4T"]:
        if col in df.columns:
            df.drop(columns=[col], inplace=True)

    # Insertar nuevas columnas
    df.insert(4, "2025 3T", prom_3T)
    df.insert(3, "2025 4T", prom_4T)

    # Eliminar columnas antiguas
    for col in ["2025", "Promedio 2025"]:
        if col in df.columns:
            df.drop(columns=[col], inplace=True)

    # Calcular promedio anual 2025
    prom_2025 = df.iloc[:, 3:7].mean(axis=1).round(2)
    df.insert(3, "2025", prom_2025)

    return df


def filtrar_datos(df):
    """Normaliza y limpia los datos, eliminando gastos duplicados."""
    df['gasto'] = df['gasto'].str.strip().str.lower()
    df['territorio'] = df['territorio'].str.strip().str.lower()
    df['procedencia'] = df['procedencia'].str.strip().str.lower()

    df_final = df.loc[:, COLUMNAS_FIJAS + [col for col in df.columns if col in AÑOS]]

    # Filtrar filas no deseadas
    df_final_filtrado = df_final[
        ~df_final['gasto'].isin(map(str.lower, ELIMINAR))
    ]

    return df_final_filtrado


# =======================================================
#   BLOQUE H1 – Procedencia con mayor gasto por año
# =======================================================

def calcular_h1(df):
    """Determina qué procedencia tiene el mayor gasto turístico por año."""
    df_proc = df[
        (df['gasto'] == 'total') &
        (df['territorio'] == 'canarias') &
        (df['procedencia'].isin(PROCEDENCIAS))
    ]

    df_indexed = df_proc.set_index('procedencia')[AÑOS]
    df_h1 = pd.DataFrame({
        'Año': AÑOS,
        'Procedencia': df_indexed.idxmax(),
        'Valor_max': df_indexed.max()
    }).reset_index(drop=True)

    return df_h1


# =======================================================
#   BLOQUE H2 – Distribución porcentual del gasto
# =======================================================

def calcular_h2(df):
    """Calcula el porcentaje que representa cada tipo de gasto sobre el total."""
    df_comprobacion_h2 = df[
        (df['gasto'].str.lower() != "total") &
        (df['territorio'].str.lower() == "canarias") &
        (df['procedencia'].str.lower() == "total")
    ].reset_index(drop=True)

    df_porcentaje_col = df_comprobacion_h2.copy()
    df_porcentaje_col[AÑOS] = df_porcentaje_col[AÑOS].div(
        df_porcentaje_col[AÑOS].sum(axis=0), axis=1
    ) * 100

    df_porcentaje_col[AÑOS] = df_porcentaje_col[AÑOS].round(2)
    return df_porcentaje_col


# =======================================================
#   BLOQUE H3 – Isla con mayor gasto diario
# =======================================================

def calcular_h3(df):
    """Obtiene la isla con mayor gasto turístico diario por año."""
    df_final_h3 = df[
        (df['gasto'].str.lower() == "total") &
        (df['territorio'].isin([t.lower() for t in TERRITORIOS])) &
        (df['procedencia'].str.lower() == "total")
    ].reset_index(drop=True)

    df_max_por_anio = pd.DataFrame(
        [(col, df_final_h3.loc[df_final_h3[col].idxmax(), 'territorio'].title(), df_final_h3[col].max())
         for col in AÑOS],
        columns=['Año', 'Isla', 'Valor máximo']
    )

    # Normalizar nombres para coincidir con la paleta
    df_max_por_anio['Isla'] = df_max_por_anio['Isla'].replace({
        'Gran canaria': 'Gran Canaria',
        'Fuerteventura': 'Fuerteventura',
        'Tenerife': 'Tenerife',
        'Lanzarote': 'Lanzarote',
        'La palma': 'La Palma'
    })

    return df_max_por_anio


# =======================================================
#   BLOQUE H4 – Evolución del gasto total
# =======================================================

def calcular_h4(df):
    """Extrae la evolución temporal del gasto total en Canarias."""
    df_final_h4 = df[
        (df['gasto'].str.lower() == "total") &
        (df['territorio'].str.lower() == "canarias") &
        (df['procedencia'].str.lower() == "total")
    ].reset_index(drop=True)

    df_long = df_final_h4.melt(
        id_vars=['gasto', 'territorio', 'procedencia'],
        value_vars=AÑOS,
        var_name='Año',
        value_name='Valor'
    )

    return df_long


# =======================================================
#   FUNCIONES DE GRÁFICOS Y GUARDADO AUTOMÁTICO
# =======================================================

def mostrar_y_guardar_grafico(nombre_archivo):
    """Muestra el gráfico y lo guarda en la carpeta img después de cerrar la ventana."""
    ruta_completa = os.path.join(RUTA_IMG, nombre_archivo)
    plt.savefig(ruta_completa, bbox_inches='tight')
    print(f"✅ Guardado: {ruta_completa}")
    plt.show()  # espera que el usuario cierre la ventana manualmente
    plt.close()


def grafico_h1(df):
    """Gráfico H1: Máximo gasto por procedencia y año."""
    sns.set_theme(style="whitegrid", font_scale=1.2)
    plt.figure(figsize=(10, 5))
    ax = sns.barplot(data=df, x="Año", y="Valor_max", hue="Procedencia",
                     dodge=False, palette=PALETA_PROCEDENCIA)
    ax.set_title("Máximo Gasto por Año y Procedencia", fontsize=16, fontweight="bold")
    for p in ax.patches:
        height = p.get_height()
        ax.text(p.get_x() + p.get_width() / 2, height + 1, f"{height:.2f}",
                ha="center", va="bottom", fontsize=10, fontweight="bold")
    plt.legend(title="Procedencia", bbox_to_anchor=(1.05, 0.5), loc='center left', frameon=False)
    plt.tight_layout()
    mostrar_y_guardar_grafico("grafico_h1.png")


def grafico_h2(df):
    """Gráfico H2: Distribución porcentual del gasto por tipo."""
    df_long = df.melt(id_vars=['gasto'], value_vars=AÑOS, var_name='Año', value_name='Porcentaje')
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Año', y='Porcentaje', hue='gasto', data=df_long)
    plt.title('Distribución porcentual del gasto en Canarias por tipo de gasto')
    plt.ylabel('Porcentaje (%)')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    mostrar_y_guardar_grafico("grafico_h2.png")


def grafico_h3(df):
    """Gráfico H3: Valor máximo de gasto diario por isla."""
    plt.figure(figsize=(12, 6))
    ax = sns.barplot(data=df, x='Año', y='Valor máximo', hue='Isla', palette=PALETA_ISLAS)
    plt.title('Valor máximo de gasto diario por turista (año e isla)', fontsize=16)
    for p in ax.patches:
        height = p.get_height()
        ax.annotate(f'{height:.2f}', (p.get_x() + p.get_width()/2., height),
                    ha='center', va='bottom', fontsize=10, fontweight='bold')
    plt.legend(title='Isla', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    mostrar_y_guardar_grafico("grafico_h3.png")


def grafico_h4(df_long):
    """Gráfico H4: Evolución temporal del gasto total."""
    plt.figure(figsize=(12,6))
    sns.lineplot(data=df_long, x='Año', y='Valor', marker='o', color='#1f77b4', linewidth=2)
    plt.title('Evolución del gasto turístico diario por turista en Canarias (Total)', fontsize=16)
    plt.ylabel('Gasto total')
    plt.xlabel('Año')
    for x, y in zip(df_long['Año'], df_long['Valor']):
        plt.text(x, y+1, f'{y:.2f}', ha='center', va='bottom', fontweight='bold')
    plt.tight_layout()
    mostrar_y_guardar_grafico("grafico_h4.png")