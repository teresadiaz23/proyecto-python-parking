import pickle

from aplicacion.app import db
from aplicacion.models.plaza import Plaza
from aplicacion.repositories.cliente_abonado_repositorio import cliente_abonado_repositorio
#from services.abonado_servicio import abonado_servicio


class PlazaRepositorio():
    # def __init__(self, lista_plazas):
    #     self.__lista_plazas = lista_plazas
    #
    # @property
    # def lista_plazas(self):
    #      return self.__lista_plazas
    #
    # @lista_plazas.setter
    # def lista_plazas(self, lista_plazas):
    #      self.__lista_plazas= lista_plazas


    def save(self, plaza):
        db.session.add(plaza)
        db.session.commit()
        #self.lista_plazas.append(plaza)
        # filename = './aplicacion/datos/plazas'
        # outfile = open(filename, 'wb')
        # pickle.dump(self.lista_plazas, outfile)
        # outfile.close()

    def find_all(self):
        plazas = Plaza.query.all()
        return plazas


    def find_by_id(self, id):
        plaza = Plaza.query.get(id)
        return plaza


    def find_by_cliente(self, cliente):
        plaza = Plaza.query.filter_by(cliente=cliente).first()
        return plaza


plaza_repositorio = PlazaRepositorio()

