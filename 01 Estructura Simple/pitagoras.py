# Propósito: Determinar la hipotenusa de un triangulo rectangulo
# Autor:     Alejandro Bolívar
# Fecha:     25/02/2021

from math import sqrt

# Primero, pedimos los catetos
a = int(input("Ingrese cateto a[cm]: "))
b = int(input("Ingrese cateto b[cm]: "))

# Calculamos el cateto faltante, y mostramos en pantalla
c = sqrt(a ** 2 + b ** 2)

# Salida de los resultados
print("Hipotenusa: %.2f" % c, "[cm]")

# Fin del programa
input("Pulse una tecla para finalizar...") #'Pausa