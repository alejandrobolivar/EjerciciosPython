# Propósito: Determinar la diferencia entre dos tiempos
# Autor:     Alejandro Bolívar
# Fecha:     25/02/2021

# Escribir una aplicacion en Python que tenga como entrada
# la hora y los minutos en que se comenzo a realizar una
# llamada telefonica y la hora y los minutos em que termino
# la llamada. Determine el tiempo en que dro la llamad en horas
# y minutos asi como el costo de la misma, sabiendo que un minuto
# tiene un costo de 1,25 Bs.

# Entrada de datos
hi = int( input("Hora de inicio de la llamada: "))
mi = int(input("Minutos de inicio de la llamada: "))

hs = int(input("Hora en que termino la llamada: "))
ms = int(input("Minutos en que termino la llamada: "))

# Procesar datos
tmi = hi * 60 + mi  # Llevamos a minutos el tiempo de inicio
tms = hs * 60 + ms  # Llevamos a minutos el tiempo de termino
dur = tms -  tmi    # Calculamos la  duracion de la llamada en min.
hd = dur // 60      # Calulamos la duracion en horas
md = dur % 60       # Calulamos minutos de duracion
costo = dur * 1.25  # Calculamos el costo de la llamada.

# Salida de los resultados
print("la llamada duro: " + str(hd) + " horas y " + str(md) + " minutos")
print("Cuyo costo fue de: " + str(costo) + " Bs.")

# Fin del programa
input("Pulse una tecla para finalizar...") #'Pausa