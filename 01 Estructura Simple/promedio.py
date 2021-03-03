# Propósito: Determinar el promedio de tres valores
# Autor:     Alejandro Bolívar
# Fecha:     25/02/2021

#Primero, pedimos los 3 valores
nota_1 = int(input("Primer valor: "))
nota_2 = int(input("Segundo valor: "))
nota_3 = int(input("Tercer valor: "))

#Calculamos el promedio y lo mostramos en pantalla. Nota el decimal en el 4.0, de esa forma la division entregara numeros decimales.
promedio = (nota_1 + nota_2 + nota_3) / 3.0

# Salida de los resultados
print ("El promedio es: " + str(promedio))

# Fin del programa
input("Pulse una tecla para finalizar...") #'Pausa