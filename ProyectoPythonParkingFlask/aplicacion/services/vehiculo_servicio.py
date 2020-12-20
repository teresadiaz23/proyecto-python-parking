from aplicacion.repositories.vehiculo_repositorio import vehiculo_repositorio


class VehiculoServicio():
    def __init__(self, repo):
        self.__repo = repo

    @property
    def repositorio(self):
        return self.__repo

    @repositorio.setter
    def repositorio(self, repo):
        self.__repo = repo

    def save(self, vehiculo):
        self.repositorio.save(vehiculo)

    def edit(self, vehiculo):
        self.repositorio.save(vehiculo)


vehiculo_servicio = VehiculoServicio(vehiculo_repositorio)
