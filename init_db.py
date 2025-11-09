import sqlite3

# Create database connection
conn = sqlite3.connect("menuu.db")
cursor = conn.cursor()

# Create kategoriler table
cursor.execute("""
CREATE TABLE IF NOT EXISTS kategoriler (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    image TEXT
)
""")

# Create menuu table with all required fields
cursor.execute("""
CREATE TABLE IF NOT EXISTS menuu (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    category TEXT NOT NULL,
    description TEXT,
    image TEXT
)
""")

# Commit changes and close
conn.commit()
conn.close()

print("Database initialized successfully!")
