#from aplicacion.models.parking import parking
from aplicacion.models.parking import Parking
from aplicacion.models.plaza import Plaza
from aplicacion.repositories.plaza_repositorio import plaza_repositorio


class ParkingRepositorio():
    # def __init__(self, parking=None):
    #     self.__parking = parking
    #
    # @property
    # def parking(self):
    #      return self.__parking
    #
    # @parking.setter
    # def parking(self, parking):
    #      self.__parking = parking

    def find_all(self):
        parking = Parking.query.first()
        return parking
        #return self.parking

    def find_all_plazas(self):
        plazas = Plaza.query.all()
        return plazas

    def find_plaza_by_cliente(self, cliente):
        plaza = Plaza.query.filter_by(cliente=cliente).first()
        return plaza
        # for plaza in self.parking.lista_plazas:
        #     if(plaza.cliente == cliente):
        #         return plaza

    def find_plaza_by_id(self, id):
        plaza = Plaza.query.get(id)
        return plaza
        # for plaza in self.parking.lista_plazas:
        #     if(plaza.id == id):
        #         return plaza


parking_repositorio = ParkingRepositorio()
#parking_repositorio.parking.lista_plazas = plaza_repositorio.find_all()

