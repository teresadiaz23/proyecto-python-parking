from aplicacion.services.abono_servicio import abono_servicio
from aplicacion.services.ticket_servicio import ticket_servicio


class Parking():
    def __init__(self, num_plazas, lista_plazas=[], dinero_tickets=[], dinero_abonos=[]):
        self.__lista_plazas = lista_plazas
        self.__num_plazas = num_plazas
        self.__dinero_tickets = dinero_tickets
        self.__dinero_abonos = dinero_abonos

    @property
    def lista_plazas(self):
        return self.__lista_plazas

    @lista_plazas.setter
    def lista_plazas(self, lista_plazas):
        self.__lista_plazas = lista_plazas

    @property
    def num_plazas(self):
        return self.__num_plazas

    @num_plazas.setter
    def num_plazas(self, num_plazas):
        self.__num_plazas = num_plazas

    @property
    def dinero_tickets(self):
        return self.__dinero_tickets

    @dinero_tickets.setter
    def dinero_tickets(self, dinero_tickets):
        self.__dinero_tickets = dinero_tickets

    @property
    def dinero_abonos(self):
        return self.__dinero_abonos

    @dinero_abonos.setter
    def dinero_abonos(self, dinero_abonos):
        self.__dinero_abonos = dinero_abonos


dinero_tickets = []
if(len(ticket_servicio.find_all()) > 0):
    for ticket in ticket_servicio.find_all():
        dinero_tickets.append(ticket.coste)


dinero_abonos = []
if(len(abono_servicio.find_all()) > 0):
    for abono in abono_servicio.find_all():
        dinero_abonos.append(abono.precio)


parking = Parking(60,  dinero_tickets=dinero_tickets, dinero_abonos=dinero_abonos)





