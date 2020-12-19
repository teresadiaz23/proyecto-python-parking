from flask import Flask, render_template, abort, request
from flask_bootstrap import Bootstrap

from aplicacion.controllers.parking_controller import parking_controller
from aplicacion.models import DatosErroneos
from aplicacion.services.cliente_servicio import cliente_servicio
from aplicacion.services.ticket_servicio import ticket_servicio
from aplicacion.services.abono_servicio import abono_servicio
from aplicacion.services.administrador_servicio import admin_servicio
from aplicacion.services.parking_servicio import parking_servicio
from aplicacion.models import AbonoNoEncontrado
from aplicacion.models import ClienteNoEncontrado
from aplicacion.services.abonado_servicio import abonado_servicio



app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
        #return "Bienvenido al parking de los Salesianos de Triana"

        return render_template("index.html")


#Rutas cliente normal
@app.route('/cliente/')
def cliente_index():

        return render_template("./cliente/cliente_index.html")


@app.route('/cliente/depositar/', methods=["get", "post"])
def depositar_cliente():
    if request.method == 'POST':
        matricula = request.form.get("matricula")
        tipo = request.form.get("tipo")


        # if(cliente_servicio.depositar_vehiculo(matricula, tipo)):
        #        #print("\nPuede aparcar su vehículo en la plaza asignada")
        #        #parking_controller.imprimir_ticket(ticket_servicio.find_all()[len(ticket_servicio.find_all()) - 1])
        #     ticket = ticket_servicio.find_all()[len(ticket_servicio.find_all()) - 1]

        try:

           if(cliente_servicio.depositar_vehiculo(matricula, tipo)):
               #print("\nPuede aparcar su vehículo en la plaza asignada")
               #parking_controller.imprimir_ticket(ticket_servicio.find_all()[len(ticket_servicio.find_all()) - 1])
               ticket = ticket_servicio.find_all()[len(ticket_servicio.find_all()) - 1]
               return render_template("./cliente/ticket.html", matricula=matricula, tipo=tipo, ticket=ticket)
        # except DatosErroneos:
        #    print("\nLos datos introducidos no son correctos")
        except:
           return render_template("./errores/error.html",error="Los datos introducidos no son correctos")


    else:
        return render_template("./cliente/cliente_depositar.html")




@app.route('/cliente/retirar/', methods=["get","post"])
def retirar_cliente():
    if request.method == 'POST':

        #total = cliente_servicio.retirar_vehiculo(matricula, id, pin)

        # if(total >= 0):
        #     # print(f"\nImporte a pagar: {total}€")
        #     # print("Puede retirar su vehículo")
        #     return render_template("./cliente/confirmacion.html", matricula=matricula, id=id, pin=pin, total=total)
        try:
            matricula = request.form.get("matricula")
            id = int(request.form.get("id"))
            pin = int(request.form.get("pin"))
            total = cliente_servicio.retirar_vehiculo(matricula, id, pin)
            if(total >= 0):

                return render_template("./cliente/confirmacion.html", matricula=matricula, id=id, pin=pin, total=total)
        except:
           return render_template("./errores/error.html", error="Los datos introducidos no son correctos")
        # except DatosErroneos:
        #     print("\nLos datos introducidos no son correctos")


    else:
        return render_template("./cliente/cliente_retirar.html")


@app.route('/cliente/abono/', methods=["get", "post"])
def alta_abono():
    if request.method == 'POST':
        dni = request.form.get("dni")
        nombre = request.form.get("nombre")
        apellidos = request.form.get("apellidos")
        num_tarjeta = request.form.get("num_tarjeta")
        email = request.form.get("email")
        matricula = request.form.get("matricula")
        tipo_vehiculo = request.form.get("tipo_vehiculo")
        tipo_abono = request.form.get("tipo_abono")


        try:
            if(admin_servicio.alta_abono(dni, nombre, apellidos, num_tarjeta, email, matricula, tipo_vehiculo, tipo_abono)):
                #print("\nHa obtenido un abono correctamente")
                abono = abono_servicio.find_all()[len(abono_servicio.find_all()) - 1]

                return render_template("./cliente/abono.html",
                                       dni=dni, nombre=nombre, apellidos=apellidos, num_tarjeta=num_tarjeta,
                                       email=email, matricula=matricula,
                                       tipo_vehiculo=tipo_vehiculo, tipo_abono=tipo_abono, abono=abono)
        except:
            return render_template("./errores/error.html", error="No se ha podido generar el abono correctamente")

    else:
        return render_template("./cliente/cliente_nuevo_abono.html")






#Rutas cliente abonado

@app.route('/abonado/')
def abonado_index():

        return render_template("./abonado/abonado_index.html")


@app.route('/abonado/depositar/', methods=["get", "post"])
def depositar_abonados():
    if request.method == 'POST':
        matricula = request.form.get("matricula")
        dni = request.form.get("dni")
        #try:
        if(abonado_servicio.depositar_abonados(matricula, dni)):
                #print("\nPuede aparcar su vehículo")
            return render_template("./abonado/confirmacion.html", matricula=matricula, dni=dni)

        # except:
        #     return render_template("./errores/error.html", error="No se encuentra ningún cliente abonado con esos datos")

    return render_template("./abonado/abonado_depositar.html")

@app.route('/abonado/retirar/', methods=["get", "post"])
def retirar_abonados():
    if request.method == 'POST':

        try:
            matricula = request.form.get("matricula")
            id = int(request.form.get("id"))
            pin = int(request.form.get("pin"))
            if(abonado_servicio.retirar_abonados(matricula, id, pin)):
                print("\nPuede retirar su vehículo")

        except ClienteNoEncontrado:
            print("\nNo se encuentra ningún cliente abonado con esos datos")

    return render_template("./abonado/abonado_retirar.html")


@app.route('/abonado/abono/', methods=["get", "post"])
def consultar_abono():
    if request.method == 'POST':
        try:
            dni = request.form.get("dni")
            pin = int(request.form.get("pin"))
            if(abonado_servicio.obtener_abono(dni, pin) != None):
                parking_controller.imprimir_abono_dni(dni, pin)

        except AbonoNoEncontrado:
            print("\nNo existe ningún abono con esos datos")
        return render_template("./abonado/abonado_ver_abono.html")

@app.route('/abonado/datos-personales/', methods=["get", "post"])
def consultar_datos_personales():
    if request.method == 'POST':
        try:
            dni = request.form.get("dni")
            pin = int(request.form.get("pin"))

            if(abonado_servicio.obtener_datos_personales(dni, pin) != None):
                cliente = abonado_servicio.obtener_datos_personales(dni, pin)
                print(f"\nNombre: {cliente.nombre}\n"
                      f"Apellidos: {cliente.apellidos}\n"
                      f"Email: {cliente.email}\n"
                      f"DNI: {cliente.dni}")
        except ClienteNoEncontrado:
            print("\nNo se encuentra ningún cliente abonado con esos datos")

        return render_template("./abonado/abonado_ver_datos.html")


@app.route('/abonado/datos-personales/editar/', methods=["get", "post"])
def modificar_datos_abono():
    if request.method == 'POST':
        try:
            dni = request.form.get("dni")
            pin = int(request.form.get("pin"))
            nombre = request.form.get("nombre")
            apellidos = request.form.get("apellidos")
            num_tarjeta = request.form.get("num_tarjeta")
            email = request.form.get("email")


            if(admin_servicio.modificar_datos_abono(dni, pin, nombre, apellidos, num_tarjeta, email)):
                print("\nLos datos se han modificado correctamente")
                cliente = abonado_servicio.obtener_datos_personales(dni, pin)
                print(f"Nombre: {cliente.nombre}\nApellidos: {cliente.apellidos}\nEmail: {cliente.email}"
                      f"\nDNI: {cliente.dni}")
        except AbonoNoEncontrado:
            print("\nNo existe ningún abono con esos datos")
        except DatosErroneos:
            print("\nNo se han podido modificar los datos")

        return render_template("./abonado/abonado_modificar_datos.html")


@app.route('/abonado/abono/renovar/', methods=["get", "post"])
def renovar_abono():
    if request.method == 'POST':
        try:
            dni = request.form.get("dni")
            pin = int(request.form.get("pin"))
            tipo_abono = request.form.get("tipo_abono")

            if(admin_servicio.renovacion_abono(dni, pin, tipo_abono)):
                print("\nSu abono se ha renovado correctamente")
                parking_controller.imprimir_abono_dni(dni, pin)

        except AbonoNoEncontrado:
            print("\nNo existe ningún abono con esos datos")
        except DatosErroneos:
            print("\nNo se han podido modificar los datos")

        return render_template("./abonado/abonado_renovar_abono.html")


@app.route('/abonado/abono/borrar/', methods=["get", "post"])
def borrar_abono():
    if request.method == 'POST':
        try:
            dni = request.form.get("dni")
            pin = int(request.form.get("pin"))


            if(admin_servicio.borrar_abono(dni, pin)):
                print("\nEl abono se ha borrado correctamente")

        except AbonoNoEncontrado:
            print("\nNo existe ningún abono con esos datos")

        return render_template("./abonado/abonado_borrar_abono.html")


#Rutas adminstrador

@app.route('/admin/')
def admin_index():

        return render_template("cliente_index.html")

