import sqlite3 as sq


db = sq.connect('Database/teleDatabase.db')
cur = db.cursor()


async def db_start():
    cur.execute('CREATE TABLE IF NOT EXISTS accounts('
                'id INTEGER PRIMARY KEY AUTOINCREMENT, '
                'tg_id INTEGER, '
                'cart_id TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS items('
                'i_id INTEGER PRIMARY KEY AUTOINCREMENT, '
                'name TEXT, '
                'url TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS admins('
                'a_id INTEGER PRIMARY KEY AUTOINCREMENT, '
                'tg_id INTEGER)')
    db.commit()

async def cmd_start_db(user_id):
    user = cur.execute('SELECT * FROM accounts WHERE tg_id == {key}'.format(key=user_id)).fetchone()
    if not user:
        cur.execute('INSERT tg_id INTO accounts VALUES {key}'.format(key=user_id))
        db.commit()