from models.DatosErroneos import DatosErroneos
from services.cliente_servicio import cliente_servicio


class ClienteController():
   def menu_cliente(self):
       return "Pulse 1 para depositar un vehículo\n" \
              "Pulse 2 para retirar un vehículo\n" \
              "Pulse 3 para obtener un abono\n" \
              "Pulse 0 para salir"

   def depositar_vehiculo(self, matricula, tipo):
       try:

           if(cliente_servicio.depositar_vehiculo(matricula, tipo)):
               print("\nPuede aparcar su vehículo en la plaza asignada")
               #imprimir ticket

           # else:
           #     raise DatosErroneos

       except DatosErroneos:
           print("\nLos datos introducidos no son correctos")

   def retirar_vehiculo(self, matricula, id, pin):

       try:
           total = cliente_servicio.retirar_vehiculo(matricula, id, pin)
           if(total >= 0):
               print(f"\n Importe a pagar: {total}€")
               print("Puede retirar su vehículo")

           # else:
           #     raise DatosErroneos

       except DatosErroneos:
            print("\nLos datos introducidos no son correctos")


cliente_controller = ClienteController()
