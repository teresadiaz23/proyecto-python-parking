from aplicacion.models.parking import parking
from aplicacion.repositories.plaza_repositorio import plaza_repositorio


class ParkingRepositorio():
    def __init__(self, parking):
        self.__parking = parking

    @property
    def parking(self):
         return self.__parking

    @parking.setter
    def parking(self, parking):
         self.__parking = parking

    def find_all(self):
        return self.parking

    def find_plaza_by_cliente(self, cliente):
        for plaza in self.parking.lista_plazas:
            if(plaza.cliente == cliente):
                return plaza

    def find_plaza_by_id(self, id):
        for plaza in self.parking.lista_plazas:
            if(plaza.id == id):
                return plaza


parking_repositorio = ParkingRepositorio(parking)
parking_repositorio.parking.lista_plazas = plaza_repositorio.find_all()

