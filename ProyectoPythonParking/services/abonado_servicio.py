from repositories.cliente_abonado_repositorio import cliente_abonado_repositorio

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

    def findAll(self):
        return self.repositorio.findAll()

    def findByDni(self, dni):
        return self.repositorio.findByDni(dni)


abonado_servicio = AbonadoServicio(cliente_abonado_repositorio)
