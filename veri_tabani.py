import sqlite3

baglanti = sqlite3.connect("menuu.db")

baglanti.execute(""" 
CREATE TABLE  IF NOT EXISTS menuu (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    category TEXT
)
""")

baglanti.commit()
baglanti.close()

def delete_menu_item(item_id):
    conn = sqlite3.connect("menuu.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM menuu WHERE id = ?", (item_id,))
    conn.commit()
    conn.close