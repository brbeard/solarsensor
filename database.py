import sqlite3
import datetime

def init():
    conn = sqlite3.connect('sensor.sqlite3')
    create_table(conn)
    conn.close()


def create_table(conn):
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS answers (takenat TIMESTAMP, temperature INTEGER, humidity INTEGER)''')
    conn.commit()

def add_new(temperature, humidity):
    conn = sqlite3.connect('sensor.sqlite3')
    now = datetime.datetime.now().ctime()
    c = conn.cursor()
    c.execute('''INSERT INTO answers (takenat, temperature,humidity ) VALUES (?,?,?)''', (now[8:16],temperature,humidity))
    conn.commit()

def read_table():
    conn = sqlite3.connect('sensor.sqlite3')
    c = conn.cursor()
    c.execute(''' SELECT * FROM answers ''')
    rows = c.fetchall()

    for row in rows:
        print(row)


def read_line():
    conn = sqlite3.connect('sensor.sqlite3')
    c = conn.cursor()
    c.execute(''' SELECT * FROM answers ''')
    rows = c.fetchone()

def delete_table():
    conn = sqlite3.connect('sensor.sqlite3')
    c = conn.cursor()
    c.execute('''DROP TABLE answers''')
    conn.commit()

    
