from models.parking import parking
from repositories.plaza_repositorio import plaza_repositorio


class ParkingRepositorio():
    def __init__(self, parking):
        self.__parking = parking

    @property
    def parking(self):
         return self.__parking

    @parking.setter
    def parking(self, parking):
         self.__parking = parking

    def findAll(self):
        return self.parking


parking_repositorio = ParkingRepositorio(parking)
parking_repositorio.parking.lista_plazas = plaza_repositorio.findAll()

