import sqlite3

DB_NAME = 'BotUsers.db'


def access_to_db(name_db):
    with sqlite3.connect(name_db) as connection:
        return connection


def create_users_table():
    db = access_to_db(DB_NAME)
    db.cursor().execute('''
    CREATE TABLE IF NOT EXISTS Users(
    tg_id INTEGER PRIMARY KEY,
    phone TEXT,
    name TEXT,
    username TEXT
    )''')
    db.commit()


def save_user_to_db(tg_id, phone, name, username):
    db = access_to_db(DB_NAME)
    db.cursor().execute('INSERT OR REPLACE INTO Users (tg_id, phone, name, username) VALUES (?, ?, ?, ?)', (tg_id, phone, name, username))
    db.commit()


def get_all_users():
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT tg_id, name FROM Users')
        users = cursor.fetchall()
        return users


# create_users_table()
# print(get_all_users())
