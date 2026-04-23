import sqlite3
def get_connection():
    return sqlite3.connect('users.db')

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users(ID INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT not null, password TEXT NOT NULL,
                    username TEXT NOT NULL, email TEXT NOT NULL)''')
    conn.commit()
    conn.close()

