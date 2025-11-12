# variables.py

# --- RUTAS ---
RUTA_CSV = r"C:\Users\balle\Desktop\DataScience\apuntesPatricia\2-Data_Analysis\EDA\data\gastoxturistaxdia.csv"
RUTA_IMG = r"C:\Users\balle\Desktop\DataScience\apuntesPatricia\2-Data_Analysis\EDA\img"

# --- COLUMNAS ---
AÑOS = ['2025', '2024', '2023', '2022', '2021', '2020', '2019', '2018']
COLUMNAS_FIJAS = ['gasto', 'territorio', 'procedencia']

# --- FILTROS ---
ELIMINAR = ["alimentación", "servicios auxiliares", "gasto principal del alojamiento"]
PROCEDENCIAS = ['españa (excluida canarias)', 'alemania', 'países bajos',
                'países nórdicos', 'reino unido', 'otros']
TERRITORIOS = ["Lanzarote", "Fuerteventura", "Gran Canaria", "Tenerife", "La Palma"]

# --- COLORES ---
PALETA_PROCEDENCIA = {
    "reino unido": "#f4a261",
    "países nórdicos": "#5dade2"
}

PALETA_ISLAS = {
    'Tenerife': '#6baed6',
    'Fuerteventura': '#FFEA00',
    'Gran Canaria': '#ff7f0e',
    'Lanzarote': '#a6cee3',
    'La Palma': '#b2df8a'
}

# --- CONFIGURACIÓN DE TIEMPO ---
TIEMPO_ENTRE_GRAFICOS = None  # None = mostrar hasta que el usuario cierre la ventana