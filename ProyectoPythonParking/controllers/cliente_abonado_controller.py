from models.ClienteNoEncontrado import ClienteNoEncontrado
from services.abonado_servicio import abonado_servicio


class ClienteAbonadoController():

    def menu_abonado(self):
        return "\nPulse 1 para depositar un vehículo \n" \
               "Pulse 2 para retirar un vehículo \n" \
               "Pulse 3 para ver su abono \n" \
               "Pulse 4 para ver sus datos personales \n" \
               "Pulse 5 para modificar datos personales \n" \
               "Pulse 6 para renovar su abono \n" \
               "Pulse 7 para borrar su abono \n" \
               "Pulse 0 para salir"

    def depositar_abonados(self, matricula, dni):
        try:
            if(abonado_servicio.depositar_abonados(matricula, dni)):
                print("\n Puede aparcar su vehículo")


        except ClienteNoEncontrado:
            print("\nNo se encuentra ningún cliente abonado con esos datos")

    def retirar_abonados(self, matricula, id, pin):
        try:
            if(abonado_servicio.retirar_abonados(matricula, id, pin)):
                print("\nPuede retirar su vehículo")

        except ClienteNoEncontrado:
            print("\nNo se encuentra ningún cliente abonado con esos datos")




cliente_abonado_controller = ClienteAbonadoController()
