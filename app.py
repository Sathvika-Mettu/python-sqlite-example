import sqlite3
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
# create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
# insert a record
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Alice', 30))
# commit changes
conn.commit()
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)
# close connection
conn.close()