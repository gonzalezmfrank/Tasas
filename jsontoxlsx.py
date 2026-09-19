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
    for col in df.columns:
        # Intentar convertir a fecha, ignorando errores
        try:
            df[col] = pd.to_datetime(df[col], errors='ignore', utc=False)
            print(f"Columna convertida a fecha: {col}")
        except Exception:
            pass
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

    # Detectar y convertir fechas
    df = detectar_y_convertir_fechas(df)

    # Guardar en Excel con formato de fecha
    with pd.ExcelWriter(excel_file, engine='xlsxwriter', datetime_format='yyyy-mm-dd', date_format='yyyy-mm-dd') as writer:
        df.to_excel(writer, index=False)

    print(f"Archivo Excel generado: {excel_file}")


# Read directly from a file path
#df = pd.read_json('Tasas.json')

# 2. Initialize the Excel writer with xlsxwriter engine
#file_name = "output.xlsx"
#writer = pd.ExcelWriter(file_name, engine="xlsxwriter")

# 3. Convert dataframe to Excel (turn off default index & headers so they don't duplicate)
#df.to_excel(writer, sheet_name="Tasas", startrow=1, header=False, index=False)

# 4. Get the xlsxwriter workbook and worksheet objects
#workbook  = writer.book
#worksheet = writer.sheets["Tasas"]

# 5. Define the table range boundaries
# We map dynamically based on dataframe dimensions
#(max_row, max_col) = df.shape
#column_settings = [{"header": column} for column in df.columns]

# 6. Add the Excel Table structure
#worksheet.add_table(0, 0, max_row, max_col - 1, {
#    "columns": column_settings,
#    "style": "TableStyleMedium9"  # Standard built-in Excel theme
#})

# Save and close
#writer.close()
#print(f"Table created successfully in {file_name}!")

# Ejemplo de uso
if __name__ == "__main__":
    try:
        json_a_excel("Tasas.json", "resultado.xlsx")
    except Exception as e:
        print(f"Error: {e}")

