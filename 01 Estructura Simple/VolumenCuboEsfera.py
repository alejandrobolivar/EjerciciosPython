# Propósito: Determinar el volumen diferencia entre un cubo y una esfera
# Autor:     Alejandro Bolívar
# Fecha:     25/02/2021

from math import pi
# Calculo del volumen vacio entre una Caja y una Esfera
# escribir una aplicacion en Python que determine el volumen vacio
# que hay entre una Caja y una Esfera la cual tendra como entrada
# la longitud de los lados de la Caja L, siendo el radio de la Esfera L/2

# Entrada de datos
L = int(input("Longitud del lado del cubo[cm]: "))

r = L / 2  # Calculamos el radio de la esfera
vcc = L * L * L  # Volumen del caja
print("Volumen de la caja= %.2f" % ves, "[cm³]")
ves = 4 / 3 *  pi * r ** 3  # volumen de la esfera
vv = vcc - ves  # volumen del vacío

# Salida de los resultados
print("Volumen de la esfera= %.2f" % ves, "[cm³]")
print(" el volumen vacio es= %.2f" % vv, "[cm³]")

# Fin del programa
input("Pulse una tecla para finalizar...") #'Pausa