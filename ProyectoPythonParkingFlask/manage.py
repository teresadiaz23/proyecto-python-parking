from datetime import datetime

from dateutil.relativedelta import relativedelta
from flask_script import Manager
from aplicacion.app import app,db
from aplicacion.models.abono import Abono
from aplicacion.models.cliente_abonado import ClienteAbonado
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

    clientes=[
        {"dni":"1234","nombre": "Luismi","apellidos": "López", "num_tarjeta":"123456", "email":"luismi@email.com"},
        {"dni":"12345678B","nombre": "Pepe","apellidos": "García", "num_tarjeta":"567897", "email":"pepe@email.com"}

    ]
    for cli in clientes:
        cliente = ClienteAbonado(**cli)
        db.session.add(cliente)
        db.session.commit()

    abonos=[
        {"pin":111, "tipo":"mensual", "fecha_activacion":datetime.now(),
         "fecha_cancelacion":datetime.now() + relativedelta(months=1), "precio":25, "ClienteId":1},
        {"pin":222, "tipo":"trimestral", "fecha_activacion":datetime.now(),
         "fecha_cancelacion":datetime.now() + relativedelta(months=3), "precio":70, "ClienteId":2}
    ]

    for ab in abonos:
        abono = Abono(**ab)
        db.session.add(abono)
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
