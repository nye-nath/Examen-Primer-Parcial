

Este proyecto realiza la ingesta, procesamiento y análisis estadístico de lecturas térmicas provenientes de sensores en instalaciones industriales.



- `data/`: Contiene el conjunto de datos de entrada (`sensores_industriales.csv`).
- `resultados/`: Almacena el archivo generado con las alertas de sobrecalentamiento (`alertas.csv`).
- `evidencias/`: Capturas y respaldos de la ejecución del proyecto.
- `analisis.py`: Script principal en Python para el procesamiento de datos.
- `requirements.txt`: Lista de dependencias del entorno virtual.



- **Total de registros procesados:** 100,000
- **Sensores únicos monitoreados:** 40
- **Temperatura promedio por planta:**
  - Planta 1: 66.62 °C
  - Planta 2: 66.53 °C
  - Planta 3: 66.77 °C
  - Planta 4: 66.67 °C
- **Temperatura máxima registrada:** 104.99 °C
- **Alertas de sobrecalentamiento (> 85 °C):** 6,954 lecturas
- **Planta crítica con mayor número de alertas:** Planta_3 (1,777 alertas)



1. Clonar el repositorio:
   ```bash
   git clone [https://github.com/nye-nath/Examen-Primer-Parcial.git](https://github.com/nye-nath/Examen-Primer-Parcial.git)
   cd Examen-Primer-Parci
