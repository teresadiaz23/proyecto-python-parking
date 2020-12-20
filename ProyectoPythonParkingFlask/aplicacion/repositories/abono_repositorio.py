import pickle
from datetime import datetime
from dateutil.relativedelta import relativedelta

from aplicacion.app import db
from aplicacion.models.abono import Abono
from aplicacion.repositories.cliente_abonado_repositorio import cliente_abonado_repositorio



class AbonoRepositorio():
    # def __init__(self, lista_abonos=[]):
    #     self.__lista_abonos = lista_abonos
    #
    # @property
    # def lista_abonos(self):
    #      return self.__lista_abonos
    #
    # @lista_abonos.setter
    # def lista_abonos(self, lista_abonos):
    #      self.__lista_abonos = lista_abonos


    def save(self, abono):
        db.session.add(abono)
        db.session.commit()
        #self.lista_abonos.append(abono)
        # filename = './aplicacion/datos/abonos'
        # outfile = open(filename, 'wb')
        # pickle.dump(self.lista_abonos, outfile)
        # outfile.close()

    def find_all(self):
        abonos = Abono.query.all()
        return abonos
        #return self.lista_abonos

    def find_by_pin(self, pin):
        abono = Abono.query.filter_by(pin=pin).first()
        return abono
        # for abono in self.lista_abonos:
        #     if(abono.pin == pin):
        #         return abono

    def find_by_cliente(self, cliente):
        abono = Abono.query.filter_by(cliente_abonado=cliente).first()
        return abono
        # for abono in self.lista_abonos:
        #     if(abono.cliente_abonado == cliente):
        #         return abono

    def delete(self, abono):
        db.session.delete(abono)
        # for a in self.lista_abonos:
        #     if(a == abono):
        #         self.lista_abonos.remove(a)




# abono1 = Abono(111, "mensual", datetime.now(), datetime.now() + relativedelta(months=1), cliente_abonado_repositorio.find_all()[0], 25)
# abono2 = Abono(222, "trimestral", datetime.now(), datetime.now() + relativedelta(months=3), cliente_abonado_repositorio.find_all()[1], 70)
# abono3 = Abono(333, "semestral", datetime.now(), datetime.now() + relativedelta(months=6), cliente_abonado_repositorio.find_all()[2], 130)
# abono4 = Abono(444, "anual", datetime.now(), datetime.now() + relativedelta(years=1), cliente_abonado_repositorio.find_all()[3], 200)

# lista_abonos = [abono1, abono2, abono3, abono4]

# filename = './aplicacion/datos/abonos'
# outfile = open(filename, 'wb')
#
# pickle.dump(lista_abonos, outfile)
# outfile.close()
#
# infile = open(filename, 'rb')
# lista = pickle.load(infile)
# infile.close()

abono_repositorio = AbonoRepositorio()

# for abono in abono_repositorio.findAll():
#     print(abono)



