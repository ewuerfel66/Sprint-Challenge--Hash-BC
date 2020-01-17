#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = HashTable(length)
    route = []

    # Enter each ticket into a hashtable
    for ticket in tickets:
        hash_table_insert(ht, ticket.source, ticket.destination)

    # Find first flight
    leaving = "NONE"
    going = hash_table_retrieve(ht, leaving)

    while going is not "NONE":
        route.append(going)
        
        # You're now leaving from where you arrived
        leaving = going
        going = hash_table_retrieve(ht, leaving)

    route.append("NONE")

    return route
