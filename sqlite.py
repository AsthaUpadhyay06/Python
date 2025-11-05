import sqlite3

con = sqlite3.connect("test.db")
cur = con.cursor()

# create table
cur.execute("CREATE TABLE IF NOT EXISTS students(id INTEGER, name TEXT)")

# insert data
cur.execute("INSERT INTO students VALUES (1, 'Astha')")
cur.execute("INSERT INTO students VALUES (2, 'Priya')")
con.commit()

# fetch data
cur.execute("SELECT * FROM students")
rows = cur.fetchall()
for r in rows:
    print(r)

con.close()
