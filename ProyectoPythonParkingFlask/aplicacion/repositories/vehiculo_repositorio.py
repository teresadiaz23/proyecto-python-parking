from aplicacion.app import db

class VehiculoRepositorio():

    def save(self, vehiculo):
        db.session.add(vehiculo)
        db.session.commit()


vehiculo_repositorio = VehiculoRepositorio()
