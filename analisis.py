import os
import pandas as pd

def analizar_datos():
    # Definición de rutas relativas
    ruta_csv = os.path.join("data", "sensores_industriales.csv")
    carpeta_resultados = "resultados"
    ruta_alertas = os.path.join(carpeta_resultados, "alertas.csv")

    # Verificar existencia del archivo
    if not os.path.exists(ruta_csv):
        print(f"Error: No se encontró el archivo de datos en '{ruta_csv}'.")
        return

    # Cargar datos
    df = pd.read_csv(ruta_csv)

    print("=== RESULTADOS DEL ANÁLISIS DE SENSORES ===\n")

    # 1. Total de registros y de sensores distintos
    total_registros = len(df)
    sensores_unicos = df["id_sensor"].nunique()
    print(f"1. Cantidad total de registros: {total_registros:,}")
    print(f"   Cantidad de sensores distintos: {sensores_unicos}\n")

    # 2. Temperatura promedio de cada planta
    promedio_planta = df.groupby("planta")["temperatura_c"].mean()
    print("2. Temperatura promedio por planta (°C):")
    for planta, prom in promedio_planta.items():
        print(f"   - Planta {planta}: {prom:.2f} °C")
    print()

    # 3. Temperatura máxima, sensor y fecha correspondientes
    temp_max = df["temperatura_c"].max()
    registros_max = df[df["temperatura_c"] == temp_max]
    print(f"3. Temperatura máxima registrada: {temp_max} °C")
    for _, fila in registros_max.iterrows():
        print(f"   - Sensor: {fila['id_sensor']} | Fecha/Hora: {fila['fecha_hora']} | Planta: {fila['planta']}")
    print()

    # 4. Lecturas con temperatura mayor a 85 °C (Alertas)
    df_alertas = df[df["temperatura_c"] > 85]
    total_alertas = len(df_alertas)
    print(f"4. Total de lecturas con alerta (> 85 °C): {total_alertas:,}\n")

    # 5. Planta con más alertas de temperatura (maneja empates)
    alertas_por_planta = df_alertas["planta"].value_counts()
    if not alertas_por_planta.empty:
        max_alertas = alertas_por_planta.max()
        plantas_top = alertas_por_planta[alertas_por_planta == max_alertas].index.tolist()
        plantas_str = ", ".join(map(str, plantas_top))
        print(f"5. Planta(s) con más alertas de temperatura ({max_alertas} alertas): {plantas_str}\n")
    else:
        print("5. No se registraron alertas mayores a 85 °C.\n")

    # 6. Exportar lecturas con alerta conservando columnas originales
    os.makedirs(carpeta_resultados, exist_ok=True)
    df_alertas.to_csv(ruta_alertas, index=False)
    print(f"6. Archivo de alertas exportado con éxito a: '{ruta_alertas}'")

if __name__ == "__main__":
    analizar_datos()
