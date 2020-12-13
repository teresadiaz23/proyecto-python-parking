from models.DatosErroneos import DatosErroneos
from models.plaza import Plaza
from models.ticket import Ticket
from services.plaza_servicio import plaza_servicio
from services.parking_servicio import parking_servicio
from services.ticket_servicio import ticket_servicio
from datetime import datetime
from random import randint
from math import floor


class ClienteServicio():

    def depositar_vehiculo(self, matricula, tipo):
        depositado = False


        if(tipo.lower() == "turismo"):
            if(len(parking_servicio.plazas_libres_turismo()) > 0):
                plaza_asignada = parking_servicio.plazas_libres_turismo()[0]
                parking_servicio.plazas_libres_turismo()[0].ocupada = True
                depositado = True

        elif(tipo.lower() == "motocicleta"):
            if(len(parking_servicio.plazas_libres_moto()) > 0):
                plaza_asignada = parking_servicio.plazas_libres_moto()[0]
                parking_servicio.plazas_libres_moto()[0].ocupada = True
                depositado = True

        elif(tipo.lower() == "movilidad reducida"):
            if(len(parking_servicio.plazas_libres_movreducida()) > 0):
                plaza_asignada = parking_servicio.plazas_libres_movreducida()[0]
                parking_servicio.plazas_libres_movreducida()[0].ocupada = True
                depositado = True

        if(depositado):
            pin = randint(111111,999999)

            ticket = Ticket(matricula, datetime.now(), plaza_asignada.id, pin)
            ticket_servicio.save(ticket)

        else:
            raise DatosErroneos

        return depositado

    def retirar_vehiculo(self, matricula, id, pin):
        ticket = ticket_servicio.findByPin(pin)
        ticket2 = ticket_servicio.findByMatricula(matricula)
        plaza = plaza_servicio.findById(id)
        total = -1

        if(ticket != None and ticket == ticket2 and plaza != None):
            hoy = datetime.now()
            tiempo = hoy - ticket.fecha_deposito
            tiempo = floor(tiempo.total_seconds()/60)

            total = tiempo * plaza.tarifa
            ticket.fecha_salida = hoy
            ticket.coste = total
            parking_servicio.findAll().dinero_tickets.append(total)

            plaza.ocupada = False

        if(total == -1):
            raise DatosErroneos

        return total


cliente_servicio = ClienteServicio()
# cliente_servicio.depositar_vehiculo("1234", "turismo")
# print(parking_servicio.findAll().lista_plazas[0])
# print(cliente_servicio.retirar_vehiculo("1234BBB", 6, 111111))
# print(parking_servicio.findAll().lista_plazas[0])
# cliente_servicio.depositar_vehiculo("1234", "motocicleta")
# cliente_servicio.depositar_vehiculo("1234", "movilidad reducida")
# for plaza in parking_servicio.findAll().lista_plazas:
#     print(plaza)
