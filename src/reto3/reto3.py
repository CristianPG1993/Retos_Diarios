from datetime import date, datetime  # Importamos las clases necesarias para trabajar con fechas

# Obtenemos la fecha actual (día, mes y año sin hora)
fecha_actual = date.today()

# Definimos manualmente la fecha de nacimiento (año, mes, día)
fecha_nacimiento = date(1993, 11, 4)

# Calculamos la diferencia total entre ambas fechas (tipo timedelta)
diferencia = fecha_actual - fecha_nacimiento

# Obtenemos los días totales transcurridos desde la fecha de nacimiento hasta hoy
dias_totales = diferencia.days

# Calculamos la edad en años de forma precisa
edad = fecha_actual.year - fecha_nacimiento.year

# Ajustamos la edad si todavía no ha llegado el cumpleaños en el año actual
if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
    edad -= 1

# Obtenemos el día de la semana en texto (ej. Monday)
dia_semana = fecha_nacimiento.strftime("%A")

# Obtenemos el nombre completo del mes de nacimiento (ej. November)
mes_nacimiento = fecha_nacimiento.strftime("%B")

# Obtenemos el año en formato completo como texto
year_nacimiento = fecha_nacimiento.strftime("%Y")

# Obtenemos el número de día dentro del año (1 al 365 o 366)
dia_year = fecha_nacimiento.strftime("%j")

# Mostramos todos los resultados al usuario
print(diferencia)  # timedelta total
print(f"Días totales: {dias_totales}")
print(f"Años totales: {edad}")
print(f"Día de la semana: {dia_semana}")
print(f"Mes de nacimiento: {mes_nacimiento}")
print(f"Año de nacimiento: {year_nacimiento}")
print(f"Número de día del año: {dia_year}")


