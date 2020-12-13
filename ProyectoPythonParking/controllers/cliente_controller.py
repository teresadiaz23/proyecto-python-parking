from controllers.parking_controller import parking_controller
from models.DatosErroneos import DatosErroneos
from services.cliente_servicio import cliente_servicio
from services.ticket_servicio import ticket_servicio


class ClienteController():
   def menu_cliente(self):
       return "\nPulse 1 para depositar un vehículo\n" \
              "Pulse 2 para retirar un vehículo\n" \
              "Pulse 3 para obtener un abono\n" \
              "Pulse 0 para salir"

   def depositar_vehiculo(self, matricula, tipo):
       try:

           if(cliente_servicio.depositar_vehiculo(matricula, tipo)):
               print("\nPuede aparcar su vehículo en la plaza asignada")
               parking_controller.imprimir_ticket(ticket_servicio.findAll()[len(ticket_servicio.findAll()) - 1])


       except DatosErroneos:
           print("\nLos datos introducidos no son correctos")

   def retirar_vehiculo(self, matricula, id, pin):

       try:
           total = cliente_servicio.retirar_vehiculo(matricula, id, pin)
           if(total >= 0):
               print(f"\n Importe a pagar: {total}€")
               print("Puede retirar su vehículo")

       except DatosErroneos:
            print("\nLos datos introducidos no son correctos")


cliente_controller = ClienteController()
