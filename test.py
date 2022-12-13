import sqlite3

conn = sqlite3.connect("D:/MySpace/Learn Python/instance/bookstore.db")

cur = conn.cursor()
cur.execute("SELECT * FROM Users")
rows = cur.fetchall()
print(rows[0])