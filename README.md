<p align="center">
  <img src="img/Islas-Canarias-Collage.jpg" alt="Mapa del Análisis Territorial" width="900">
</p>

# 🌍 Un viaje por el gasto turístico en Canarias (2018–2025)

---

## 🏖️ 1. Resumen Ejecutivo

Este proyecto de **Análisis Exploratorio de Datos (EDA)** estudia el **Gasto Medio Diario por Turista** en las **Islas Canarias**, una de las regiones más turísticas y dependientes del sector servicios de Europa.

Mediante datos históricos (2018–2025) obtenidos del **Instituto Canario de Estadística (ISTAC)**, se analizan la **evolución del gasto**, su **distribución por tipo**, y las **diferencias entre procedencias e islas**.

El análisis confirma una **recuperación económica sólida post-pandemia**, alcanzando **niveles récord de gasto turístico**, con el **alojamiento** como la partida más dominante dentro del consumo medio diario.

---

## 📊 2. Hipótesis y Conclusiones

El estudio se basa en cuatro hipótesis, todas **verificadas positivamente** mediante el análisis y la visualización de los datos.

| Hipótesis | Conclusión | Gráfico de Soporte |
| :--- | :--- | :--- |
| **H1: Origen del Gasto Máximo** | El gasto medio diario más alto proviene de turistas del **Reino Unido** y los **Países Nórdicos**. | 🌐 *Máximo Gasto por Procedencia* |
| **H2: Concentración del Gasto** | El **Alojamiento** concentra el mayor porcentaje del gasto total del turista. | 🏨 *Distribución Porcentual del Gasto* |
| **H3: Liderazgo Insular** | **Tenerife** lidera el gasto turístico diario medio durante la mayoría de los años. | 🏝️ *Valor Máximo por Año e Isla* |
| **H4: Recuperación Post-Pandemia** | Se confirma una **recuperación progresiva (2021–2024)** tras la caída de 2020. | 📈 *Evolución del Gasto Total* |

---

## 🗂️ 3. Estructura del Proyecto

Esta es la estructura **real** del proyecto, con los scripts `.py` ubicados en la carpeta principal `EDA`:

EDA/
│
├── data/
│ └── gastoxturistaxdia.csv # Fuente de datos (ISTAC)
│
├── img/ # Gráficos e imágenes generadas
│ ├── Islas-Canarias-Collage.jpg # Imagen de portada
│ ├── grafico_h1.png
│ ├── grafico_h2.png
│ ├── grafico_h3.png
│ └── grafico_h4.png
│
├── notebooks/ # Notebooks Jupyter de desarrollo
│ ├── 0-Enunciado_EDA.ipynb
│ ├── Memoria.ipynb
│ ├── Turismo_Canarias_presentación.ipynb
│ └── Un_viaje_desarrollo.ipynb
│
├── funciones.py # Funciones de cálculo, EDA y visualización
├── variables.py # Variables globales, rutas y constantes
├── main.py # Script principal de ejecución
├── README.md # Documentación del proyecto
└── requirements.txt # Dependencias del entorno

yaml
Copiar código

---

## ⚙️ 4. Requisitos e Instalación

**Requisitos mínimos:**
- 🐍 Python 3.10 o superior  
- 📦 Librerías: `pandas`, `numpy`, `matplotlib`, `seaborn`

### Instalación rápida

```bash
pip install pandas numpy matplotlib seaborn
🚀 5. Ejecución del Análisis
Ejecuta el proyecto desde el directorio principal EDA:

bash
Copiar código
cd "C:\Users\balle\Desktop\DataScience\apuntesPatricia\2-Data_Analysis\proyecto_EDA\EDA"
python main.py
El script:

📥 Carga los datos desde data/gastoxturistaxdia.csv.

🧹 Limpia y normaliza los datos.

🧮 Calcula las cuatro hipótesis (H1–H4).

📊 Genera los gráficos correspondientes.

💾 Guarda automáticamente los resultados en img/.

📈 6. Resultados y Visualizaciones
Código	Tipo de Gráfico	Descripción	Archivo
H1	🌐 Barras	Compara el gasto máximo por procedencia. Destaca el papel del turista nórdico/británico.	img/grafico_h1.png
H2	🏨 Barras	Distribuye el gasto total por categorías. Muestra el peso del alojamiento.	img/grafico_h2.png
H3	🏝️ Barras	Muestra la isla con el mayor gasto medio diario cada año.	img/grafico_h3.png
H4	📉 Línea	Representa la evolución temporal del gasto total (2018–2025).	img/grafico_h4.png

💬 7. Conclusiones Generales
🌐 Reino Unido y los Países Nórdicos son los principales impulsores del gasto medio diario.

🏨 El Alojamiento sigue siendo la partida de gasto dominante.

🏝️ Tenerife y Gran Canaria lideran en gasto medio por turista.

📉 El año 2020 marca un descenso histórico debido al impacto de la pandemia.

📈 Desde 2021, se consolida una recuperación sostenida hasta alcanzar máximos en 2025.

✍️ 8. Autora
Patricia Ballesteros
Proyecto de Análisis Exploratorio de Datos (EDA) – Turismo en Canarias
Data Science | Python | Visualización de Datos
📍 Gazteiz, Araba · 🗓️ 2025


