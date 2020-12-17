class Ticket():
    def __init__(self, matricula, fecha_deposito, id_plaza, pin, fecha_salida=None, coste=0):
        self.__matricula = matricula
        self.__fecha_deposito = fecha_deposito
        self.__id_plaza = id_plaza
        self.__pin = pin
        self.__fecha_salida = fecha_salida
        self.__coste = coste

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @property
    def fecha_deposito(self):
        return self.__fecha_deposito

    @fecha_deposito.setter
    def fecha_deposito(self, fecha_deposito):
        self.__fecha_deposito = fecha_deposito

    @property
    def id_plaza(self):
        return self.__id_plaza

    @id_plaza.setter
    def id_plaza(self, id_plaza):
        self.__id_plaza = id_plaza

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, pin):
        self.__pin = pin

    @property
    def fecha_salida(self):
        return self.__fecha_salida

    @fecha_salida.setter
    def fecha_salida(self, fecha_salida):
        self.__fecha_salida = fecha_salida

    @property
    def coste(self):
        return self.__coste

    @coste.setter
    def coste(self, coste):
        self.__coste = coste


    def __str__(self):
        return f"Ticket(matrícula: {self.matricula}, fecha_deposito: {self.fecha_salida}, id_plaza: {self.id_plaza}, " \
               f"pin: {self.pin}, fecha_salida: {self.fecha_salida}, coste: {self.coste})"




