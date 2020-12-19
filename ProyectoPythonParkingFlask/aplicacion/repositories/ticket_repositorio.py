import pickle
from datetime import datetime

from aplicacion.models.ticket import Ticket


class TicketRepositorio():
    def __init__(self, lista_tickets=[]):
        self.__lista_tickets = lista_tickets

    @property
    def lista_tickets(self):
         return self.__lista_tickets

    @lista_tickets.setter
    def lista_tickets(self, lista_tickets):
         self.__lista_tickets = lista_tickets


    def save(self, ticket):
        self.lista_tickets.append(ticket)
        # filename = './aplicacion/datos/tickets'
        # outfile = open(filename, 'wb')
        # pickle.dump(self.lista_tickets, outfile)
        # outfile.close()

    def find_all(self):
        return self.lista_tickets

    def find_by_pin(self, pin):
        for ticket in self.lista_tickets:
            if(ticket.pin == pin):
                return ticket

    def find_by_matricula(self, matricula):
        for ticket in self.lista_tickets:
            if(ticket.matricula == matricula):
                return ticket


lista_tickets = [
    Ticket("1234BBB", datetime(2020, 12, 10, 15, 30), 6, 111111, datetime(2020, 12, 10, 17, 30), 5),
    Ticket("1234JJJ", datetime(2020, 12, 12, 15, 30), 6, 111111, datetime(2020, 12, 12, 17, 30), 5.50),
    Ticket("1234FFF", datetime(2020, 12, 14, 15, 30), 6, 111111, datetime(2020, 12, 14, 17, 30), 6)
]

# filename = './aplicacion/datos/tickets'
# outfile = open(filename, 'wb')
#
# pickle.dump(lista_tickets, outfile)
# outfile.close()
#
# infile = open(filename, 'rb')
# tickets = pickle.load(infile)
# infile.close()

ticket_repositorio = TicketRepositorio(lista_tickets)
