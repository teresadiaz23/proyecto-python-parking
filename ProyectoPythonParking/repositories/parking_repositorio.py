class ParkingRepositorio():
    def __init__(self, parking):
        self.__parking = parking

    @property
    def parking(self):
         return self.__parking

    @parking.setter
    def parking(self, parking):
         self.__parking = parking
