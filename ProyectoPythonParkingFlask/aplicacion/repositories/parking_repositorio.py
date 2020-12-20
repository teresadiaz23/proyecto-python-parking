
from aplicacion.app import db
from aplicacion.models.parking import Parking
from aplicacion.models.plaza import Plaza

class ParkingRepositorio():

    def save(self, abono):
        db.session.add(abono)
        db.session.commit()

    def find_all(self):
        parking = Parking.query.first()
        return parking
        #return self.parking

    def find_all_plazas(self):
        plazas = Plaza.query.all()
        return plazas

    def find_plaza_by_cliente(self, cliente):
        plaza = Plaza.query.filter_by(cliente=cliente).first()
        return plaza

    def find_plaza_by_id(self, id):
        plaza = Plaza.query.get(id)
        return plaza


parking_repositorio = ParkingRepositorio()


