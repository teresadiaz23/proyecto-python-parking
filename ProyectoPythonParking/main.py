from controllers.admin_controller import admin_controller
from controllers.cliente_abonado_controller import cliente_abonado_controller
from controllers.cliente_controller import cliente_controller
from controllers.main_controller import main_controller
from controllers.parking_controller import parking_controller

from datetime import datetime

from models.MesIncorrecto import MesIncorrecto

print(main_controller.bienvenida())

continuar = True

while continuar:
    op = input(main_controller.menu_principal() + "\n")
    continuar2 = True
    continuar3 = True
    continuar4 = True
    if(op == "1"):
        while continuar2:
            op = input(cliente_controller.menu_cliente() + "\n")
            if(op == "1"):
                parking_controller.plazas_libres()
                matricula = input("Introduce la matrícula de su vehículo: ")
                tipo = input("Introduce el tipo de vehículo (turismo, motocicleta o movilidad reducida): ")
                cliente_controller.depositar_vehiculo(matricula, tipo)

            elif(op == "2"):
                matricula = input("Introduce la matrícula de su vehículo: ")
                id = int(input("Introduce el identificador de su plaza: "))
                pin = int(input("Introduce el pin de su ticket: "))
                cliente_controller.retirar_vehiculo(matricula, id, pin)

            elif(op == "3"):
                dni = input("Introduce su dni: ")
                nombre = input("Introduce su nombre: ")
                apellidos = input("Introduce sus apellidos: ")
                num_tarjeta = input("Introduce el número de su tarjeta de crédito: ")
                email = input("Introduce su email: ")
                matricula = input("Introduce la matrícula de su vehículo: ")
                tipo_vehiculo = input("Introduce el tipo de vehículo (turismo, motocicleta o movilidad reducida): ")
                tipo_abono = input("Introduce el tipo de abono (mensual, trimestral, semestral o anual): ")
                admin_controller.alta_abono(dni, nombre, apellidos, num_tarjeta, email, matricula, tipo_vehiculo, tipo_abono)

            elif(op == "0"):
                print("Saliendo al menú principal")
                continuar2 = False

            else:
                print("\nEsa opción no está disponible")

    elif(op == "2"):
        while continuar3:
            op = input(cliente_abonado_controller.menu_abonado() + "\n")
            if(op == "1"):
                matricula = input("Introduce la matrícula de su vehículo: ")
                dni = input("Introduce su dni: ")
                cliente_abonado_controller.depositar_abonados(matricula, dni)

            elif(op == "2"):
                matricula = input("Introduce la matrícula de su vehículo: ")
                id = int(input("Introduce el identificador de su plaza: "))
                pin = int(input("Introduce su pin: "))
                cliente_abonado_controller.retirar_abonados(matricula, id, pin)

            elif(op == "3"):
                dni = input("Introduce su dni: ")
                pin = int(input("Introduce su pin: "))
                cliente_abonado_controller.obtener_abono(dni, pin)

            elif(op == "4"):
                dni = input("Introduce su dni: ")
                pin = int(input("Introduce su pin: "))
                cliente_abonado_controller.obtener_datos_personales(dni, pin)

            elif(op == "5"):
                dni = input("Introduce su dni: ")
                pin = int(input("Introduce su pin: "))
                nombre = input("Introduce su nombre: ")
                apellidos = input("Introduce sus apellidos: ")
                num_tarjeta = input("Introduce el número de su tarjeta de crédito: ")
                email = input("Introduce su email: ")
                cliente_abonado_controller.modificar_datos_abono(dni, pin, nombre, apellidos, num_tarjeta, email)

            elif(op == "6"):
                dni = input("Introduce su dni: ")
                pin = int(input("Introduce su pin: "))
                tipo_abono = input("Introduce el tipo de abono (mensual, trimestral, semestral o anual): ")
                cliente_abonado_controller.renovacion_abono(dni, pin, tipo_abono)

            elif(op == "7"):
                dni = input("Introduce su dni: ")
                pin = int(input("Introduce su pin: "))
                cliente_abonado_controller.borrar_abono(dni, pin)

            elif(op == "0"):
                print("Saliendo al menú principal")
                continuar3 = False

            else:
                print("\nEsa opción no está disponible")

    elif(op == "3"):
        while continuar4:
            op = input(admin_controller.menu_admin() + "\n")
            if(op == "1"):
                admin_controller.estado_parking()

            elif(op == "2"):
                fecha1 = input("Introduce la primera fecha y hora con el formato 'aaaa,mm,dd,hh,mm': ")
                lista1 = fecha1.split(",")
                fecha2 = input("Introduce la segunda fecha y hora con el formato 'aaaa,mm,dd,hh,mm': ")
                lista2 = fecha1.split(",")

                admin_controller.facturacion(datetime(int(lista1[0]), int(lista1[1]), int(lista1[2]), int(lista1[3]), int(lista1[4]))
                                             , datetime(int(lista2[0]), int(lista2[1]), int(lista2[2]), int(lista2[3]), int(lista2[4])))


            elif(op == "3"):
                admin_controller.consulta_abonados()

            elif(op == "4"):

                try:
                    mes = int(input("Introduce un mes en número: "))
                    print(f"\nAbonos que caducan en {parking_controller.imprimir_mes(mes)}")
                    admin_controller.caducidad_abonos_mes(mes)
                except MesIncorrecto:
                     print("\nEse mes no existe")

            elif(op == "5"):
                admin_controller.caducidad_abonos_proximos_10_dias()

            elif(op == "0"):
                print("Saliendo al menú principal")
                continuar4 = False

            else:
                print("\nEsa opción no está disponible")


    elif(op == "0"):
        print("Saliendo...")
        continuar = False

    else:
        print("\nEsa opción no está disponible")




print("\nGracias por usar el parking\nBuen viaje")




