from models.AbonoNoEncontrado import AbonoNoEncontrado
from models.MesIncorrecto import MesIncorrecto
from services.abonado_servicio import abonado_servicio
from services.abono_servicio import abono_servicio
from services.parking_servicio import parking_servicio
from services.ticket_servicio import ticket_servicio


class ParkingController():

    def plazas_libres(self):

        print(f"Hay {len(parking_servicio.plazas_libres_turismo())} plazas de turismos, "
              f"{len(parking_servicio.plazas_libres_moto())} plazas de motocicletas y "
              f"{len(parking_servicio.plazas_libres_movreducida())} plazas de movilidad reducida libres")


    def imprimir_ticket(self, ticket):
        print("*"*40)
        print("*               Ticket                 *")
        print("*                                      *")
        print(f"*    Matrícula: {ticket.matricula}                *")
        print(f"*    Fecha depósito: {ticket.fecha_deposito.day}/{ticket.fecha_deposito.month}/{ticket.fecha_deposito.year}        *")
        print(f"*    Hora: {ticket.fecha_deposito.hour}:{ticket.fecha_deposito.minute}:{ticket.fecha_deposito.second}                     *")
        print(f"*    Id Plaza: {ticket.id_plaza}                       *")
        print(f"*    Pin: {ticket.pin}                       *")
        print("*                                      *")
        print("*                                      *")
        print("*"*40)

    def imprimir_abono(self, abono):
        print("-"*40)
        print("|               Abono                  |")
        print("|                                      |")
        print(f"|    Cliente: {abono.cliente_abonado.nombre} {abono.cliente_abonado.apellidos}             |")
        print(f"|    Tipo: {abono.tipo}                     |")
        print(f"|    Pin: {abono.pin}                       |")
        print(f"|    Id Plaza: {abono.cliente_abonado.id_plaza}                       |")
        print(f"|    Fecha Activación: {abono.fecha_activacion.day}/{abono.fecha_activacion.month}/{abono.fecha_activacion.year}      |")
        print(f"|    Fecha Caducidad: {abono.fecha_cancelacion.day}/{abono.fecha_cancelacion.month}/{abono.fecha_cancelacion.year}        |")
        print(f"|    Precio: {abono.precio} €                      |")
        print("|                                      |")
        print("|                                      |")
        print("-"*40)


    def imprimir_abono_dni(self, dni, pin):
        cliente = abonado_servicio.findByDni(dni)
        abono = abono_servicio.findByCliente(cliente)
        abono2 = abono_servicio.findByPin(pin)

        try:

            if(abono == abono2 and abono != None):
                print("-"*40)
                print("|               Abono                  |")
                print("|                                      |")
                print(f"|    Cliente: {abono.cliente_abonado.nombre} {abono.cliente_abonado.apellidos}             |")
                print(f"|    Tipo: {abono.tipo}                     |")
                print(f"|    Pin: {abono.pin}                       |")
                print(f"|    Id Plaza: {abono.cliente_abonado.id_plaza}                       |")
                print(f"|    Fecha Activación: {abono.fecha_activacion.day}/{abono.fecha_activacion.month}/{abono.fecha_activacion.year}      |")
                print(f"|    Fecha Caducidad: {abono.fecha_cancelacion.day}/{abono.fecha_cancelacion.month}/{abono.fecha_cancelacion.year}        |")
                print(f"|    Precio: {abono.precio} €                      |")
                print("|                                      |")
                print("|                                      |")
                print("-"*40)
            else:
                raise AbonoNoEncontrado

        except AbonoNoEncontrado:
            print("\n No se ha encontrado ningún abono con esos datos")

    def imprimir_mes(self, mes):
        meses = {1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio", 7: "Julio",
                 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"}


        for k, v in meses.items():
            if(k == mes):
                return v
        if(mes not in meses.values()):
            raise MesIncorrecto


        # try:
        #
        #     for k, v in meses.items():
        #         if(k == mes):
        #             return v
        #     if(mes not in meses.values()):
        #         raise MesIncorrecto
        #
        # except MesIncorrecto:
        #     print("\nEse mes no existe")

parking_controller = ParkingController()
#parking_controller.imprimir_ticket(ticket_servicio.findByPin(111111))
#parking_controller.imprimir_abono(abono_servicio.findByPin(111))
#parking_controller.imprimir_abono_dni("1234", 111)
