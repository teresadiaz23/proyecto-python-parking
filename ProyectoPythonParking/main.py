from models.cliente_abonado import ClienteAbonado
from datetime import datetime, date, timedelta
from random import randint
from math import floor

cliente = ClienteAbonado("1234", "Teresa", "Diaz", "123456", "teresa@email.com", None)

print(cliente.nombre)

fecha1 = datetime(2020, 12, 10, 18, 0, 0)
fecha = date(2020,12,12)
print(fecha + timedelta(days=30))
fecha2 = datetime.now()
tiempo = fecha2 -fecha1

print(floor(tiempo.total_seconds()/60))

#print(hoy.day, hoy.month, hoy.year)

alea = randint(111111, 999999)
print(alea)
