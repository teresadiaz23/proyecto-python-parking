class TicketRepositorio():
    def __init__(self, lista_tickets):
        self.__lista_tickets = lista_tickets

    @property
    def lista_tickets(self):
         return self.__lista_tickets

    @lista_tickets.setter
    def lista_tickets(self, lista_tickets):
         self.__lista_tickets = lista_tickets


    def save(self, ticket):
        self.lista_tickets.append(ticket)

    def findAll(self):
        return self.lista_tickets

    def findByPin(self, pin):
        for ticket in self.lista_tickets:
            if(ticket.pin == pin):
                return ticket
