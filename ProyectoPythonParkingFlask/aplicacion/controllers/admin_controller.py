from aplicacion.controllers.parking_controller import parking_controller
from aplicacion.models import DatosErroneos
from aplicacion.services.abono_servicio import abono_servicio
from aplicacion.services.administrador_servicio import admin_servicio
from aplicacion.services.parking_servicio import parking_servicio


class AdminController():

    def menu_admin(self):
        return "\nPulse 1 para ver el estado del parking \n" \
               "Pulse 2 para ver la facturación entre dos fechas \n" \
               "Pulse 3 para consultar los abonados \n" \
               "Pulse 4 para ver los abonos que caducan en un mes específico \n" \
               "Pulse 5 para ver los abonos que caducan en los próximos 10 días \n" \
               "Pulse 0 para salir"


    def comprobar_password(self, password):
        return admin_servicio.comprobar_password(password)


    def estado_parking(self):
        lista_plazas = parking_servicio.find_all().lista_plazas

        for plaza in lista_plazas:
            if(plaza.ocupada == False and plaza.cliente == None):
                print(f"ID: {plaza.id} -> Vehículo: {plaza.tipo_vehiculo} -> Estado: Libre")

            elif(plaza.ocupada == True and plaza.cliente == None):
                print(f"ID: {plaza.id} -> Vehículo: {plaza.tipo_vehiculo} -> Estado: Ocupada")

            elif(plaza.ocupada == False and plaza.cliente != None):
                print(f"ID: {plaza.id} -> Vehículo: {plaza.tipo_vehiculo} -> Estado: Abono Libre")

            elif(plaza.ocupada == True and plaza.cliente != None):
                print(f"ID: {plaza.id} -> Vehículo: {plaza.tipo_vehiculo} -> Estado: Abono Ocupada")


    def facturacion(self, fecha1, fecha2):
        print(f"\nFacturación entre {fecha1.day}/{fecha1.month}/{fecha1.year} {fecha1.hour}:{fecha1.minute}h "
              f"y el {fecha2.day}/{fecha2.month}/{fecha2.year} {fecha2.hour}:{fecha2.minute}h "
              f"--> {admin_servicio.facturacion(fecha1, fecha2)} €")


    def consulta_abonados(self):
        i = 1
        if(len(abono_servicio.find_all()) > 0):
            for abono in abono_servicio.find_all():
                print(f"\nAbono {i}\nTipo: {abono.tipo}\nId Plaza: {abono.cliente_abonado.id_plaza}\n"
                      f"Fecha Activacion: {abono.fecha_activacion.day}/{abono.fecha_activacion.month}/{abono.fecha_activacion.year}\n"
                      f"Fecha Caducidad: {abono.fecha_cancelacion.day}/{abono.fecha_cancelacion.month}/{abono.fecha_cancelacion.year}\n"
                      f"Precio: {abono.precio} €")
                i+=1
        print(f"\nTotal facturado con los abonos: {admin_servicio.consulta_cobro_abonados()} €")


    def alta_abono(self, dni, nombre, apellidos, num_tarjeta, email, matricula, tipo_vehiculo, tipo_abono):

        try:
            if(admin_servicio.alta_abono(dni, nombre, apellidos, num_tarjeta, email, matricula, tipo_vehiculo, tipo_abono)):
                print("\nHa obtenido un abono correctamente")
                parking_controller.imprimir_abono(abono_servicio.find_all()[len(abono_servicio.find_all()) - 1])


        except DatosErroneos:
            print("\nError. No se ha podido generar el abono correctamente")



    def caducidad_abonos_mes(self, mes):
        abonos = admin_servicio.caducidad_abonos_mes(mes)
        if(len(abonos) > 0):
            i = 1
            for abono in abonos:
                print(f"\nAbono {i}\nTipo: {abono.tipo}\nId Plaza: {abono.cliente_abonado.id_plaza}\n"
                      f"Fecha Activacion: {abono.fecha_activacion.day}/{abono.fecha_activacion.month}/{abono.fecha_activacion.year}\n"
                      f"Fecha Caducidad: {abono.fecha_cancelacion.day}/{abono.fecha_cancelacion.month}/{abono.fecha_cancelacion.year}\n"
                      f"Precio: {abono.precio} €")
                i += 1

        else:
            print("\nNo hay abonos que caduquen en el mes indicado")



    def caducidad_abonos_proximos_10_dias(self):
        abonos = admin_servicio.caducidad_abonos_10_dias()
        if(len(abonos) > 0):
            i = 1
            for abono in abonos:
                print(f"\nAbono {i}\nTipo: {abono.tipo}\nId Plaza: {abono.cliente_abonado.id_plaza}\n"
                      f"Fecha Activacion: {abono.fecha_activacion.day}/{abono.fecha_activacion.month}/{abono.fecha_activacion.year}\n"
                      f"Fecha Caducidad: {abono.fecha_cancelacion.day}/{abono.fecha_cancelacion.month}/{abono.fecha_cancelacion.year}\n"
                      f"Precio: {abono.precio} €")
                i += 1

        else:
            print("\nNo hay abonos que caduquen en los próximos 10 días")



admin_controller = AdminController()
