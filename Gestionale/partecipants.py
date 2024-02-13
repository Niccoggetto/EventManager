from dbOperations import *


class Participant:
    def __init__(self, id, name, surname, phone, drinks, payment, paid, presence):
        self.id = id
        self.name = name
        self.surname = surname
        self.phone = phone
        self.drinks = drinks
        self.payment = payment
        self.paid = paid
        self.presence = presence


def persons():
    subs = []
    query_results = readparticipants()
    for q in query_results:
        participant = Participant(*q)
        subs.append(participant)
    return subs
