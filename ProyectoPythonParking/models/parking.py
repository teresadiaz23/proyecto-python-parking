from models.plaza import Plaza


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

parking = Parking(60)
# plazas = []
# for p in range(parking.num_plazas):
#     if(p < 42):
#         plazas.append(Plaza(p+1, "turismo", 0.12))
#     elif(p >= 42 and p < 51):
#         plazas.append((Plaza(p+1, "motocicleta", 0.08)))
#     else:
#         plazas.append(Plaza(p+1, "movilidad reducida", 0.10))

#parking.lista_plazas = plazas


