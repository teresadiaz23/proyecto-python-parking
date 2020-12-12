class MainController():
    def bienvenida(self):
        return "Bienvenido al parking de los Salesianos de Triana"

    def menu_principal(self):
        return "Pulse 1 si eres cliente normal \n" \
               "Pulse 2 si eres cliente abonado\n" \
               "Pulse 3 si eres administrador\n" \
               "Pulse 0 para salir"
        # menu = {1:"Cliente", 2: "Abonado", 3: "Administrador"}
        # for k, v in menu.items():
        #     print(k, v)



main_controller = MainController()
#print(main_controller.menu_principal())
