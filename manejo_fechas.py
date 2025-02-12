"""
    Fechas en Python
"""
from datetime import date, datetime, timedelta

# Today
fecha = datetime.today()
print(type(fecha), fecha)
print(fecha)

# Now
print("-" * 50)
print(datetime.now())

# Year
print("-" * 50)
fecha_2 = datetime.now()
print(fecha_2.year)

# Month
print("-" * 50)
print(fecha_2.month)

# Day
print("-" * 50)
print(fecha_2.day)

# Hour
print("-" * 50)
print(fecha_2.hour)

# Minute
print("-" * 50)
print(fecha_2.minute)

# Second
print("-" * 50)
print(fecha_2.second)

# Microsecond
print("-" * 50)
print(fecha_2.microsecond)

# UTC queda en deuda deprecado con el metodo utcnow()
print("-" * 50)
print("UTC: ", fecha_2.utcnow())

"""
    Weekday
    
    lunes = 0
    martes = 1
    miércoles = 2
    jueves = 3
    viernes = 4
    sábado = 5
    domingo = 6
"""
print("-" * 50)
print(fecha_2.weekday())
list_dias: list = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
print(list_dias[fecha_2.weekday()])

"""
    ISOWEEKDAY
    
    lunes = 1
    martes = 2
    miércoles = 3
    jueves = 4
    viernes = 5
    sábado = 6
    domingo = 7
"""
print("-" * 50)
print(fecha_2.isoweekday())

"""
    FORMATOS DE FECHA STRFTIME
    
    %a	Nombre local abreviado de día de semana
    %A	Nombre local completo de día de semana
    %b	Nombre local abreviado de mes
    %B	Nombre local completo de mes
    %c	Representación local de fecha y hora
    %d	Día de mes [01,31]
    %H	Hora (horario 24 horas) [00,23]
    %I	Hora (horario 12 horas) [01,12]
    %j	Número de día del año [001,366]
    %m	Mes [01,12]
    %M	Minuto [00,59]
    %S	Segundo
    %U	Nº semana del año. Se considera al Domingo como primer día de semana [00,53]
    %w	Establece el primer día de semana [0(Domingo),1(Lunes)... 6].
    %W	Nº semana del año (Se considera al Lunes como primer día de semana) [00,53]
    %x	Fecha local
    %X	Hora local
    %y	Año en formato corto [00,99]
    %Y	Año en formato largo
    %Z	Nombre de Zona Horaria
"""
# DD/MM/YYYY HH:MM:SS
# 11/02/2025 18:35:51
fecha_formateada = fecha_2.strftime("%d/%m/%Y %H:%M:%S")
print(fecha_formateada)
print(type(fecha_formateada))

# FORMATOS DE FECHA STRPTIME
str_a_date = datetime.strptime("11/02/2025 18:35:51", "%d/%m/%Y %H:%M:%S")
print(str_a_date)
print(type(str_a_date))
print(str_a_date.year)

# ISOCALENDAR
print(str_a_date.isocalendar())

# TIMEDELTA
print("-" * 50)
print(str_a_date)
print("incrementando días  +   ",str_a_date + timedelta(days=5))
print("incrementando días  -   ",str_a_date + timedelta(days=-5))
print("incrementando segundos  ",str_a_date + timedelta(seconds=18000))
print("incrementando microseg.  ",str_a_date + timedelta(microseconds=1000000))

# ZONA HORARIA TIMEZONE
print(str_a_date.astimezone().tzinfo)
