from aplicacion.repositories.parking_repositorio import parking_repositorio

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

    def find_all(self):
        return self.repositorio.find_all()

    def find_all_plazas(self):
        return self.repositorio.find_all_plazas()

    def find_plaza_by_cliente(self, cliente):
        return self.repositorio.find_plaza_by_cliente(cliente)

    def find_plaza_by_id(self, id):
        return self.repositorio.find_plaza_by_id(id)

    def plazas_libres_turismo(self):
        libres = []
        for plaza in self.repositorio.find_all_plazas():
            if(plaza.tipo_vehiculo == "turismo"):
                if(plaza.ocupada == False and plaza.cliente == None):
                    libres.append(plaza)


        return libres

    def plazas_libres_moto(self):
        libres = []
        for plaza in self.repositorio.find_all_plazas():
            if(plaza.tipo_vehiculo == "motocicleta"):
                if(plaza.ocupada == False and plaza.cliente == None):
                    libres.append(plaza)


        return libres

    def plazas_libres_movreducida(self):
        libres = []
        for plaza in self.repositorio.find_all_plazas():
            if(plaza.tipo_vehiculo == "movilidad reducida"):
                if(plaza.ocupada == False and plaza.cliente == None):
                    libres.append(plaza)


        return libres


parking_servicio = ParkingServicio(parking_repositorio)
