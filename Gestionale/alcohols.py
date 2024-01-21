from dbOperations import *
from db_connection import *

db = Database()


class Alcohol:
    def __init__(self, id, name, quantity):
        self.id = id
        self.name = name
        self.quantity = quantity


def alcohols():
    in_house = []
    query_results = inventory_request('alcohol')
    for q in query_results:
        alcohol = Alcohol(*q)
        in_house.append(alcohol)
    return in_house




