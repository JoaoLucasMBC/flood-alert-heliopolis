import sqlite3

conn = sqlite3.connect('database/db_alert.db')

conn.execute('''CREATE TABLE usuarios
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            regiao TEXT NOT NULL,
            numero TEXT NOT NULL)''')

conn.close()