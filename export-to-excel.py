import pyodbc
import pandas as pd

server = "BÜRO-COMPUTER"
database = "BOArt"
username = ""
password = ""

conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};trusted_connection=True')

query = """
SELECT 
    Verkauf.EAN,
    Verkauf.VK0,
    Verkauf.Internet,
    Artikel.VKArtNr As sku
FROM
    Verkauf
INNER JOIN
    Artikel ON Verkauf.EAN = Artikel.EAN
WHERE
    Verkauf.Internet = 1;
"""

df = pd.read_sql(query, conn)

csv_file = "produkte.csv"
df.to_csv(csv_file, index=False)

print(f"CSV-Datei '{csv_file}' wurde erstellt!")
