import json
import xlsxwriter
import pandas as pd

from dateutil import parser
import json
import os

def detectar_y_convertir_fechas(df):
    """
    Detecta columnas con formato de fecha y las convierte a tipo datetime.
    """
    df['Fecha_Proceso'] = pd.to_datetime(df['Fecha_Proceso'], errors='coerce')
    df['Fecha_Valor'] = pd.to_datetime(df['Fecha_Valor'], errors='coerce')
    return df


def json_a_excel(json_file, excel_file):
    """
    Convierte un archivo JSON a Excel, manejando formatos de fecha.
    """
    if not os.path.exists(json_file):
        raise FileNotFoundError(f"El archivo {json_file} no existe.")

    # Leer JSON
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Convertir a DataFrame
    df = pd.json_normalize(data)  # Soporta JSON anidado

    print (f"DataFrame generado con {len(df)} filas y {len(df.columns)} columnas.")

    # Detectar y convertir fechas
    df = detectar_y_convertir_fechas(df)

    # Guardar en Excel con formato de fecha
    with pd.ExcelWriter(excel_file, engine='xlsxwriter', datetime_format='yyyy-mm-dd', date_format='yyyy-mm-dd') as writer:
        df.to_excel(writer, index=False)

    print(f"Archivo Excel generado: {excel_file}")

# Ejemplo de uso
if __name__ == "__main__":
    try:
        json_a_excel("Tasas.json", "Tasas.xlsx")
    except Exception as e:
        print(f"Error: {e}")

