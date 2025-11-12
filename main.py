# main.py

from funciones import *

def main():
    print("Cargando y preparando datos...")
    df = cargar_datos()
    df = limpiar_y_preparar(df)
    df_final = filtrar_datos(df)
    print("Datos preparados correctamente.\n")

    # H1 – Procedencia con mayor gasto
    print("Generando gráfico H1 (procedencia con mayor gasto)...")
    df_h1 = calcular_h1(df_final)
    grafico_h1(df_h1)
    print("Gráfico H1 completado.\n")

    # H2 – Distribución porcentual del gasto
    print("Generando gráfico H2 (distribución porcentual del gasto)...")
    df_h2 = calcular_h2(df_final)
    grafico_h2(df_h2)
    print("Gráfico H2 completado.\n")

    # H3 – Isla con mayor gasto
    print("Generando gráfico H3 (isla con mayor gasto)...")
    df_h3 = calcular_h3(df_final)
    grafico_h3(df_h3)
    print("Gráfico H3 completado.\n")

    # H4 – Evolución temporal del gasto total
    print("Generando gráfico H4 (evolución temporal del gasto total)...")
    df_h4 = calcular_h4(df_final)
    grafico_h4(df_h4)
    print("Gráfico H4 completado.\n")

    print("Todos los gráficos se han mostrado y guardado correctamente en:")
    print(RUTA_IMG)

if __name__ == "__main__":
    main()
