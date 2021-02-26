# Propósito: Determinar la parte decimal de un número
# Autor:     Alejandro Bolívar
# Fecha:     25/02/2021

# Primero, pedimos el numero
num = float(input("Ingrese un numero: "))

#Calculamos la parte entera, y se la restamos al numero.
num_entero = int(num)
num_decimal = abs(num) - abs(num_entero)

print(num_decimal)

# Fin del programa
input("Pulse una tecla para finalizar...") #'Pausa