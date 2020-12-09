class Plaza():
    def __init__(self, id, tipo_vehiculo, tarifa, ocupada = False, cliente = None):
        self.__id = id
        self.__tipo_vehiculo = tipo_vehiculo
        self.__tarifa = tarifa
        self.__ocupada = ocupada
        self.__cliente = cliente

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def tipo_vehiculo(self):
        return self.__tipo_vehiculo

    @tipo_vehiculo.setter
    def tipo_vehiculo(self, tipo_vehiculo):
        self.__tipo_vehiculo = tipo_vehiculo

    @property
    def tarifa(self):
        return self.__tarifa

    @tarifa.setter
    def tarifa(self, tarifa):
        self.__tarifa = tarifa

    @property
    def ocupada(self):
        return self.__ocupada

    @ocupada.setter
    def ocupada(self, ocupada):
        self.__ocupada = ocupada

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente


