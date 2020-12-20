from datetime import datetime

from flask import Flask, render_template, abort, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from aplicacion import config
# from aplicacion.controllers.parking_controller import parking_controller
# from aplicacion.models import DatosErroneos
# from aplicacion.services.cliente_servicio import cliente_servicio
# from aplicacion.services.ticket_servicio import ticket_servicio
# from aplicacion.services.abono_servicio import abono_servicio
# from aplicacion.services.administrador_servicio import admin_servicio
# from aplicacion.services.parking_servicio import parking_servicio
# from aplicacion.models import AbonoNoEncontrado
# from aplicacion.models import ClienteNoEncontrado
# from aplicacion.services.abonado_servicio import abonado_servicio
from aplicacion.models.cliente_abonado import ClienteAbonado
from aplicacion.repositories.cliente_abonado_repositorio import cliente_abonado_repositorio
#from aplicacion.services.abonado_servicio import abonado_servicio

app = Flask(__name__)
app.config.from_object(config)
Bootstrap(app)
db = SQLAlchemy(app)



@app.route('/')
def index():
        #return "Bienvenido al parking de los Salesianos de Triana"
        clientes=ClienteAbonado.query.all()
        cliente_abonado_repositorio.lista_clientes = clientes
        abonados = cliente_abonado_repositorio.find_all()
        return render_template("index.html", abonados=abonados)

#
# #Rutas cliente normal
# @app.route('/cliente/')
# def cliente_index():
#
#         return render_template("./cliente/cliente_index.html")
#
#
# @app.route('/cliente/depositar/', methods=["get", "post"])
# def depositar_cliente():
#     if request.method == 'POST':
#         matricula = request.form.get("matricula")
#         tipo = request.form.get("tipo")
#
#
#         # if(cliente_servicio.depositar_vehiculo(matricula, tipo)):
#         #        #print("\nPuede aparcar su vehículo en la plaza asignada")
#         #        #parking_controller.imprimir_ticket(ticket_servicio.find_all()[len(ticket_servicio.find_all()) - 1])
#         #     ticket = ticket_servicio.find_all()[len(ticket_servicio.find_all()) - 1]
#
#         try:
#
#            if(cliente_servicio.depositar_vehiculo(matricula, tipo)):
#                #print("\nPuede aparcar su vehículo en la plaza asignada")
#                #parking_controller.imprimir_ticket(ticket_servicio.find_all()[len(ticket_servicio.find_all()) - 1])
#                ticket = ticket_servicio.find_all()[len(ticket_servicio.find_all()) - 1]
#                return render_template("./cliente/ticket.html", matricula=matricula, tipo=tipo, ticket=ticket)
#         # except DatosErroneos:
#         #    print("\nLos datos introducidos no son correctos")
#         except:
#            return render_template("./errores/error.html",error="Los datos introducidos no son correctos")
#
#
#     else:
#         libres_t = len(parking_servicio.plazas_libres_turismo())
#         libres_m = len(parking_servicio.plazas_libres_moto())
#         libres_mvr = len(parking_servicio.plazas_libres_movreducida())
#
#         return render_template("./cliente/cliente_depositar.html", libres_t=libres_t, libres_m=libres_m,
#                                libres_mvr=libres_mvr)
#
#
#
#
# @app.route('/cliente/retirar/', methods=["get","post"])
# def retirar_cliente():
#     if request.method == 'POST':
#
#         #total = cliente_servicio.retirar_vehiculo(matricula, id, pin)
#
#         # if(total >= 0):
#         #     # print(f"\nImporte a pagar: {total}€")
#         #     # print("Puede retirar su vehículo")
#         #     return render_template("./cliente/confirmacion.html", matricula=matricula, id=id, pin=pin, total=total)
#         try:
#             matricula = request.form.get("matricula")
#             id = int(request.form.get("id"))
#             pin = int(request.form.get("pin"))
#             total = cliente_servicio.retirar_vehiculo(matricula, id, pin)
#             if(total >= 0):
#
#                 return render_template("./cliente/confirmacion.html", matricula=matricula, id=id, pin=pin, total=total)
#         except:
#            return render_template("./errores/error.html", error="Los datos introducidos no son correctos")
#         # except DatosErroneos:
#         #     print("\nLos datos introducidos no son correctos")
#
#
#     else:
#         return render_template("./cliente/cliente_retirar.html")
#
#
# @app.route('/cliente/abono/', methods=["get", "post"])
# def alta_abono():
#     if request.method == 'POST':
#         dni = request.form.get("dni")
#         nombre = request.form.get("nombre")
#         apellidos = request.form.get("apellidos")
#         num_tarjeta = request.form.get("num_tarjeta")
#         email = request.form.get("email")
#         matricula = request.form.get("matricula")
#         tipo_vehiculo = request.form.get("tipo_vehiculo")
#         tipo_abono = request.form.get("tipo_abono")
#
#
#         try:
#             if(admin_servicio.alta_abono(dni, nombre, apellidos, num_tarjeta, email, matricula, tipo_vehiculo, tipo_abono)):
#                 #print("\nHa obtenido un abono correctamente")
#                 abono = abono_servicio.find_all()[len(abono_servicio.find_all()) - 1]
#
#                 return render_template("./cliente/abono.html",
#                                        dni=dni, nombre=nombre, apellidos=apellidos, num_tarjeta=num_tarjeta,
#                                        email=email, matricula=matricula,
#                                        tipo_vehiculo=tipo_vehiculo, tipo_abono=tipo_abono, abono=abono)
#         except:
#             return render_template("./errores/error.html", error="No se ha podido generar el abono correctamente")
#
#     else:
#         return render_template("./cliente/cliente_nuevo_abono.html")
#
#
#
#
#
#
# #Rutas cliente abonado
#
# @app.route('/abonado/')
# def abonado_index():
#
#         return render_template("./abonado/abonado_index.html")
#
#
# @app.route('/abonado/depositar/', methods=["get", "post"])
# def depositar_abonados():
#     if request.method == 'POST':
#         matricula = request.form.get("matricula")
#         dni = request.form.get("dni")
#         try:
#             if(abonado_servicio.depositar_abonados(matricula, dni)):
#                 #print("\nPuede aparcar su vehículo")
#                 return render_template("./abonado/confirmacion.html", matricula=matricula, dni=dni,
#                                    mensaje="Puede aparcar su vehículo")
#
#         except:
#             return render_template("./errores/error.html", error="No se encuentra ningún cliente abonado con esos datos")
#     else:
#         return render_template("./abonado/abonado_depositar.html")
#
# @app.route('/abonado/retirar/', methods=["get", "post"])
# def retirar_abonados():
#     if request.method == 'POST':
#
#         try:
#             matricula = request.form.get("matricula")
#             id = int(request.form.get("id"))
#             pin = int(request.form.get("pin"))
#             if(abonado_servicio.retirar_abonados(matricula, id, pin)):
#                 return render_template("./abonado/confirmacion.html", matricula=matricula, id=id, pin=pin,
#                                        mensaje="Puede retirar su vehículo")
#                 # print("\nPuede retirar su vehículo")
#
#         except:
#             return render_template("./errores/error.html", error="No se encuentra ningún cliente abonado con esos datos")
#
#     else:
#         return render_template("./abonado/abonado_retirar.html")
#
#
# @app.route('/abonado/abono/', methods=["get", "post"])
# def consultar_abono():
#     if request.method == 'POST':
#         try:
#             dni = request.form.get("dni")
#             pin = int(request.form.get("pin"))
#             if(abonado_servicio.obtener_abono(dni, pin) != None):
#                 abono = parking_controller.imprimir_abono_dni(dni, pin)
#                 return render_template("./abonado/abono.html", dni=dni, pin=pin,
#                                        abono=abono, mensaje="")
#
#         except:
#             return render_template("./errores/error.html", error="No existe ningún abono con esos datos")
#             #print("\nNo existe ningún abono con esos datos")
#     else:
#         return render_template("./abonado/abonado_ver_abono.html")
#
# @app.route('/abonado/datos-personales/', methods=["get", "post"])
# def consultar_datos_personales():
#     if request.method == 'POST':
#         try:
#             dni = request.form.get("dni")
#             pin = int(request.form.get("pin"))
#
#             if(abonado_servicio.obtener_datos_personales(dni, pin) != None):
#                 cliente = abonado_servicio.obtener_datos_personales(dni, pin)
#                 return render_template("./abonado/datos.html", dni=dni, pin=pin, cliente=cliente,
#                                        mensaje="Datos abono")
#                 # print(f"\nNombre: {cliente.nombre}\n"
#                 #       f"Apellidos: {cliente.apellidos}\n"
#                 #       f"Email: {cliente.email}\n"
#                 #       f"DNI: {cliente.dni}")
#         except:
#             return render_template("./errores/error.html", error="No se encuentra ningún cliente abonado con esos datos")
#             #print("\nNo se encuentra ningún cliente abonado con esos datos")
#     else:
#         return render_template("./abonado/abonado_ver_datos.html")
#
#
# @app.route('/abonado/datos-personales/editar/', methods=["get", "post"])
# def modificar_datos_abono():
#     if request.method == 'POST':
#         try:
#             dni = request.form.get("dni")
#             pin = int(request.form.get("pin"))
#             nombre = request.form.get("nombre")
#             apellidos = request.form.get("apellidos")
#             num_tarjeta = request.form.get("num_tarjeta")
#             email = request.form.get("email")
#
#
#             if(admin_servicio.modificar_datos_abono(dni, pin, nombre, apellidos, num_tarjeta, email)):
#                 #print("\nLos datos se han modificado correctamente")
#                 cliente = abonado_servicio.obtener_datos_personales(dni, pin)
#                 # print(f"Nombre: {cliente.nombre}\nApellidos: {cliente.apellidos}\nEmail: {cliente.email}"
#                 #       f"\nDNI: {cliente.dni}")
#                 return render_template("./abonado/datos.html", dni=dni, pin=pin, cliente=cliente,
#                                        mensaje="Los datos se han modificado correctamente")
#         except AbonoNoEncontrado:
#             return render_template("./errores/error.html", error="No existe ningún abono con esos datos")
#             #print("\nNo existe ningún abono con esos datos")
#         except DatosErroneos:
#             return render_template("./errores/error.html", error="No se han podido modificar los datos")
#             #print("\nNo se han podido modificar los datos")
#     else:
#         return render_template("./abonado/abonado_modificar_datos.html")
#
#
# @app.route('/abonado/abono/renovar/', methods=["get", "post"])
# def renovar_abono():
#     if request.method == 'POST':
#         try:
#             dni = request.form.get("dni")
#             pin = int(request.form.get("pin"))
#             tipo_abono = request.form.get("tipo_abono")
#
#             if(admin_servicio.renovacion_abono(dni, pin, tipo_abono)):
#                 #print("\nSu abono se ha renovado correctamente")
#                 abono = parking_controller.imprimir_abono_dni(dni, pin)
#                 return render_template("./abonado/abono.html", dni=dni, pin=pin, tipo_abono=tipo_abono, abono=abono,
#                                        mensaje="Su abono se ha renovado correctamente")
#
#         except:
#             return render_template("./errores/error.html", error="No existe ningún abono con esos datos")
#             #print("\nNo existe ningún abono con esos datos")
#         # except:
#         #     return render_template("./errores/error.html", error="No se han podido modificar los datos")
#             #print("\nNo se han podido modificar los datos")
#     else:
#         return render_template("./abonado/abonado_renovar_abono.html")
#
#
# @app.route('/abonado/abono/borrar/', methods=["get", "post"])
# def borrar_abono():
#     if request.method == 'POST':
#         try:
#             dni = request.form.get("dni")
#             pin = int(request.form.get("pin"))
#
#             if(admin_servicio.borrar_abono(dni, pin)):
#                 #print("\nEl abono se ha borrado correctamente")
#                 return render_template("./abonado/confirmacion.html", dni=dni, pin=pin,
#                                        mensaje="El abono se ha borrado correctamente")
#         except:
#             return render_template("./errores/error.html", error="No existe ningún abono con esos datos")
#             #print("\nNo existe ningún abono con esos datos")
#     else:
#         return render_template("./abonado/abonado_borrar_abono.html")
#
#
# #Rutas adminstrador
#
# @app.route('/admin/')
# def admin_index():
#
#         return render_template("./administrador/admin_index.html")
#
#
# @app.route('/admin/estado_parking/')
# def estado_parking():
#
#     lista_plazas = parking_servicio.find_all().lista_plazas
#     return render_template("./administrador/estado_parking.html", lista_plazas=lista_plazas)
#
#
#
# @app.route('/admin/facturacion/', methods=["get", "post"])
# def facturacion():
#
#     if request.method == 'POST':
#         fecha1 = request.form.get("fecha1")
#         fecha2 = request.form.get("fecha2")
#
#         lista1 = fecha1.split(",")
#         lista2 = fecha2.split(",")
#         fecha1 = datetime(int(lista1[0]), int(lista1[1]), int(lista1[2]), int(lista1[3]), int(lista1[4]))
#         fecha2 = datetime(int(lista2[0]), int(lista2[1]), int(lista2[2]), int(lista2[3]), int(lista2[4]))
#         fac = admin_servicio.facturacion(fecha1, fecha2)
#         # print(f"\nFacturación entre {fecha1.day}/{fecha1.month}/{fecha1.year} {fecha1.hour}:{fecha1.minute}h "
#         #       f"y el {fecha2.day}/{fecha2.month}/{fecha2.year} {fecha2.hour}:{fecha2.minute}h "
#         #       f"--> {admin_servicio.facturacion(fecha1, fecha2)} €")
#
#         return render_template("./administrador/facturacion.html", fecha1=fecha1, fecha2=fecha2, fac=fac)
#     else:
#        return render_template("./administrador/ver_facturacion.html")
#
#
# @app.route('/admin/abonados/')
# def consulta_abonados():
#         index = 1
#         if(len(abono_servicio.find_all()) > 0):
#             abonos = abono_servicio.find_all()
#             total = admin_servicio.consulta_cobro_abonados()
#         #     for abono in abono_servicio.find_all():
#         #         print(f"\nAbono {i}\nTipo: {abono.tipo}\nId Plaza: {abono.cliente_abonado.id_plaza}\n"
#         #               f"Fecha Activacion: {abono.fecha_activacion.day}/{abono.fecha_activacion.month}/{abono.fecha_activacion.year}\n"
#         #               f"Fecha Caducidad: {abono.fecha_cancelacion.day}/{abono.fecha_cancelacion.month}/{abono.fecha_cancelacion.year}\n"
#         #               f"Precio: {abono.precio} €")
#         #         i+=1
#         # print(f"\nTotal facturado con los abonos: {admin_servicio.consulta_cobro_abonados()} €")
#         return render_template("./administrador/abonados.html", abonos=abonos, total=total, index=index)
#
#
#
# @app.route('/admin/caducidad_mes/', methods=["get", "post"])
# def caducidad_abonos_mes():
#     if request.method == 'POST':
#         try:
#             mes = int(request.form.get("mes"))
#             abonos = admin_servicio.caducidad_abonos_mes(mes)
#             cant = len(abonos)
#
#             mes_letra = parking_controller.imprimir_mes(mes)
#             return render_template("./administrador/abonos_caducidad.html", abonos=abonos, mes=mes, mes_letra=mes_letra,
#                                    cant=cant)
#
#         except:
#             return render_template("./errores/error.html", error="Ese mes no existe")
#         #if(len(abonos) > 0):
#             # i = 1
#             # for abono in abonos:
#             #     print(f"\nAbono {i}\nTipo: {abono.tipo}\nId Plaza: {abono.cliente_abonado.id_plaza}\n"
#             #           f"Fecha Activacion: {abono.fecha_activacion.day}/{abono.fecha_activacion.month}/{abono.fecha_activacion.year}\n"
#             #           f"Fecha Caducidad: {abono.fecha_cancelacion.day}/{abono.fecha_cancelacion.month}/{abono.fecha_cancelacion.year}\n"
#             #           f"Precio: {abono.precio} €")
#             #     i += 1
#
#         # else:
#         #     return render_template("./administrador/abonados.html", abonos=abonos, total=total, index=index)
#         #     print("\nNo hay abonos que caduquen en el mes indicado")
#     else:
#         return render_template("./administrador/caducidad_mes.html")
#
# @app.route('/admin/caducidad-10-dias/')
# def caducidad_abonos_proximos_10_dias():
#         abonos = admin_servicio.caducidad_abonos_10_dias()
#         cant = len(abonos)
#         # if(len(abonos) > 0):
#         #     i = 1
#         #     for abono in abonos:
#         #         print(f"\nAbono {i}\nTipo: {abono.tipo}\nId Plaza: {abono.cliente_abonado.id_plaza}\n"
#         #               f"Fecha Activacion: {abono.fecha_activacion.day}/{abono.fecha_activacion.month}/{abono.fecha_activacion.year}\n"
#         #               f"Fecha Caducidad: {abono.fecha_cancelacion.day}/{abono.fecha_cancelacion.month}/{abono.fecha_cancelacion.year}\n"
#         #               f"Precio: {abono.precio} €")
#         #         i += 1
#         #
#         # else:
#         #     print("\nNo hay abonos que caduquen en los próximos 10 días")
#         return render_template("./administrador/caducidad_10_dias.html", abonos=abonos, cant=cant)
