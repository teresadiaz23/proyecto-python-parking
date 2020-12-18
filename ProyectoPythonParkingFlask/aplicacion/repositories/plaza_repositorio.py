import pickle

from aplicacion.models.plaza import Plaza
from aplicacion.repositories.cliente_abonado_repositorio import cliente_abonado_repositorio
#from services.abonado_servicio import abonado_servicio


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
        filename = './aplicacion/datos/plazas'
        outfile = open(filename, 'wb')
        pickle.dump(self.lista_plazas, outfile)
        outfile.close()

    def find_all(self):
        return self.lista_plazas

    def find_by_id(self, id):
        for plaza in self.lista_plazas:
            if(plaza.id == id):
                return plaza

    def find_by_cliente(self, cliente):
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

plazas[2].cliente = cliente_abonado_repositorio.find_all()[0]
plazas[44].cliente = cliente_abonado_repositorio.find_all()[1]
plazas[51].cliente = cliente_abonado_repositorio.find_all()[2]
plazas[29].cliente = cliente_abonado_repositorio.find_all()[3]

filename = './aplicacion/datos/plazas'
outfile = open(filename, 'wb')

pickle.dump(plazas, outfile)
outfile.close()

infile = open(filename, 'rb')
lista_plazas = pickle.load(infile)
infile.close()

plaza_repositorio = PlazaRepositorio(lista_plazas)

# for plaza in plaza_repositorio.findAll():
#     print(plaza)
