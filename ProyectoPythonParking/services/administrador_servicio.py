from random import randint
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta

from models.AbonoNoEncontrado import AbonoNoEncontrado
from models.DatosErroneos import DatosErroneos
from models.abono import Abono
from models.cliente_abonado import ClienteAbonado
from models.vehiculo import Turismo, Motocicleta, MovilidadReducida
from services.abonado_servicio import abonado_servicio
from services.abono_servicio import abono_servicio
from services.parking_servicio import parking_servicio
from services.ticket_servicio import ticket_servicio



class AdminServicio():

    def comprobar_password(self, password):
        if(password == "1234"):
            return True

    def facturacion(self, fecha1, fecha2):
        total = 0
        coste = []

        for ticket in ticket_servicio.find_all():
            if(ticket.fecha_salida >= fecha1 and ticket.fecha_salida <= fecha2):
                coste.append(ticket.coste)

        if(len(coste) > 0):
            for c in coste:
                total += c

        return round(total, 2)


    def consulta_cobro_abonados(self):
        total = 0
        if(len(parking_servicio.find_all().dinero_abonos) > 0):
            for d in parking_servicio.find_all().dinero_abonos:
                total += d

        return round(total, 2)

    def alta_abono(self, dni, nombre, apellidos, num_tarjeta, email, matricula, tipo_vehiculo, tipo_abono):
        confirmado = True

        if(tipo_vehiculo.lower() == "turismo"):
            vehiculo = Turismo(matricula)
            plaza = parking_servicio.plazas_libres_turismo()[0]

        elif(tipo_vehiculo.lower() == "motocicleta"):
            vehiculo = Motocicleta(matricula)
            plaza = parking_servicio.plazas_libres_moto()[0]

        elif(tipo_vehiculo.lower() == "movilidad reducida"):
            vehiculo = MovilidadReducida(matricula)
            plaza = parking_servicio.plazas_libres_movreducida()[0]

        else:
            confirmado = False

        if(plaza != None):
            id = plaza.id


        cliente = ClienteAbonado(dni, nombre, apellidos, num_tarjeta, email, vehiculo, tipo_abono, id)
        pin = randint(111111, 999999)
        fecha = datetime.now()
        if(tipo_abono.lower() == "mensual"):
            abono = Abono(pin, tipo_abono, datetime.now(), fecha + relativedelta(months=1), cliente, 25)

        elif(tipo_abono.lower() == "trimestral"):
            abono = Abono(pin, tipo_abono, datetime.now(), fecha + relativedelta(months=3), cliente, 70)

        elif(tipo_abono.lower() == "semestral"):
            abono = Abono(pin, tipo_abono, datetime.now(), fecha + relativedelta(months=6), cliente, 130)

        elif(tipo_abono.lower() == "anual"):
            abono = Abono(pin, tipo_abono, datetime.now(), fecha + relativedelta(years=1), cliente, 200)

        else:
            confirmado = False

        if(confirmado):
            abonado_servicio.save(cliente)
            abono_servicio.save(abono)
            plaza.cliente = cliente
            parking_servicio.find_all().dinero_abonos.append(abono.precio)

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
                cliente.abono = tipo_abono
                abono.precio = 25
                modificado = True

            elif(tipo_abono.lower() == "trimestral"):
                abono.fecha_cancelacion = abono.fecha_cancelacion + relativedelta(months=3)
                abono.tipo = tipo_abono
                cliente.abono = tipo_abono
                abono.precio = 70
                modificado = True

            elif(tipo_abono.lower() == "semestral"):
                abono.fecha_cancelacion = abono.fecha_cancelacion + relativedelta(months=6)
                abono.tipo = tipo_abono
                cliente.abono = tipo_abono
                abono.precio = 130
                modificado = True

            elif(tipo_abono.lower() == "anual"):
                abono.fecha_cancelacion = abono.fecha_cancelacion + relativedelta(years=1)
                abono.tipo = tipo_abono
                cliente.abono = tipo_abono
                abono.precio = 200
                abono_servicio.edit(abono)
                modificado = True
        else:
            raise AbonoNoEncontrado

        if(not modificado):
            raise DatosErroneos

        parking_servicio.find_all().dinero_abonos.append(abono.precio)
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
            for plaza in parking_servicio.find_all().lista_plazas:
                if(plaza.cliente == cliente):
                    plaza.cliente = None

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
