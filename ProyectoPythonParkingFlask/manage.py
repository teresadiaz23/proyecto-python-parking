from datetime import datetime

from dateutil.relativedelta import relativedelta
from flask_script import Manager
from aplicacion.app import app,db
from aplicacion.models.abono import Abono
from aplicacion.models.cliente_abonado import ClienteAbonado
from aplicacion.models.parking import Parking
from aplicacion.models.plaza import Plaza
from aplicacion.models.ticket import Ticket
from aplicacion.models.vehiculo import Turismo, Motocicleta, MovilidadReducida
from aplicacion.repositories.cliente_abonado_repositorio import cliente_abonado_repositorio

manager = Manager(app)
app.config['DEBUG'] = True # Ensure debugger will load.

@manager.command
def create_tables():
    "Create relational database tables."
    db.create_all()

@manager.command
def drop_tables():
    "Drop all project relational database tables. THIS DELETES DATA."
    db.drop_all()

@manager.command
def add_data_tables():
    db.create_all()

    vehiculos=[
        Turismo(matricula="1234BBB", tarifa=0.12),
        Motocicleta(matricula="6543HHH", tarifa=0.08),
        MovilidadReducida(matricula="3846DDD", tarifa=0.10),
        Turismo(matricula="3876KKK",tarifa=0.12)
    ]

    for v in vehiculos:

        db.session.add(v)
        db.session.commit()

    parking = Parking(num_plazas=60,  dinero_tickets=0, dinero_abonos=0)
    db.session.add(parking)
    db.session.commit()

    plazas = []
    for p in range(60):
        if(p < 42):
            plazas.append(Plaza(tipo_vehiculo="turismo", tarifa=0.12, ParkingId=1))
        elif(p >= 42 and p < 51):
            plazas.append((Plaza(tipo_vehiculo="motocicleta", tarifa=0.08, ParkingId=1)))
        else:
            plazas.append(Plaza(tipo_vehiculo="movilidad reducida", tarifa=0.10, ParkingId=1))

    for plaza in plazas:

        db.session.add(plaza)
        db.session.commit()

    clientes=[
        {"dni":"1234","nombre": "Luismi","apellidos": "López", "num_tarjeta":"123456", "email":"luismi@email.com",
         "VehiculoId":1},
        {"dni":"12345678B","nombre": "Pepe","apellidos": "García", "num_tarjeta":"567897", "email":"pepe@email.com",
         "VehiculoId":2},
        {"dni":"12345678C","nombre": "María","apellidos": "Pérez", "num_tarjeta":"342565", "email":"maria@email.com",
         "VehiculoId":3},
        {"dni":"12345678D","nombre": "Miguel","apellidos": "Campos", "num_tarjeta":"287698", "email":"miguel@email.com",
         "VehiculoId":4}

    ]

    for cli in clientes:
        cliente = ClienteAbonado(**cli)
        db.session.add(cliente)
        db.session.commit()

    abonos=[
        {"pin":111, "tipo":"mensual", "fecha_activacion":datetime.now(),
         "fecha_cancelacion":datetime.now() + relativedelta(months=1), "precio":25, "ClienteId":1},
        {"pin":222, "tipo":"trimestral", "fecha_activacion":datetime.now(),
         "fecha_cancelacion":datetime.now() + relativedelta(months=3), "precio":70, "ClienteId":2},
        {"pin":333, "tipo":"semestral", "fecha_activacion":datetime.now(),
         "fecha_cancelacion":datetime.now() + relativedelta(months=6), "precio":130, "ClienteId":3},
        {"pin":444, "tipo":"anual", "fecha_activacion":datetime.now(),
         "fecha_cancelacion":datetime.now() + relativedelta(years=1), "precio":200, "ClienteId":4}
    ]

    for ab in abonos:
        abono = Abono(**ab)
        db.session.add(abono)
        db.session.commit()



    lista_tickets = [

        Ticket(matricula="1234BBB", fecha_deposito=datetime(2020, 12, 10, 15, 30), PlazaId=6, pin=111111,
               fecha_salida=datetime(2020, 12, 10, 17, 30), coste=5),
        Ticket(matricula="1234JJJ", fecha_deposito=datetime(2020, 12, 12, 15, 30), PlazaId=6, pin=111111,
               fecha_salida=datetime(2020, 12, 12, 17, 30), coste=5.50),
        Ticket(matricula="1234FFF", fecha_deposito=datetime(2020, 12, 14, 15, 30), PlazaId=6, pin=111111,
               fecha_salida=datetime(2020, 12, 14, 17, 30), coste=6)
    ]

    for ticket in lista_tickets:
        db.session.add(ticket)
        db.session.commit()

    tickets = Ticket.query.all()
    dinero_tickets = 0
    if(len(tickets) > 0):
        for ticket in tickets:
            dinero_tickets+=ticket.coste

    abonos = Abono.query.all()
    dinero_abonos = 0
    if(len(abonos) > 0):
        for abono in abonos:
            dinero_abonos+=abono.precio

    parking = Parking.query.get(1)
    parking.dinero_tickets = dinero_tickets
    parking.dinero_abonos = dinero_abonos


    db.session.add(parking)

    plaza1 = Plaza.query.get(3)
    plaza1.ClienteId = ClienteAbonado.query.get(1).id
    db.session.add(plaza1)
    plaza2 = Plaza.query.get(45)
    plaza2.ClienteId = ClienteAbonado.query.get(2).id
    db.session.add(plaza2)
    plaza3 = Plaza.query.get(52)
    plaza3.ClienteId = ClienteAbonado.query.get(3).id
    db.session.add(plaza3)
    plaza4 = Plaza.query.get(30)
    plaza4.ClienteId = ClienteAbonado.query.get(4).id
    db.session.add(plaza4)

    db.session.commit()

    # for cliente in cliente_abonado_repositorio.find_all():
    #     print(cliente)


    # abonos = [
    #     Abono(pin=111, tipo="mensual", fecha_activacion=datetime.now(), fecha_cancelacion=datetime.now() + relativedelta(months=1), precio=25),
    #     Abono(pin=222, tipo="trimestral", fecha_activacion=datetime.now(), fecha_cancelacion=datetime.now() + relativedelta(months=3), precio=70),
    #     Abono(pin=333, tipo="semestral", fecha_activacion=datetime.now(), fecha_cancelacion=datetime.now() + relativedelta(months=6), precio=130),
    #     Abono(pin=444, tipo="anual", fecha_activacion=datetime.now(), fecha_cancelacion=datetime.now() + relativedelta(years=1), precio=200)
    # ]
    #
    # for abono in abonos:
    #
    #     db.session.add(abono)
    #     db.session.commit()
    # abono1 = Abono(111, "mensual", datetime.now(), datetime.now() + relativedelta(months=1), 25)
    # abono2 = Abono(222, "trimestral", datetime.now(), datetime.now() + relativedelta(months=3), 70)
    # abono3 = Abono(333, "semestral", datetime.now(), datetime.now() + relativedelta(months=6), 130)
    # abono4 = Abono(444, "anual", datetime.now(), datetime.now() + relativedelta(years=1), 200)
    #
    # db.session.add_all([abono1,abono2,abono3,abono4])
    # db.session.commit()

    # cliente1 = ClienteAbonado("1234", "Luismi", "López", "123456", "luismi@email.com", "mensual", 3),
    # cliente2 =ClienteAbonado("12345678B", "Pepe", "García", "567897", "pepe@email.com", "trimestral", 45),
    # cliente3 =ClienteAbonado("12345678C", "María", "Pérez", "342565", "maria@email.com", "semestral", 52),
    # cliente4 =ClienteAbonado("12345678D", "Miguel", "Campos", "287698", "miguel@email.com", "anual", 30)
    #
    #
    # db.session.add_all([cliente1,cliente2,cliente3,cliente4])
    # db.session.commit()



if __name__ == '__main__':
	manager.run()
