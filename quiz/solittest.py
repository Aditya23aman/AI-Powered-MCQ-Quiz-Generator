import sqlite3
conn = sqlite3.connect('questions.db')
cursor = conn.cursor()

#create table if it doesn't exist
cursor.execute('SELECT first FROM questions ORDER BY id')
data = cursor.fetchall()
print(data[])


print(type(data))

conn.commit()
conn.close()

