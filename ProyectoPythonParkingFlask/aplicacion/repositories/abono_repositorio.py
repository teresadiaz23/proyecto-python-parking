import pickle
from datetime import datetime
from dateutil.relativedelta import relativedelta

from aplicacion.app import db
from aplicacion.models.abono import Abono




class AbonoRepositorio():

    def save(self, abono):
        db.session.add(abono)
        db.session.commit()


    def find_all(self):
        abonos = Abono.query.all()
        return abonos


    def find_by_pin(self, pin):
        abono = Abono.query.filter_by(pin=pin).first()
        return abono


    def find_by_cliente(self, cliente):
        abono = Abono.query.filter_by(cliente_abonado=cliente).first()
        return abono


    def delete(self, abono):
        db.session.delete(abono)


abono_repositorio = AbonoRepositorio()




