from multiprocessing import connection
import sqlite3

connection=sqlite3.connect('data.db')
cursor=connection.cursor()

create_table= "CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, name TEXT)"

cursor.execute(create_table)

connection.commit()

connection.close()