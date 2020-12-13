from controllers.parking_controller import parking_controller
from models.AbonoNoEncontrado import AbonoNoEncontrado
from models.ClienteNoEncontrado import ClienteNoEncontrado
from models.DatosErroneos import DatosErroneos
from services.abonado_servicio import abonado_servicio
from services.administrador_servicio import admin_servicio


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
                print("\nPuede aparcar su vehículo")


        except ClienteNoEncontrado:
            print("\nNo se encuentra ningún cliente abonado con esos datos")

    def retirar_abonados(self, matricula, id, pin):
        try:
            if(abonado_servicio.retirar_abonados(matricula, id, pin)):
                print("\nPuede retirar su vehículo")

        except ClienteNoEncontrado:
            print("\nNo se encuentra ningún cliente abonado con esos datos")


    def obtener_abono(self, dni, pin):
        try:
            if(abonado_servicio.obtener_abono(dni, pin) != None):
                parking_controller.imprimir_abono_dni(dni, pin)

        except AbonoNoEncontrado:
            print("\nNo existe ningún abono con esos datos")


    def obtener_datos_personales(self, dni, pin):
        try:

            if(abonado_servicio.obtener_datos_personales(dni, pin) != None):
                cliente = abonado_servicio.obtener_datos_personales(dni, pin)
                print(f"\nNombre: {cliente.nombre}\n"
                      f"Apellidos: {cliente.apellidos}\n"
                      f"Email: {cliente.email}\n"
                      f"DNI: {cliente.dni}")
        except ClienteNoEncontrado:
            print("\nNo se encuentra ningún cliente abonado con esos datos")


    def modificar_datos_abono(self, dni, pin, nombre, apellidos, num_tarjeta, email):
        try:
            if(admin_servicio.modificar_datos_abono(dni, pin, nombre, apellidos, num_tarjeta, email)):
                print("\nLos datos se han modificado correctamente")
                cliente = abonado_servicio.obtener_datos_personales(dni, pin)
                print(f"Nombre: {cliente.nombre}\nApellidos: {cliente.apellidos}\nEmail: {cliente.email}"
                      f"\nDNI: {cliente.dni}")
        except AbonoNoEncontrado:
            print("\nNo existe ningún abono con esos datos")
        except DatosErroneos:
            print("\nNo se han podido modificar los datos")


    def renovacion_abono(self, dni, pin, tipo_abono):
        try:
            if(admin_servicio.renovacion_abono(dni, pin, tipo_abono)):
                print("\nSu abono se ha renovado correctamente")
                parking_controller.imprimir_abono_dni(dni, pin)

        except AbonoNoEncontrado:
            print("\nNo existe ningún abono con esos datos")
        except DatosErroneos:
            print("\nNo se han podido modificar los datos")


    def borrar_abono(self, dni, pin):
        try:
            if(admin_servicio.borrar_abono(dni, pin)):
                print("\nEl abono se ha borrado correctamente")

        except AbonoNoEncontrado:
            print("\nNo existe ningún abono con esos datos")





cliente_abonado_controller = ClienteAbonadoController()
