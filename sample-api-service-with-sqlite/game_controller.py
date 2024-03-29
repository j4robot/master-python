from db import get_db

def insert_game(name, price, rate):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO games(name, price, rate) VALUES (?, ?, ?)"
    cursor.execute(statement, [name, price, rate])
    db.commit()
    return True


def update_game(id, name, price, rate):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE games SET name = ?, price = ?, rate = ? WHERE id = ?"
    cursor.execute(statement, [name, price, rate, id])
    db.commit()
    return True


def delete_game(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM games WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True


def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id, name, price, rate FROM games WHERE id = ?"
    cursor.execute(statement, [id])
    return cursor.fetchone()

'''
for row in cur.execute('SELECT * FROM stocks ORDER BY price'):
        print(row)

'''
def get_games():
    temp = []
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, name, price, rate FROM games"
    for row in cursor.execute(query):
        data = {'id': row[0], 'name': row[1], 'price': row[2], 'rate': row[3]}
        temp.append(data)
    #cursor.execute(query)
    return temp #cursor.fetchall()