import json
import xlsxwriter
import pandas as pd

# Read directly from a file path
df = pd.read_json('Tasas.json')

# 2. Initialize the Excel writer with xlsxwriter engine
file_name = "output.xlsx"
writer = pd.ExcelWriter(file_name, engine="xlsxwriter")

# 3. Convert dataframe to Excel (turn off default index & headers so they don't duplicate)
df.to_excel(writer, sheet_name="Tasas", startrow=1, header=False, index=False)

# 4. Get the xlsxwriter workbook and worksheet objects
workbook  = writer.book
worksheet = writer.sheets["Tasas"]

# 5. Define the table range boundaries
# We map dynamically based on dataframe dimensions
(max_row, max_col) = df.shape
column_settings = [{"header": column} for column in df.columns]

# 6. Add the Excel Table structure
worksheet.add_table(0, 0, max_row, max_col - 1, {
    "columns": column_settings,
    "style": "TableStyleMedium9"  # Standard built-in Excel theme
})

# Save and close
writer.close()
print(f"Table created successfully in {file_name}!")



