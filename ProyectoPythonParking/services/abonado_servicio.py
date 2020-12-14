from models.AbonoNoEncontrado import AbonoNoEncontrado
from models.ClienteNoEncontrado import ClienteNoEncontrado
from repositories.cliente_abonado_repositorio import cliente_abonado_repositorio
from services.abono_servicio import abono_servicio
from services.parking_servicio import parking_servicio
from services.plaza_servicio import plaza_servicio


class AbonadoServicio():
    def __init__(self, repo):
        self.__repo = repo

    @property
    def repositorio(self):
        return self.__repo

    @repositorio.setter
    def repositorio(self, repo):
        self.__repo = repo

    def save(self, cliente):
        self.repositorio.save(cliente)

    def edit(self, cliente):
        self.repositorio.save(cliente)

    def findAll(self):
        return self.repositorio.findAll()

    def findByDni(self, dni):
        return self.repositorio.findByDni(dni)

    def findByMatricula(self, matricula):
        return self.repositorio.findByMatricula(matricula)


    def depositar_abonados(self, matricula, dni):
        depositado = False
        cliente = self.repositorio.findByDni(dni)
        cliente2 = self.repositorio.findByMatricula(matricula)

        if(cliente == cliente2 and cliente != None):
            depositado = True
            plaza = parking_servicio.findPlazaByCliente(cliente)
            plaza.ocupada = True
        if(not depositado):
            raise ClienteNoEncontrado

        return depositado

    def retirar_abonados(self, matricula, id, pin):
        retirado = False
        cliente = self.repositorio.findByMatricula(matricula)
        plaza = parking_servicio.findPlazaById(id)
        abono = abono_servicio.findByPin(pin)

        if(cliente != None and abono != None):
            if(abono.cliente_abonado == cliente and plaza.ocupada):
                plaza.ocupada = False
                retirado = True

        else:
            raise ClienteNoEncontrado

        return retirado


    def obtener_abono(self, dni, pin):
        cliente = self.repositorio.findByDni(dni)
        abono = abono_servicio.findByPin(pin)
        abono2 = abono_servicio.findByCliente(cliente)

        if(abono == abono2):
            return abono

        else:
            raise AbonoNoEncontrado

    def obtener_datos_personales(self, dni, pin):
        cliente = self.repositorio.findByDni(dni)
        abono = abono_servicio.findByPin(pin)
        abono2 = abono_servicio.findByCliente(cliente)

        if(abono == abono2):
            return cliente
        else:
            raise ClienteNoEncontrado


abonado_servicio = AbonadoServicio(cliente_abonado_repositorio)

# print(abonado_servicio.depositar_abonados("1234BBB", "1234"))
# print(abonado_servicio.retirar_abonados("1234BBB", 3, 111))
# print(abonado_servicio.obtener_abono("1234", 111))
# print(abonado_servicio.obtener_datos_personales("1234", 111))
