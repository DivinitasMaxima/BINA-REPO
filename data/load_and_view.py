import pandas as pd

# CSV-Datei einlesen (Pfad und Dateiname anpassen falls nötig)
df = pd.read_csv('data/Invistico_Airline.csv')

# Vorschau auf die ersten 5 Zeilen
print("📋 Erste Einträge im Dataset:")
print(df.head())

# Zeige alle Spaltennamen
print("\n🧱 Spalten im Datensatz:")
print(df.columns.tolist())