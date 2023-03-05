from sqlite3 import *

with connect('database.db') as db:
    cursor = db.cursor()
    query = """ CREATE TABLE IF NOT EXISTS table1(id INTEGER, name TEXT,  expenses TEXT )"""
    cursor.execute(query)
cursor.execute("""  INSERT INTO table1 ( id, name, expenses) VALUES('1', 'John', 32) """)
cursor.execute("""  INSERT INTO table1 ( id, name, expenses) VALUES('2', 'Richard', 56) """)
cursor.execute("""  INSERT INTO table1 ( id, name, expenses) VALUES('3', 'Arnold', 29) """)
cursor.execute("""  INSERT INTO table1 ( id, name, expenses) VALUES('4', 'Sveta', 71) """)

db.commit()


def information():
    cursor.execute("SELECT * FROM table1")
    return cursor.fetchall()

#функция изменения в бд(костыльная)
def cnangeDB(event):
    id_polz = input('Нужный id \n')
    command = input('Изменение имени(1) или Изменение Расходов(2) \n')
    if command == '1':
        name_polz = input('Изменить имя пользователя\n')
        cursor.execute("""Update table1 set name = ? where id = ? """, (name_polz, id_polz))
        print('\nUpdating...\n')
        db.commit()
    elif command == '2':
        expenses_polz = input('Изменить имя пользователя\n')
        cursor.execute("""Update table1 set expenses = ? where id = ? """, (expenses_polz, id_polz))
        print('\nUpdating...\n')
        db.commit()


