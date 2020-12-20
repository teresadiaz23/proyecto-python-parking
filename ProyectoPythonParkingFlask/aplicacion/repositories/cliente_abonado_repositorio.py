from aplicacion.app import db
from aplicacion.models.cliente_abonado import ClienteAbonado
from aplicacion.models.vehiculo import Turismo, Motocicleta, MovilidadReducida, Vehiculo



class ClienteAbonadoRepositorio():


    def save(self, cliente):
        db.session.add(cliente)
        db.session.commit()


    def find_all(self):
        clientes = ClienteAbonado.query.all()
        return clientes


    def find_by_dni(self, dni):
        cliente = ClienteAbonado.query.filter_by(dni=dni).first()
        return cliente


    def find_by_matricula(self, matricula):
        vehiculo = Vehiculo.query.filter_by(matricula=matricula).first()
        cliente = ClienteAbonado.query.filter_by(vehiculo=vehiculo).first()
        return cliente


    def delete(self, cliente):
        db.session.delete(cliente)



cliente_abonado_repositorio = ClienteAbonadoRepositorio()


