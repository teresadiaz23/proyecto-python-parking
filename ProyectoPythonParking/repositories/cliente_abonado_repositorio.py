from models.cliente_abonado import ClienteAbonado
from models.vehiculo import Turismo, Motocicleta, MovilidadReducida
import pickle


class ClienteAbonadoRepositorio():
    def __init__(self, lista_clientes):
        self.__lista_clientes = lista_clientes

    @property
    def lista_clientes(self):
         return self.__lista_clientes

    @lista_clientes.setter
    def lista_clientes(self, lista_clientes):
         self.__lista_clientes = lista_clientes


    def save(self, cliente):
        self.lista_clientes.append(cliente)


    def find_all(self):
        return self.lista_clientes

    def find_by_dni(self, dni):
        for cliente in self.lista_clientes:
            if(cliente.dni == dni):
                return cliente

    def find_by_matricula(self, matricula):
        for cliente in self.lista_clientes:
            if(cliente.vehiculo.matricula == matricula):
                return cliente



lista = [
    ClienteAbonado("1234", "Luismi", "López", "123456", "luismi@email.com", Turismo("1234BBB"), "mensual", 3),
    ClienteAbonado("12345678B", "Pepe", "García", "567897", "pepe@email.com", Motocicleta("6543HHH"), "trimestral", 45),
    ClienteAbonado("12345678C", "María", "Pérez", "342565", "maria@email.com", MovilidadReducida("3846DDD"), "semestral", 52),
    ClienteAbonado("12345678D", "Miguel", "Campos", "287698", "miguel@email.com", Turismo("3876KKK"), "anual", 30)
]



cliente_abonado_repositorio = ClienteAbonadoRepositorio(lista)



