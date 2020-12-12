from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta

from models.abono import Abono
from repositories.cliente_abonado_repositorio import cliente_abonado_repositorio



class AbonoRepositorio():
    def __init__(self, lista_abonos=[]):
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

    def findByCliente(self, cliente):
        for abono in self.lista_abonos:
            if(abono.cliente_abonado == cliente):
                return abono

    def delete(self, abono):
        for a in self.lista_abonos:
            if(a == abono):
                self.lista_abonos.remove(a)




abono1 = Abono(111, "mensual", datetime.now(), datetime.now() + relativedelta(months=1), cliente_abonado_repositorio.findAll()[0], 25)
abono2 = Abono(222, "trimestral", datetime.now(), datetime.now() + relativedelta(months=3), cliente_abonado_repositorio.findAll()[1], 70)
abono3 = Abono(333, "semestral", datetime.now(), datetime.now() + relativedelta(months=6), cliente_abonado_repositorio.findAll()[2], 130)
abono4 = Abono(444, "anual", datetime.now(), datetime.now() + relativedelta(years=1), cliente_abonado_repositorio.findAll()[3], 200)

lista_abonos = [abono1, abono2, abono3, abono4]
abono_repositorio = AbonoRepositorio(lista_abonos)

# for abono in abono_repositorio.findAll():
#     print(abono)



