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

    def findAll(self):
        return self.repositorio.findAll()

    def findById(self, id):
        return self.repositorio.findById(id)

    def findByCliente(self, cliente):
        return self.repositorio.findByCliente(cliente)


plaza_servicio = PlazaServicio(plaza_repositorio)
