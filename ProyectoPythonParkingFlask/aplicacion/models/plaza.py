from aplicacion.app import db
from sqlalchemy import Boolean, Column, ForeignKey
from sqlalchemy import DateTime, Integer, String, Text, Float
from sqlalchemy.orm import relationship

class Plaza(db.Model):
    __tablename__ = 'plaza'
    id = Column(Integer, primary_key=True)
    tipo_vehiculo = Column(String(100))
    tarifa = Column(Float)
    ocupada = Column(Boolean, default=False)
    ClienteId = Column(Integer,ForeignKey('cliente_abonado.id'), default=-1)
    cliente = relationship("ClienteAbonado", backref="Plaza")
    ParkingId = Column(Integer,ForeignKey('parking.id'), nullable=False)
    parking = relationship("Parking", backref="Plaza")


    # def __init__(self, id, tipo_vehiculo, tarifa, ocupada=False, cliente=None):
    #     self.__id = id
    #     self.__tipo_vehiculo = tipo_vehiculo
    #     self.__tarifa = tarifa
    #     self.__ocupada = ocupada
    #     self.__cliente = cliente
    #
    # @property
    # def id(self):
    #     return self.__id
    #
    # @id.setter
    # def id(self, id):
    #     self.__id = id
    #
    # @property
    # def tipo_vehiculo(self):
    #     return self.__tipo_vehiculo
    #
    # @tipo_vehiculo.setter
    # def tipo_vehiculo(self, tipo_vehiculo):
    #     self.__tipo_vehiculo = tipo_vehiculo
    #
    # @property
    # def tarifa(self):
    #     return self.__tarifa
    #
    # @tarifa.setter
    # def tarifa(self, tarifa):
    #     self.__tarifa = tarifa
    #
    # @property
    # def ocupada(self):
    #     return self.__ocupada
    #
    # @ocupada.setter
    # def ocupada(self, ocupada):
    #     self.__ocupada = ocupada
    #
    # @property
    # def cliente(self):
    #     return self.__cliente
    #
    # @cliente.setter
    # def cliente(self, cliente):
    #     self.__cliente = cliente


    def __str__(self):
        return f"Plaza(id: {self.id}, tipo_vehículo: {self.tipo_vehiculo}, tarifa: {self.tarifa}," \
               f" ocupada: {self.ocupada}, cliente: {self.cliente})"


