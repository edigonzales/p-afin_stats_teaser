import random

# Funktion zur Generierung der Werte
def generate_values(start_year, end_year, start_value, end_value):
    years = range(start_year, end_year + 1)
    values = []
    current_value = start_value
    for year in years:
        values.append((year, current_value))
        # Leichte Zunahme mit gelegentlichen Rückgängen
        if random.random() < 0.85:  # 85% Chance auf Zunahme
            current_value += random.randint(0, 5)
        else:
            current_value -= random.randint(0, 5)
        # Sicherstellen, dass der Wert nicht negativ wird
        current_value = max(current_value, 0)
    return values

# Daten für 2024
data_2024 = [
    ("Bezirk Bucheggberg", "SO", "Leichte Motorwagen", 6286),
    ("Bezirk Bucheggberg", "SO", "Schwere Motorwagen", 51),
    ("Bezirk Bucheggberg", "SO", "Anhänger", 837),
    ("Bezirk Bucheggberg", "SO", "Landw. FZ Ind. Trak.", 703),
    ("Bezirk Bucheggberg", "SO", "Motorräder", 936),
    ("Bezirk Bucheggberg", "SO", "Klein-Motorräder", 24),
    ("Bezirk Bucheggberg", "SO", "Gewerbe FZ", 127),
    ("Bezirk Dorneck", "SO", "Leichte Motorwagen", 13452),
    ("Bezirk Dorneck", "SO", "Schwere Motorwagen", 220),
    ("Bezirk Dorneck", "SO", "Anhänger", 1332),
    ("Bezirk Dorneck", "SO", "Landw. FZ Ind. Trak.", 759),
    ("Bezirk Dorneck", "SO", "Motorräder", 2144),
    ("Bezirk Dorneck", "SO", "Klein-Motorräder", 53),
    ("Bezirk Dorneck", "SO", "Gewerbe FZ", 127),
    ("Bezirk Gäu", "SO", "Leichte Motorwagen", 17446),
    ("Bezirk Gäu", "SO", "Schwere Motorwagen", 888),
    ("Bezirk Gäu", "SO", "Anhänger", 2162),
    ("Bezirk Gäu", "SO", "Landw. FZ Ind. Trak.", 478),
    ("Bezirk Gäu", "SO", "Motorräder", 1587),
    ("Bezirk Gäu", "SO", "Klein-Motorräder", 275),
    ("Bezirk Gäu", "SO", "Gewerbe FZ", 365),
    ("Bezirk Gösgen", "SO", "Leichte Motorwagen", 15506),
    ("Bezirk Gösgen", "SO", "Schwere Motorwagen", 147),
    ("Bezirk Gösgen", "SO", "Anhänger", 1306),
    ("Bezirk Gösgen", "SO", "Landw. FZ Ind. Trak.", 542),
    ("Bezirk Gösgen", "SO", "Motorräder", 2224),
    ("Bezirk Gösgen", "SO", "Klein-Motorräder", 87),
    ("Bezirk Gösgen", "SO", "Gewerbe FZ", 178),
    ("Bezirk Lebern", "SO", "Leichte Motorwagen", 30715),
    ("Bezirk Lebern", "SO", "Schwere Motorwagen", 290),
    ("Bezirk Lebern", "SO", "Anhänger", 2005),
    ("Bezirk Lebern", "SO", "Landw. FZ Ind. Trak.", 669),
    ("Bezirk Lebern", "SO", "Motorräder", 3446),
    ("Bezirk Lebern", "SO", "Klein-Motorräder", 153),
    ("Bezirk Lebern", "SO", "Gewerbe FZ", 333),
    ("Bezirk Olten", "SO", "Leichte Motorwagen", 34842),
    ("Bezirk Olten", "SO", "Schwere Motorwagen", 913),
    ("Bezirk Olten", "SO", "Anhänger", 2628),
    ("Bezirk Olten", "SO", "Landw. FZ Ind. Trak.", 568),
    ("Bezirk Olten", "SO", "Motorräder", 4094),
    ("Bezirk Olten", "SO", "Klein-Motorräder", 140),
    ("Bezirk Olten", "SO", "Gewerbe FZ", 464),
    ("Bezirk Solothurn", "SO", "Leichte Motorwagen", 10289),
    ("Bezirk Solothurn", "SO", "Schwere Motorwagen", 71),
    ("Bezirk Solothurn", "SO", "Anhänger", 561),
    ("Bezirk Solothurn", "SO", "Landw. FZ Ind. Trak.", 36),
    ("Bezirk Solothurn", "SO", "Motorräder", 889),
    ("Bezirk Solothurn", "SO", "Klein-Motorräder", 33),
    ("Bezirk Solothurn", "SO", "Gewerbe FZ", 187),
    ("Bezirk Thal", "SO", "Leichte Motorwagen", 10737),
    ("Bezirk Thal", "SO", "Schwere Motorwagen", 152),
    ("Bezirk Thal", "SO", "Anhänger", 1453),
    ("Bezirk Thal", "SO", "Landw. FZ Ind. Trak.", 870),
    ("Bezirk Thal", "SO", "Motorräder", 1162),
    ("Bezirk Thal", "SO", "Klein-Motorräder", 48),
    ("Bezirk Thal", "SO", "Gewerbe FZ", 188),
    ("Bezirk Thierstein", "SO", "Leichte Motorwagen", 10848),
    ("Bezirk Thierstein", "SO", "Schwere Motorwagen", 204),
    ("Bezirk Thierstein", "SO", "Anhänger", 1511),
    ("Bezirk Thierstein", "SO", "Landw. FZ Ind. Trak.", 698),
    ("Bezirk Thierstein", "SO", "Motorräder", 1717),
    ("Bezirk Thierstein", "SO", "Klein-Motorräder", 52),
    ("Bezirk Thierstein", "SO", "Gewerbe FZ", 287),
    ("Bezirk Wasseramt", "SO", "Leichte Motorwagen", 35846),
    ("Bezirk Wasseramt", "SO", "Schwere Motorwagen", 318),
    ("Bezirk Wasseramt", "SO", "Anhänger", 2657),
    ("Bezirk Wasseramt", "SO", "Landw. FZ Ind. Trak.", 768),
    ("Bezirk Wasseramt", "SO", "Motorräder", 4116),
    ("Bezirk Wasseramt", "SO", "Klein-Motorräder", 160),
    ("Bezirk Wasseramt", "SO", "Gewerbe FZ", 399)
]

# Generiere Werte für die Jahre 1990 bis 2023
for entry in data_2024:
    bezirk, kanton, typ, wert_2024 = entry
    start_value = wert_2024 - (2024 - 1990) * 10  # Annahme: Startwert ist niedriger
    values = generate_values(1990, 2023, start_value, wert_2024)
    for year, value in values:
        print(f"{year}\t{bezirk}\t{kanton}\t{typ}\t{value}")