from aplicacion.repositories.abono_repositorio import abono_repositorio


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

    def find_all(self):
        return self.repositorio.find_all()

    def find_by_pin(self, pin):
        return self.repositorio.find_by_pin(pin)

    def find_by_cliente(self, cliente):
        return self.repositorio.find_by_cliente(cliente)

    def delete(self, abono):
        self.repositorio.delete(abono)


abono_servicio = AbonoServicio(abono_repositorio)

