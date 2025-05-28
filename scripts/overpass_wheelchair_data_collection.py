import overpy
import csv
from pathlib import Path
import os

api = overpy.Overpass()

result = api.query("""
    area[name="Москва"]->.searchArea;
    node[wheelchair=yes](area.searchArea);
    out body;
""")

project_root = Path(__file__).resolve().parent.parent
data_dir = project_root / "data"
data_dir.mkdir(exist_ok=True)
csv_path = data_dir / "wheelchair_accessible.csv"

try:
    with open(csv_path, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        # Заголовки
        writer.writerow([
            "ID", "Latitude", "Longitude", "Name", "Amenity", "Shop",
            "Wheelchair", "Street", "House Number", "City", "Postcode"
        ])

        for node in result.nodes:
            writer.writerow([
                node.id,
                node.lat,
                node.lon,
                node.tags.get("name", ""),
                node.tags.get("amenity", ""),
                node.tags.get("shop", ""),
                node.tags.get("wheelchair", ""),
                node.tags.get("addr:street", ""),
                node.tags.get("addr:housenumber", ""),
                node.tags.get("addr:city", ""),
                node.tags.get("addr:postcode", "")
            ])
except IOError as e:
    print(f"Ошибка при записи файла: {e}")

