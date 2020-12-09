class AbonoRepositorio():
    def __init__(self, lista_abonos):
        self.__lista_abonos = lista_abonos

    @property
    def lista_abonos(self):
         return self.__lista_abonos

    @lista_abonos.setter
    def lista_abonos(self, lista_abonos):
         self.__lista_abonos = lista_abonos


    def save(self, abono):
        self.lista_abonos.append(abono)

    def findAll(self):
        return self.lista_abonos

    def findByPin(self, pin):
        for abono in self.lista_abonos:
            if(abono.pin == pin):
                return abono
