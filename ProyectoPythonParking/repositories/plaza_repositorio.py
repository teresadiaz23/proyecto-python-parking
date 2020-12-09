class PlazaRepositorio():
    def __init__(self, lista_plazas):
        self.__lista_plazas = lista_plazas

    @property
    def lista_plazas(self):
         return self.__lista_plazas

    @lista_plazas.setter
    def lista_plazas(self, lista_plazas):
         self.__lista_plazas= lista_plazas


    def save(self, plaza):
        self.lista_plazas.append(plaza)

    def findAll(self):
        return self.lista_plazas

    def findById(self, id):
        for plaza in self.lista_plazas:
            if(plaza.id == id):
                return plaza
