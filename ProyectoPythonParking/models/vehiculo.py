class Vehiculo():
    def __init__(self, matricula):
        self.__matricula = matricula

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula



class Turismo(Vehiculo):
    def __init__(self, matricula, tarifa):
        super().__init__(matricula)
        self.__tarifa = tarifa

    @property
    def tarifa(self):
        return self.__tarifa

    @tarifa.setter
    def tarifa(self, tarifa):
        self.__tarifa = tarifa


class Motocicleta(Vehiculo):
    def __init__(self, matricula, tarifa):
        super().__init__(matricula)
        self.__tarifa = tarifa

    @property
    def tarifa(self):
        return self.__tarifa

    @tarifa.setter
    def tarifa(self, tarifa):
        self.__tarifa = tarifa


class MovilidadReducida(Vehiculo):
    def __init__(self, matricula, tarifa):
        super().__init__(matricula)
        self.__tarifa = tarifa

    @property
    def tarifa(self):
        return self.__tarifa

    @tarifa.setter
    def tarifa(self, tarifa):
        self.__tarifa = tarifa


