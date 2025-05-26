import sqlite3
produkte_mock_daten = [
    {
        "name": "Raspberry Pi 5",
        "short_description": "Mini-Computer für Bastler",
        "product_description": "Der neueste Raspberry Pi 5 mit 8GB RAM, ideal für DIY-Projekte, Home Automation und Retro-Gaming.",
        "stock": 42,
        "price": 89.99
    },
    {
        "name": "Mechanische Tastatur (QMK)",
        "short_description": "Programmierbare Tastatur",
        "product_description": "Hot-Swap-fähige mechanische Tastatur mit QMK-Firmware, RGB-Beleuchtung und Gateron-Switches.",
        "stock": 30,
        "price": 129.99
    },
    {
        "name": "Arduino Starter Kit",
        "short_description": "Elektronik-Bausatz",
        "product_description": "Komplettes Arduino-Starterkit mit UNO-Board, Sensoren, LEDs und Anleitungen für Maker und Nerds.",
        "stock": 55,
        "price": 59.99
    },
    {
        "name": "3D-Drucker (Prusa Mini+)",
        "short_description": "Kompakter 3D-Drucker",
        "product_description": "Prusa Mini+ 3D-Drucker für präzise und zuverlässige Drucke, perfekt für Prototyping und Cosplay.",
        "stock": 12,
        "price": 429.00
    },
    {
        "name": "USB-Raketenwerfer",
        "short_description": "Gadget für den Schreibtisch",
        "product_description": "USB-gesteuerter Raketenwerfer für den ultimativen Spaß im Büro – steuerbar per Software.",
        "stock": 77,
        "price": 24.99
    }
]


# Establish connection to the SQLite3 database
conn = sqlite3.connect('db.sqlite3')

# Optional: create a cursor object
cursor = conn.cursor()


for produkt in produkte_mock_daten:
    cursor.execute(
        """
        INSERT INTO api_products (name, short_description, product_description, stock, price)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            produkt["name"],
            produkt["short_description"],
            produkt["product_description"],
            produkt["stock"],
            produkt["price"]
        )
    )


conn.commit()

# Don't forget to close the connection when done
# conn.close()