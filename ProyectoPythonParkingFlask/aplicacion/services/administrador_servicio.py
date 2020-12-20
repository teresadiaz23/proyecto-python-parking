from random import randint
from datetime import datetime
from dateutil.relativedelta import relativedelta

from aplicacion.models import AbonoNoEncontrado
from aplicacion.models import DatosErroneos
from aplicacion.models.abono import Abono
from aplicacion.models.cliente_abonado import ClienteAbonado
from aplicacion.models.vehiculo import Turismo, Motocicleta, MovilidadReducida
from aplicacion.services.abonado_servicio import abonado_servicio
from aplicacion.services.abono_servicio import abono_servicio
from aplicacion.services.parking_servicio import parking_servicio
from aplicacion.services.plaza_servicio import plaza_servicio
from aplicacion.services.ticket_servicio import ticket_servicio
from aplicacion.services.vehiculo_servicio import vehiculo_servicio


class AdminServicio():

    def comprobar_password(self, password):
        if(password == "1234"):
            return True

    def facturacion(self, fecha1, fecha2):
        total = 0
        coste = []

        for ticket in ticket_servicio.find_all():
            if(ticket.fecha_salida != None):
                if(ticket.fecha_salida >= fecha1 and ticket.fecha_salida <= fecha2):
                    coste.append(ticket.coste)

        if(len(coste) > 0):
            for c in coste:
                total += c

        return round(total, 2)


    def consulta_cobro_abonados(self):
        total = 0
        if(parking_servicio.find_all().dinero_abonos > 0):

                total += parking_servicio.find_all().dinero_abonos

        return round(total, 2)

    def alta_abono(self, dni, nombre, apellidos, num_tarjeta, email, matricula, tipo_vehiculo, tipo_abono):
        confirmado = True

        if(tipo_vehiculo.lower() == "turismo"):
            vehiculo = Turismo(matricula=matricula, tarifa=0.12)
            plaza = parking_servicio.plazas_libres_turismo()[0]

        elif(tipo_vehiculo.lower() == "motocicleta"):
            vehiculo = Motocicleta(matricula=matricula, tarifa=0.08)
            plaza = parking_servicio.plazas_libres_moto()[0]

        elif(tipo_vehiculo.lower() == "movilidad reducida"):
            vehiculo = MovilidadReducida(matricula=matricula, tarifa=0.10)
            plaza = parking_servicio.plazas_libres_movreducida()[0]

        else:
            confirmado = False

        if(plaza != None):
            id = plaza.id


        vehiculo_servicio.save(vehiculo)
        cliente = ClienteAbonado(dni=dni, nombre=nombre, apellidos=apellidos, num_tarjeta=num_tarjeta,
                                 email=email, VehiculoId=vehiculo.id)



        pin = randint(111111, 999999)
        fecha = datetime.now()
        if(tipo_abono.lower() == "mensual"):
            abono = Abono(pin=pin, tipo=tipo_abono, fecha_activacion=datetime.now(),
                          fecha_cancelacion=fecha + relativedelta(months=1), precio=25)

        elif(tipo_abono.lower() == "trimestral"):
            abono = Abono(pin=pin, tipo=tipo_abono, fecha_activacion=datetime.now(),
                          fecha_cancelacion=fecha + relativedelta(months=3), precio=70)

        elif(tipo_abono.lower() == "semestral"):
            abono = Abono(pin=pin, tipo=tipo_abono, fecha_activacion=datetime.now(),
                          fecha_cancelacion=fecha + relativedelta(months=6), precio=130)

        elif(tipo_abono.lower() == "anual"):
            abono = Abono(pin=pin, tipo=tipo_abono, fecha_activacion=datetime.now(),
                          fecha_cancelacion=fecha + relativedelta(years=1), precio=200)

        else:
            confirmado = False

        if(confirmado):
            abonado_servicio.save(cliente)
            abono.ClienteId = cliente.id
            abono_servicio.save(abono)
            plaza.ClienteId = cliente.id
            plaza_servicio.save(plaza)
            # plaza.cliente = cliente
            #parking_servicio.find_all().dinero_abonos.append(abono.precio)
            parking_servicio.find_all().dinero_abonos += abono.precio
            parking_servicio.edit(parking_servicio.find_all())

        else:
            raise DatosErroneos

        return confirmado

    def renovacion_abono(self, dni, pin, tipo_abono):
        modificado = False
        cliente = abonado_servicio.find_by_dni(dni)
        abono = abono_servicio.find_by_cliente(cliente)
        abono2 = abono_servicio.find_by_pin(pin)

        if(abono == abono2 and abono != None):
            if(tipo_abono.lower() == "mensual"):
                abono.fecha_cancelacion = abono.fecha_cancelacion + relativedelta(months=1)
                abono.tipo = tipo_abono
                #cliente.abono = tipo_abono
                abono.precio = 25
                modificado = True

            elif(tipo_abono.lower() == "trimestral"):
                abono.fecha_cancelacion = abono.fecha_cancelacion + relativedelta(months=3)
                abono.tipo = tipo_abono
                #cliente.abono = tipo_abono
                abono.precio = 70
                modificado = True

            elif(tipo_abono.lower() == "semestral"):
                abono.fecha_cancelacion = abono.fecha_cancelacion + relativedelta(months=6)
                abono.tipo = tipo_abono
                #cliente.abono = tipo_abono
                abono.precio = 130
                modificado = True

            elif(tipo_abono.lower() == "anual"):
                abono.fecha_cancelacion = abono.fecha_cancelacion + relativedelta(years=1)
                abono.tipo = tipo_abono
                #cliente.abono = tipo_abono
                abono.precio = 200
                abono_servicio.edit(abono)
                modificado = True
        else:
            raise AbonoNoEncontrado

        if(not modificado):
            raise DatosErroneos
        else:
            abono_servicio.edit(abono)

        parking_servicio.find_all().dinero_abonos += abono.precio
        parking_servicio.edit(parking_servicio.find_all())
        return modificado

    def modificar_datos_abono(self, dni, pin, nombre, apellidos, num_tarjeta, email):
        modificado = False
        cliente = abonado_servicio.find_by_dni(dni)
        abono = abono_servicio.find_by_cliente(cliente)
        abono2 = abono_servicio.find_by_pin(pin)

        if(abono == abono2 and abono != None):
            if(nombre != ""):
                cliente.nombre = nombre
                modificado = True
            if(apellidos != ""):
                cliente.apellidos = apellidos
                modificado = True
            if(num_tarjeta != ""):
                cliente.num_tarjeta = num_tarjeta
                modificado = True
            if(email != ""):
                cliente.email = email
                modificado = True

            if(modificado):
                abono.cliente_abonado = cliente
                abono_servicio.edit(abono)
                abonado_servicio.edit(cliente)
            else:
                raise DatosErroneos
        else:
            raise AbonoNoEncontrado

        return modificado

    def borrar_abono(self, dni, pin):
        cliente = abonado_servicio.find_by_dni(dni)
        abono = abono_servicio.find_by_cliente(cliente)
        abono2 = abono_servicio.find_by_pin(pin)
        borrado = False

        if(abono == abono2 and abono != None):
            abono_servicio.delete(abono)

            for plaza in parking_servicio.find_all_plazas():
                if(plaza.cliente == cliente):
                    plaza.ClienteId = -1
                    plaza_servicio.edit(plaza)
                    abonado_servicio.delete(cliente)

            borrado = True
        else:
            raise AbonoNoEncontrado

        return borrado

    def caducidad_abonos_mes(self, mes):
        abonos = []
        for abono in abono_servicio.find_all():
            if(abono.fecha_cancelacion.month == int(mes)):
                abonos.append(abono)

        return abonos

    def caducidad_abonos_10_dias(self):
        abonos = []
        for abono in abono_servicio.find_all():
            if(abono.fecha_cancelacion >= datetime.now() and abono.fecha_cancelacion <= (datetime.now() + relativedelta(days=10))):
                abonos.append(abono)
        
        return abonos



admin_servicio = AdminServicio()
# print(admin_servicio.comprobar_password("1234"))
# print(admin_servicio.facturacion(datetime(2020, 10, 10), datetime(2020, 12, 14)))
# print(admin_servicio.consulta_cobro_abonados())
# print(admin_servicio.alta_abono("1235", "Teresa", "Diaz", "14141241", "teresa@email.com", "1234FFF", "turismo", "mensual"))
# print(admin_servicio.renovacion_abono("1234", 111, "anual"))
# print(admin_servicio.borrar_abono("1234", 111))
# print(admin_servicio.caducidad_abonos_mes("12"))
# print(admin_servicio.caducidad_abonos_10_dias())
# for abono in abono_servicio.findAll():
#     print(abono)

