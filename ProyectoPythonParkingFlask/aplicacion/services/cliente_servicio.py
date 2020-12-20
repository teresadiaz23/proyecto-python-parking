from aplicacion.models import DatosErroneos
from aplicacion.models.ticket import Ticket
from aplicacion.services.plaza_servicio import plaza_servicio
from aplicacion.services.parking_servicio import parking_servicio
from aplicacion.services.ticket_servicio import ticket_servicio
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
            pin = randint(111111, 999999)

            ticket = Ticket(matricula=matricula, fecha_deposito=datetime.now(), PlazaId=plaza_asignada.id, pin=pin)
            ticket_servicio.save(ticket)


        else:
            raise DatosErroneos

        return depositado

    def retirar_vehiculo(self, matricula, id, pin):
        ticket = ticket_servicio.find_by_pin(pin)
        ticket2 = ticket_servicio.find_by_matricula(matricula)
        plaza = plaza_servicio.find_by_id(id)
        total = -1

        if(ticket != None and ticket2 != None and plaza != None):
            hoy = datetime.now()
            tiempo = hoy - ticket.fecha_deposito
            tiempo = floor(tiempo.total_seconds()/60)

            total = tiempo * plaza.tarifa
            ticket.fecha_salida = hoy
            ticket.coste = total
            ticket_servicio.edit(ticket)
            parking_servicio.find_all().dinero_tickets+=total

            plaza.ocupada = False
            plaza_servicio.edit(plaza)

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
