from aplicacion.app import db
from sqlalchemy import Boolean, Column, ForeignKey
from sqlalchemy import DateTime, Integer, String, Text, Float
from sqlalchemy.orm import relationship


class Abono(db.Model):

    __tablename__ = 'abono'
    id = Column(Integer, primary_key=True)
    pin = Column(Integer)
    tipo = Column(String(100))
    fecha_activacion = Column(DateTime(20))
    fecha_cancelacion = Column(DateTime(20))
    pin = Column(Integer)
    precio = Column(Float)
    ClienteId = Column(Integer,ForeignKey('cliente_abonado.id'), nullable=False)
    cliente_abonado = relationship("ClienteAbonado", backref="Abono")

    # def __init__(self, pin, tipo, fecha_activacion, fecha_cancelacion, precio, ClienteId):
    #     self.__pin = pin
    #     self.__tipo = tipo
    #     self.__fecha_activacion = fecha_activacion
    #     self.__fecha_cancelacion = fecha_cancelacion
    #     self.__cliente_abonado = ClienteId
    #     self.__precio = precio

    # @property
    # def pin(self):
    #     return self.__pin
    #
    # @pin.setter
    # def pin(self, pin):
    #     self.__pin = pin
    #
    # @property
    # def tipo(self):
    #     return self.__tipo
    #
    # @tipo.setter
    # def tipo(self, tipo):
    #     self.__tipo = tipo
    #
    # @property
    # def fecha_activacion(self):
    #     return self.__fecha_activacion
    #
    # @fecha_activacion.setter
    # def fecha_activacion(self, fecha_activacion):
    #     self.__fecha_activacion = fecha_activacion
    #
    # @property
    # def fecha_cancelacion(self):
    #     return self.__fecha_cancelacion
    #
    # @fecha_cancelacion.setter
    # def fecha_cancelacion(self, fecha_cancelacion):
    #     self.__fecha_cancelacion = fecha_cancelacion
    #
    # @property
    # def cliente_abonado(self):
    #     return self.__cliente_abonado
    #
    # @cliente_abonado.setter
    # def cliente_abonado(self, cliente_abonado):
    #     self.__cliente_abonado = cliente_abonado
    #
    # @property
    # def precio(self):
    #     return self.__precio
    #
    # @precio.setter
    # def precio(self, precio):
    #     self.__precio = precio
    #
    # def __str__(self):
    #     return f"Abono(pin: {self.pin}, tipo: {self.tipo}, fecha_activacion: {self.fecha_activacion}," \
    #            f" fecha_cancelacion: {self.fecha_cancelacion}," \
    #            f" cliente_abonado: {self.cliente_abonado}, precio: {self.precio})"
