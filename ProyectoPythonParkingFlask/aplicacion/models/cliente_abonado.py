from aplicacion.app import db
from sqlalchemy import Boolean, Column , ForeignKey
from sqlalchemy import DateTime, Integer, String, Text, Float
from sqlalchemy.orm import relationship


class ClienteAbonado(db.Model):
    __tablename__ = 'cliente_abonado'
    id = Column(Integer, primary_key=True)
    dni = Column(String(9))
    nombre = Column(String(100))
    apellidos = Column(String(10))
    num_tarjeta = Column(String(10))
    email = Column(Integer)
    VehiculoId = Column(Integer, ForeignKey('vehiculo.id'), nullable=False)
    vehiculo = relationship("Vehiculo", backref="ClienteAbonado")
    abono = relationship("Abono", backref="ClienteAbonado")
    plaza = relationship("Plaza", backref="ClienteAbonado")

    # def __init__(self, dni, nombre, apellidos, num_tarjeta, email, vehiculo=None, abono=None, id_plaza=0):
    #     self.__dni = dni
    #     self.__nombre = nombre
    #     self.__apellidos = apellidos
    #     self.__num_tarjeta = num_tarjeta
    #     self.__email = email
    #     self.__vehiculo = vehiculo
    #     self.__abono = abono
    #     self.__id_plaza = id_plaza
    #
    # @property
    # def dni(self):
    #     return self.__dni
    #
    # @dni.setter
    # def dni(self, dni):
    #     self.__dni = dni
    #
    # @property
    # def nombre(self):
    #     return self.__nombre
    #
    # @nombre.setter
    # def nombre(self, nombre):
    #     self.__nombre = nombre
    #
    # @property
    # def apellidos(self):
    #     return self.__apellidos
    #
    # @apellidos.setter
    # def apellidos(self, apellidos):
    #     self.__apellidos = apellidos
    #
    # @property
    # def num_tarjeta(self):
    #     return self.__num_tarjeta
    #
    # @num_tarjeta.setter
    # def num_tarjeta(self, num_tarjeta):
    #     self.__num_tarjeta = num_tarjeta
    #
    # @property
    # def email(self):
    #     return self.__email
    #
    # @email.setter
    # def email(self, email):
    #     self.__email = email
    #
    # @property
    # def vehiculo(self):
    #     return self.__vehiculo
    #
    # @vehiculo.setter
    # def vehiculo(self, vehiculo):
    #     self.__vehiculo = vehiculo
    #
    # @property
    # def abono(self):
    #     return self.__abono
    #
    # @abono.setter
    # def abono(self, abono):
    #     self.__abono = abono
    #
    # @property
    # def id_plaza(self):
    #     return self.__id_plaza
    #
    # @id_plaza.setter
    # def id_plaza(self, id_plaza):
    #     self.__id_plaza = id_plaza

    def __str__(self):
        return f"ClienteAbonado(nombre: {self.nombre}, apellidos: {self.apellidos}, dni: {self.dni}, email: {self.email})"





