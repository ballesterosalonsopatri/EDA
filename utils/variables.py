
# variables.py

# Columnas de años
AÑOS = ['2025','2024','2023','2022','2021','2020','2019','2018']

# Columnas fijas del DataFrame
COLUMNAS_FIJAS = ['gasto', 'territorio', 'procedencia']

# Elementos a eliminar
ELIMINAR = ["alimentación", "servicios auxiliares", "gasto principal del alojamiento"]

# Procedencias seleccionadas
PROCEDENCIAS = [
    'españa (excluida canarias)', 'alemania', 'países bajos',
    'países nórdicos', 'reino unido', 'otros'
]

# Territorios de interés
TERRITORIOS = ["Lanzarote", "Fuerteventura", "Gran Canaria", "Tenerife", "La Palma"]

# Paletas de colores personalizadas
PALETA_PROCEDENCIA = {
    "reino unido": "#f4a261",       # naranja claro
    "países nórdicos": "#5dade2"    # azul suave
}

PALETA_ISLAS = {
    'Tenerife': '#6baed6',
    'Fuerteventura': '#FFEA00',
    'Gran Canaria': '#ff7f0e',
    'Lanzarote': '#a6cee3',
    'La Palma': '#b2df8a'
}