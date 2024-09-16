import sqlite3

conn = sqlite3.connect('concerts.db')
cursor = conn.cursor()

# Your SQL operations here

conn.close()
