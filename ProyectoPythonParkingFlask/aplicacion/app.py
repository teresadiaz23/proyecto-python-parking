from flask import Flask, render_template, abort, request
from flask_bootstrap import Bootstrap

from aplicacion.controllers.parking_controller import parking_controller
from aplicacion.models import DatosErroneos
from aplicacion.services.cliente_servicio import cliente_servicio
from aplicacion.services.ticket_servicio import ticket_servicio

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
        #return "Bienvenido al parking de los Salesianos de Triana"

        return render_template("index.html")


@app.route('/cliente/')
def cliente_index():

        return render_template("cliente_index.html")


@app.route('/cliente/depositar/', methods=["get", "post"])
def depositar_cliente():
    if request.method == 'POST':
        matricula = request.form.get("matricula")
        tipo = request.form.get("tipo")


        if(cliente_servicio.depositar_vehiculo(matricula, tipo)):
               #print("\nPuede aparcar su vehículo en la plaza asignada")
               #parking_controller.imprimir_ticket(ticket_servicio.find_all()[len(ticket_servicio.find_all()) - 1])
            ticket = ticket_servicio.find_all()[len(ticket_servicio.find_all()) - 1]

        # try:
        #
        #    if(cliente_servicio.depositar_vehiculo(matricula, tipo)):
        #        #print("\nPuede aparcar su vehículo en la plaza asignada")
        #        #parking_controller.imprimir_ticket(ticket_servicio.find_all()[len(ticket_servicio.find_all()) - 1])
        #         ticket= ticket_servicio.find_all()[len(ticket_servicio.find_all()) - 1]
        # except DatosErroneos:
        #    print("\nLos datos introducidos no son correctos")

        return render_template("ticket.html", matricula=matricula, tipo=tipo, ticket=ticket)
    else:
        return render_template("cliente_depositar.html")

@app.route('/cliente/retirar/', methods=["get","post"])
def retirar_cliente():
    if request.method == 'POST':
        matricula = request.form.get("matricula")
        id = int(request.form.get("id"))
        pin = int(request.form.get("pin"))
        total = cliente_servicio.retirar_vehiculo(matricula, id, pin)

        if(total >= 0):
            # print(f"\nImporte a pagar: {total}€")
            # print("Puede retirar su vehículo")
            return render_template("confirmacion.html", matricula=matricula, id=id, pin=pin, total=total)
        # try:
        #     total = cliente_servicio.retirar_vehiculo(matricula, id, pin)
        #     if(total >= 0):
        #         print(f"\nImporte a pagar: {total}€")
        #         print("Puede retirar su vehículo")
        #
        # except DatosErroneos:
        #     print("\nLos datos introducidos no son correctos")


    else:
        return render_template("cliente_retirar.html")



@app.route('/abonado/')
def abonado_index():

        return render_template("cliente_index.html")

@app.route('/admin/')
def admin_index():

        return render_template("cliente_index.html")

