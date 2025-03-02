import requests
import json
import pandas as pd


WC_API_URL = "https://wallner.bio/wp-json/wc/v3/products"
CONSUMER_KEY = "ck_1ea2be6e6959fc4351a72123ebf1069b426a190e"
CONSUMER_SECRET = "cs_e3e0bd3789f3d95d3e1e6f28991a18b8ae197d53"

df = pd.read_csv("produkte.csv")

for index, row in df.iterrows():
    sku = str(row["sku"])
    update_data = {
        "regular_price": str(row["VK0"])
    }

    response = requests.get(
        WC_API_URL,
        auth=(CONSUMER_KEY, CONSUMER_SECRET),
        params={"sku": sku}  
    )

    if response.status_code == 200 and isinstance(response.json(), list) and len(response.json()) > 0:
        product_id = response.json()[0]["id"]

        response = requests.put(
            f"{WC_API_URL}/{product_id}",
            auth=(CONSUMER_KEY, CONSUMER_SECRET),
            headers={"Content-Type": "application/json"},
            data=json.dumps(update_data)
        )

        if response.status_code == 200:
            print(f"✅ Produkt {sku} erfolgreich aktualisiert: Neuer Preis {row['VK0']}")
        else:
            print(f"❌ Fehler beim Aktualisieren von Produkt {sku}: {response.status_code} - {response.text}")
    else:
        print(f"❌ Kein Produkt mit SKU {sku} gefunden.")

print("🚀 Alle Produkte wurden verarbeitet!")
