from models.cliente_abonado import ClienteAbonado
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

    def findAll(self):
        return self.lista_clientes

    def findByDni(self, dni):
        for cliente in self.lista_clientes:
            if(cliente.dni == dni):
                return cliente

    def findByMatricula(self, matricula):
        for cliente in self.lista_clientes:
            if(cliente.matricula == matricula):
                return cliente



lista = [ClienteAbonado("1234", "Teresa", "Diaz", "123456", "teresa@email.com", None),
         ClienteAbonado("4321", "Pepe", "García", "123456", "pepe@email.com", None)]

cliente_abonado_repositorio = ClienteAbonadoRepositorio(lista)


for c in cliente_abonado_repositorio.findAll():
    print(c)
print(cliente_abonado_repositorio.findByDni("1234"))
