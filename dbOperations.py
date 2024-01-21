from db_connection import Database

db = Database()


def readparticipants():
    db.connect()
    query = 'SELECT * FROM eventmanager.people;'
    cursor = db.conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    db.disconnect()
    return results


def update_presence(participant_id, presence):
    db.connect()
    query = 'UPDATE eventmanager.people SET presence = %s WHERE id= %s'
    cursor = db.conn.cursor()
    cursor.execute(query, (presence, participant_id))
    db.conn.commit()
    db.disconnect()


def inventory_request(table):
    db.connect()
    query = 'SELECT * FROM eventmanager.%s'
    cursor = db.conn.cursor()
    cursor.execute(query % (table,))
    results = cursor.fetchall()
    db.disconnect()
    return results


def manage_qt(idn, qt):
    db.connect()
    print(idn)
    print(qt)
    query = 'UPDATE eventmanager.alcohol SET quantity = %s WHERE idalcohol = %s'
    cursor = db.conn.cursor()
    cursor.execute(query, (qt, idn))
    db.conn.commit()
    db.disconnect()


