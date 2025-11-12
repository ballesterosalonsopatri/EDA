
![Mapa del Análisis Territorial](../img/mapa.png)

# 💰 Análisis del Gasto Turístico en las Islas Canarias (2018-2025)

## 🎯 1. Resumen Ejecutivo

Este proyecto de **Análisis Exploratorio de Datos (EDA)** se centra en el estudio del **Gasto Medio Diario por Turista** en las Islas Canarias, un factor económico clave para el archipiélago. A través del análisis de datos históricos (2018-2025), se identifica la evolución del gasto, su distribución por categorías y las disparidades entre los principales mercados emisores (países de procedencia) e islas.

El análisis confirma una **robusta recuperación post-pandemia** con un gasto que alcanza máximos históricos, pero también revela una alta dependencia del sector de **Alojamiento**.

## 🧠 2. Hipótesis y Conclusiones

El proyecto fue guiado por cuatro hipótesis, todas las cuales fueron verificadas positivamente:

| Hipótesis | Conclusión | Gráfico de Soporte |
| :--- | :--- | :--- |
| **H1: Origen del Gasto Máximo** | El gasto diario máximo es impulsado por turistas del **Reino Unido** y **Países Nórdicos**. | **H1: Máximo Gasto por Procedencia** |
| **H2: Concentración del Gasto** | El **Alojamiento** es la partida de gasto individual más significativa en la serie histórica. | **H2: Distribución Porcentual del Gasto** |
| **H3: Liderazgo Insular** | **Tenerife** registra el valor máximo de gasto diario con mayor frecuencia y es la isla líder en este indicador. | **H3: Valor Máximo por Año e Isla** |
| **H4: Recuperación Post-Pandemia** | Se confirma una **Expansión (2021–2024)** con máximos históricos de gasto tras el mínimo de 2020. | **H4: Evolución del Gasto Total** |

---

## 📁 3. Estructura del Proyecto

El análisis se estructura en un paquete modular (`utils`) para una ejecución limpia y eficiente, basado en el flujo de trabajo de Python y `NumPy`/`Pandas`.
├── EDA/│   ├── data/│   │   └── gastoxturistaxdia.csv  # ⬅️ Fuente de datos (ISTAC)│   ├── img/                       # ⬅️ Directorio de salida de todos los gráficos (.png)│   └── utils/                     # ⬅️ Paquete de Código│       ├── init.py            # Identificador de Paquete│       ├── main.py                # Control de Ejecución (Flujo principal)│       ├── funciones.py           # Funciones de Cálculo, EDA y Visualización│       └── variable.py            # Variables y Constantes del proyecto├── README.md                      # Documentación del proyecto└── requirements.txt               # (Recomendado) Lista de dependencias
## ⚙️ 4. Requisitos e Instalación

Para ejecutar el análisis, se requiere:

* **Python 3.10** o superior.
* **Librerías:** `pandas`, `numpy`, `matplotlib`, `seaborn`.

Instala las dependencias necesarias en tu entorno virtual con el siguiente comando:

```bash
pip install pandas numpy matplotlib seaborn
▶️ 5. Cómo Ejecutar el AnálisisLa ejecución debe realizarse desde el directorio principal del EDA, tratando a utils como un paquete.Asegúrate de estar en el directorio EDA (el padre de utils).Ejecuta el script principal con el siguiente comando:Bashpython -m utils.main
El programa cargará los datos, realizará la limpieza, ejecutará los cálculos de las cuatro hipótesis y guardará los gráficos generados en la carpeta EDA/img/.📈 6. Resultados y VisualizacionesTodos los resultados gráficos generados confirman las hipótesis planteadas y se almacenan en la carpeta EDA/img/. Estos gráficos son clave para entender la distribución y la evolución temporal del gasto.GráficoDescripción de la VisualizaciónEjemplo de Uso de SímbolosH1Gráfico de Barras que compara el Valor Máximo de Gasto por procedencia.Muestra la alta rentabilidad del turista Nórdico/Británico.H2Gráfico de Barras que segmenta el gasto total de Canarias por categoría.Muestra el peso porcentual del Alojamiento frente a Ocio o Restauración.H3Gráfico de Barras que identifica la isla con el valor máximo de gasto en cada año.Comprueba la posición dominante de Tenerife en picos de gasto.H4Gráfico de Línea que traza la serie histórica del Gasto Total (2018-2025).Visualiza la caída dramática en 2020 y la recuperación posterior.