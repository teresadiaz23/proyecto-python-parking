from repositories.cliente_abonado_repositorio import cliente_abonado_repositorio
from repositories.plaza_repositorio import plaza_repositorio


class PlazaServicio():
    def __init__(self, repo):
        self.__repo = repo

    @property
    def repositorio(self):
        return self.__repo

    @repositorio.setter
    def repositorio(self, repo):
        self.__repo = repo

    def save(self, plaza):
        self.repositorio.save(plaza)

    def edit(self, plaza):
        self.repositorio.save(plaza)

    def find_all(self):
        return self.repositorio.find_all()

    def find_by_id(self, id):
        return self.repositorio.find_by_id(id)

    def find_by_cliente(self, cliente):
        return self.repositorio.find_by_cliente(cliente)


plaza_servicio = PlazaServicio(plaza_repositorio)

