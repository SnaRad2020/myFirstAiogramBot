import sqlite3 as sq


db = sq.connect('Database/teleDatabase')
cur = db.cursor()


async def db_start():
    cur.execute('CREATE TABLE IF NOT EXISTS accounts('
                'id INTEGER PRIMARY KEY AUTOINCREMENT, '
                'cart_id TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS items('
                'i_id INTEGER PRIMARY KEY AUTOINCREMENT, '
                'name TEXT'
                'url TEXT)')
    db.commit()