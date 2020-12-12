from controllers.cliente_abonado_controller import cliente_abonado_controller
from controllers.cliente_controller import cliente_controller
from controllers.main_controller import main_controller
from models.cliente_abonado import ClienteAbonado
from datetime import datetime, date, timedelta
from random import randint
from math import floor
from dateutil.relativedelta import relativedelta

print(main_controller.bienvenida()+"\n")
#print(main_controller.menu_principal())
continuar = True
#continuar2 = True

while continuar:
    op = int(input(main_controller.menu_principal() + "\n"))
    continuar2 = True
    continuar3 = True
    if(op == 1):
        while continuar2:
            op = int(input("\n" + cliente_controller.menu_cliente() + "\n"))
            if(op == 1):
                matricula = input("Introduce la matrícula de su vehículo: ")
                tipo = input("Introduce el tipo de vehículo (turismo, motocicleta o movilidad reducida): ")
                cliente_controller.depositar_vehiculo(matricula, tipo)

            elif(op == 2):
                matricula = input("Introduce la matrícula de su vehículo: ")
                id = input("Introduce el identificador de su plaza: ")
                pin = input("Introduce el pin de su ticket: ")
                cliente_controller.retirar_vehiculo(matricula, id, pin)

            elif(op == 3):
                pass

            elif(op == 0):
                continuar2 = False

    elif(op == 2):
        while continuar3:
            op = int(input("\n" + cliente_abonado_controller.menu_abonado() + "\n"))
            if(op == 1):
                pass

            elif(op == 2):
                pass

            elif(op == 3):
                pass

            elif(op == 4):
                pass

            elif(op == 5):
                pass

            elif(op == 6):
                pass

            elif(op == 7):
                pass

            elif(op == 0):
                continuar3 = False

    elif(op == 3):
        pass

    elif(op == 0):
        continuar = False




print("Gracias por usar el parking")

# if(op == 1):
#     pass
#
# elif(op == 2):
#     pass
#
# elif(op == 3):
#     pass
#
# elif(op == 0):
#     continuar = False
#
# cliente = ClienteAbonado("1234", "Teresa", "Diaz", "123456", "teresa@email.com", None)
#
# print(cliente.nombre)
#
# fecha1 = datetime(2020, 12, 10, 18, 0, 0)
# fecha = date(2020,12,12)
# print(fecha + timedelta(days=30))
# print(fecha.month)
# print(fecha + relativedelta(months=1))
# print(datetime.now() + relativedelta(months=1))
# fecha2 = datetime.now()
# tiempo = fecha2 -fecha1
#
# print(floor(tiempo.total_seconds()/60))
#
# #print(hoy.day, hoy.month, hoy.year)
#
# alea = randint(111111, 999999)
# print(alea)



