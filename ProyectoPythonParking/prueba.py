from datetime import datetime, date, timedelta

fecha1 = input("Fecha1: ")
lista = fecha1.split(",")
print(lista)
print(datetime(int(lista[0]), int(lista[1]), int(lista[2])))
