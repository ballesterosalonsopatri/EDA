# funciones.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from variables import AÑOS, PALETA_PROCEDENCIA, PALETA_ISLAS


def cargar_datos(ruta_csv):
    df = pd.read_csv(ruta_csv)
    df = df.rename(columns={
        df.columns[0]: 'gasto',
        df.columns[1]: 'territorio',
        df.columns[2]: 'procedencia'
    })
    return df


def calcular_promedios(df):
    cols_3T = [col for col in df.columns if "3T" in col]
    cols_4T = [col for col in df.columns if "4T" in col]

    prom_3T = df[cols_3T].mean(axis=1).round(2)
    prom_4T = df[cols_4T].mean(axis=1).round(2)

    for col in ["2025 3T", "2025 4T"]:
        if col in df.columns:
            df.drop(columns=[col], inplace=True)

    df.insert(4, "2025 3T", prom_3T)
    df.insert(3, "2025 4T", prom_4T)

    prom_2025 = df.iloc[:, 3:7].mean(axis=1).round(2)
    for col in ["2025", "Promedio 2025"]:
        if col in df.columns:
            df.drop(columns=[col], inplace=True)

    df.insert(3, "2025", prom_2025)
    return df


def filtrar_datos(df, eliminar):
    df_final = df.copy()
    df_final = df_final[
        ~df_final['gasto'].str.strip().str.lower().isin(map(str.lower, eliminar))
    ]
    return df_final


def normalizar(df):
    for col in ['gasto', 'territorio', 'procedencia']:
        df[col] = df[col].str.strip().str.lower()
    return df


def guardar_grafico(nombre, carpeta="EDA/img"):
    """Guarda el gráfico actual en formato PNG dentro de la carpeta especificada."""
    os.makedirs(carpeta, exist_ok=True)
    ruta = os.path.join(carpeta, f"{nombre}.png")
    plt.savefig(ruta, format="png", bbox_inches="tight", dpi=300)
    print(f"✅ Gráfico guardado en: {ruta}")


# --- Gráficos --- #

def grafico_max_por_procedencia(df, save_path=None):
    sns.set_theme(style="whitegrid", font_scale=1.2)
    plt.figure(figsize=(10, 5))
    ax = sns.barplot(
        data=df,
        x="Año",
        y="Valor_max",
        hue="Procedencia",
        dodge=False,
        palette=PALETA_PROCEDENCIA
    )
    ax.set_title("Máximo Gasto por Año y Procedencia", fontsize=16, fontweight="bold")
    ax.set_xlabel("AÑO")
    ax.set_ylabel("GASTO MÁXIMO")

    for p in ax.patches:
        height = p.get_height()
        if height > 0:
            ax.text(
                p.get_x() + p.get_width() / 2,
                height + 1,
                f"{height:.2f}",
                ha="center", va="bottom",
                fontsize=11,
                fontweight="bold"
            )

    ax.legend(title="Procedencia", bbox_to_anchor=(1, 0.5), loc="center left", frameon=False)
    plt.xticks(rotation=45)
    plt.tight_layout(rect=[0, 0, 0.9, 1])

    if save_path:
        guardar_grafico(save_path)
    plt.show()


def grafico_porcentaje(df_long, save_path=None):
    plt.figure(figsize=(12,6))
    sns.barplot(x='Año', y='Porcentaje', hue='gasto', data=df_long)
    plt.title('Distribución porcentual del gasto en Canarias por tipo de gasto')
    plt.ylabel('Porcentaje (%)')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    if save_path:
        guardar_grafico(save_path)
    plt.show()


def grafico_max_por_isla(df, save_path=None):
    sns.set_style("whitegrid")
    plt.figure(figsize=(12,6))
    ax = sns.barplot(data=df, x='Año', y='Valor máximo', hue='Isla', palette=PALETA_ISLAS)
    plt.title('Valor máximo por año y isla')
    plt.ylabel('Valor máximo')
    plt.xlabel('Año')

    for p in ax.patches:
        height = p.get_height()
        ax.annotate(
            f'{height:.2f}',
            (p.get_x() + p.get_width()/2., height),
            ha='center', va='bottom',
            fontsize=12, fontweight='bold',
            xytext=(0,3), textcoords='offset points'
        )
    plt.legend(title='Isla', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    if save_path:
        guardar_grafico(save_path)
    plt.show()


def grafico_linea(df_long, save_path=None):
    sns.set_style("whitegrid")
    plt.figure(figsize=(10,6))
    sns.lineplot(data=df_long, x='Año', y='Valor', marker='o', color='#1f77b4', linewidth=2)
    plt.title('Evolución del gasto turístico en Canarias (Total)', fontsize=16)
    plt.ylabel('Gasto total')
    plt.xlabel('Año')

    for x, y in zip(df_long['Año'], df_long['Valor']):
        plt.text(x, y+1, f'{y:.2f}', ha='center', va='bottom', fontweight='bold')

    plt.tight_layout()
    if save_path:
        guardar_grafico(save_path)
    plt.show()


def grafico_max_por_isla(df):
    sns.set_style("whitegrid")
    plt.figure(figsize=(12,6))
    ax = sns.barplot(data=df, x='Año', y='Valor máximo', hue='Isla', palette=PALETA_ISLAS)
    plt.title('Valor máximo por año y isla')
    plt.ylabel('Valor máximo')
    plt.xlabel('Año')

    for p in ax.patches:
        height = p.get_height()
        ax.annotate(
            f'{height:.2f}',
            (p.get_x() + p.get_width()/2., height),
            ha='center', va='bottom',
            fontsize=12, fontweight='bold',
            xytext=(0,3), textcoords='offset points'
        )
    plt.legend(title='Isla', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()


def grafico_linea(df_long):
    sns.set_style("whitegrid")
    plt.figure(figsize=(10,6))
    sns.lineplot(data=df_long, x='Año', y='Valor', marker='o', color='#1f77b4', linewidth=2)
    plt.title('Evolución del gasto turístico en Canarias (Total)', fontsize=16)
    plt.ylabel('Gasto total')
    plt.xlabel('Año')

    for x, y in zip(df_long['Año'], df_long['Valor']):
        plt.text(x, y+1, f'{y:.2f}', ha='center', va='bottom', fontweight='bold')

    plt.tight_layout()
    plt.show()