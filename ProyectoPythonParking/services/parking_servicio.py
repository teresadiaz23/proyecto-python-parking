from repositories.parking_repositorio import parking_repositorio

class ParkingServicio():
    def __init__(self, repo):
        self.__repo = repo

    @property
    def repositorio(self):
        return self.__repo

    @repositorio.setter
    def repositorio(self, repo):
        self.__repo = repo

    def save(self, parking):
        self.repositorio.save(parking)

    def findAll(self):
        return self.repositorio.findAll()

    def plazas_libres_turismo(self):
        libres = []
        for plaza in self.repositorio.parking.lista_plazas:
            if(plaza.tipo_vehiculo == "turismo"):
                if(plaza.ocupada == False and plaza.cliente == None):
                    libres.append(plaza)


        return libres

    def plazas_libres_moto(self):
        libres = []
        for plaza in self.repositorio.parking.lista_plazas:
            if(plaza.tipo_vehiculo == "motocicleta"):
                if(plaza.ocupada == False and plaza.cliente == None):
                    libres.append(plaza)


        return libres

    def plazas_libres_movreducida(self):
        libres = []
        for plaza in self.repositorio.parking.lista_plazas:
            if(plaza.tipo_vehiculo == "movilidad reducida"):
                if(plaza.ocupada == False and plaza.cliente == None):
                    libres.append(plaza)


        return libres


parking_servicio = ParkingServicio(parking_repositorio)
