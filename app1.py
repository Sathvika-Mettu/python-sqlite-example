import sqlite3
connection = sqlite3.connect("example.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE student_dFs(id INTEGER PRIMARY KEY, name TEXT, grade REAL)")
cursor.execute("INSERT INTO student_dFs(name,grade) VALUES(?,?) VALUES(?,?)",('Tarun', 77.9),('Sam',99.99))
cursor.execute("SELECT * FROM student_dFs")
rows = cursor.fetchall()
for row in rows:
    print(row)
connection.commit()
connection.close()
