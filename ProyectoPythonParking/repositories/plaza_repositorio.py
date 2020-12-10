from models.plaza import Plaza


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

    def findByCliente(self, cliente):
        for plaza in self.lista_plazas:
            if(plaza.cliente == cliente):
                return plaza

plazas = []
for p in range(60):
    if(p < 42):
        plazas.append(Plaza(p+1, "turismo", 0.12))
    elif(p >= 42 and p < 51):
        plazas.append((Plaza(p+1, "motocicleta", 0.08)))
    else:
        plazas.append(Plaza(p+1, "movilidad reducida", 0.10))


plaza_repositorio = PlazaRepositorio(plazas)
