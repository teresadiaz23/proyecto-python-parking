class MainController():
    def bienvenida(self):
        return "Bienvenido al parking robotizado"

    def menu_principal(self):
        menu = {1:"Cliente", 2: "Abonado", 3: "Administrador"}
        for k, v in menu.items():
            print(k, v)


main = MainController()
main.menu_principal()
