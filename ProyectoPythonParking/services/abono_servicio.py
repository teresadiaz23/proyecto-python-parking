from repositories.abono_repositorio import abono_repositorio


class AbonoServicio():
    def __init__(self, repo):
        self.__repo = repo

    @property
    def repositorio(self):
        return self.__repo

    @repositorio.setter
    def repositorio(self, repo):
        self.__repo = repo

    def save(self, abono):
        self.repositorio.save(abono)

    def edit(self, abono):
        self.repositorio.save(abono)

    def findAll(self):
        return self.repositorio.findAll()

    def findByPin(self, pin):
        return self.repositorio.findByPin(pin)

    def findByCliente(self, cliente):
        return self.repositorio.findByCliente(cliente)

    def delete(self, abono):
        self.repositorio.delete(abono)


abono_servicio = AbonoServicio(abono_repositorio)

