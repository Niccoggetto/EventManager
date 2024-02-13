from db_connection import Database
from Gestionale.cocktails import *

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


def update_payment(participant_id, payment):
    db.connect()
    query = 'UPDATE eventmanager.people SET paid = %s WHERE id= %s'
    cursor = db.conn.cursor()
    cursor.execute(query, (payment, participant_id))
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


def calculate_elements(c, n):
    db.connect()
    cursor = db.conn.cursor()
    for alcolici, quantita_alcolici in c.alcohols:
        value = quantita_alcolici * n
        query = f'UPDATE eventmanager SET quantity = %s WHERE name = %s'
        cursor.execute(query, (value, alcolici))
        db.conn.commit()
    db.disconnect()


def calculate_shopping():
    db.connect()
    query = 'SELECT * FROM eventmanager.cocktails'
    cursor = db.conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    while row is not None:

        id, name, qt = row
        found_cocktail = None
        for c in cocktails_list:
            if c.nome == name:
                found_cocktail = c
            if found_cocktail:
                calculate_elements(found_cocktail, qt)

        row = cursor.fetchone()

    db.disconnect()


def show_shopping():
    query = 'SELECT * FROM eventmanager.alcohol'
    db.connect()
    cursor = db.conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    db.disconnect()
    return results



