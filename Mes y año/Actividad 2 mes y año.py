import datetime

año = 0
dia = 0
mes = 0

año = int(input("Ingrese su año en el que nacio: "))
dia = int(input("Ingrese el dìa en el que nacio: "))
mes = int(input("Ingrese el nùmero del mes en que nacio: "))

nacim = datetime.date(año,mes,dia)

fecha_actual = datetime.datetime.now()

hoy = datetime.date.today()

print(hoy-nacim)

