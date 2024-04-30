import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO persona (nome, cognome) VALUES (?, ?)",
            ('John', 'Doe')
            )

cur.execute("INSERT INTO test (name, surname) VALUES (?, ?)",
            ('Jane', 'Doe')
            )

data = cur.execute("SELECT * FROM persona")

print(data.fetchall())

connection.commit()
connection.close()