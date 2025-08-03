import sqlite3

conn = sqlite3.connect('users.db')
conn.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password BLOB NOT NULL
)
''')
conn.close()

print("Database initialized.")
