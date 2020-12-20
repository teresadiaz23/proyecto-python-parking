from aplicacion.app import db
from sqlalchemy import Boolean, Column, ForeignKey
from sqlalchemy import DateTime, Integer, String, Text, Float
from sqlalchemy.orm import relationship

class Vehiculo(db.Model):
    __tablename__ = 'vehiculo'
    id = Column(Integer, primary_key=True)
    tipo_vehiculo = Column(String(32), nullable=False)
    matricula = Column(String(7))
    tarifa = Column(Float)
    cliente = relationship("ClienteAbonado", backref="Vehiculo")
    __mapper_args__ = {'polymorphic_on': tipo_vehiculo}

    # def __init__(self, matricula):
    #     self.__matricula = matricula
    #
    # @property
    # def matricula(self):
    #     return self.__matricula
    #
    # @matricula.setter
    # def matricula(self, matricula):
    #     self.__matricula = matricula



class Turismo(Vehiculo):
    __mapper_args__ = {'polymorphic_identity': 'turismo'}

    # def __init__(self, matricula, tarifa=0.12):
    #     super().__init__(matricula)
    #     self.__tarifa = tarifa
    #
    # @property
    # def tarifa(self):
    #     return self.__tarifa
    #
    # @tarifa.setter
    # def tarifa(self, tarifa):
    #     self.__tarifa = tarifa


class Motocicleta(Vehiculo):
    __mapper_args__ = {'polymorphic_identity': 'motocicleta'}

    # def __init__(self, matricula, tarifa=0.08):
    #     super().__init__(matricula)
    #     self.__tarifa = tarifa
    #
    # @property
    # def tarifa(self):
    #     return self.__tarifa
    #
    # @tarifa.setter
    # def tarifa(self, tarifa):
    #     self.__tarifa = tarifa


class MovilidadReducida(Vehiculo):
    __mapper_args__ = {'polymorphic_identity': 'movilidad_reducida'}


    # def __init__(self, matricula, tarifa=0.10):
    #     super().__init__(matricula)
    #     self.__tarifa = tarifa
    #
    # @property
    # def tarifa(self):
    #     return self.__tarifa
    #
    # @tarifa.setter
    # def tarifa(self, tarifa):
    #     self.__tarifa = tarifa


