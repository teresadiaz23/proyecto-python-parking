from aplicacion.app import db
from aplicacion.services.abono_servicio import abono_servicio
from aplicacion.services.ticket_servicio import ticket_servicio
from sqlalchemy import Boolean, Column, ForeignKey
from sqlalchemy import DateTime, Integer, String, Text, Float
from sqlalchemy.orm import relationship

class Parking(db.Model):
    __tablename__ = 'parking'
    id = Column(Integer, primary_key=True)
    num_plazas = Column(Integer)
    dinero_tickets = Column(Float)
    dinero_abonos = Column(Float)
    plazas = relationship("Plaza", backref="Parking")

#     def __init__(self, num_plazas, lista_plazas=[], dinero_tickets=[], dinero_abonos=[]):
#         self.__lista_plazas = lista_plazas
#         self.__num_plazas = num_plazas
#         self.__dinero_tickets = dinero_tickets
#         self.__dinero_abonos = dinero_abonos
#
#     @property
#     def lista_plazas(self):
#         return self.__lista_plazas
#
#     @lista_plazas.setter
#     def lista_plazas(self, lista_plazas):
#         self.__lista_plazas = lista_plazas
#
#     @property
#     def num_plazas(self):
#         return self.__num_plazas
#
#     @num_plazas.setter
#     def num_plazas(self, num_plazas):
#         self.__num_plazas = num_plazas
#
#     @property
#     def dinero_tickets(self):
#         return self.__dinero_tickets
#
#     @dinero_tickets.setter
#     def dinero_tickets(self, dinero_tickets):
#         self.__dinero_tickets = dinero_tickets
#
#     @property
#     def dinero_abonos(self):
#         return self.__dinero_abonos
#
#     @dinero_abonos.setter
#     def dinero_abonos(self, dinero_abonos):
#         self.__dinero_abonos = dinero_abonos






