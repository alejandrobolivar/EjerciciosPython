#Primero, pedimos el numero.
numero = int(input("Ingrese numero: "))

#Luego invertimos el numero. Se puede hacer mediante manejo de strings, pero aca lo haremos de modo matematico.
#Obtenemos el primer digito
digito_1 = numero // 100

#Luego, obtenemos el segundo digito
numero = numero % 100
digito_2 = numero // 10

#Y finalmente, obtenemos el tercer digito
digito_3 = numero % 10

#Ahora, hace falta invertir el numero y mostrarlo en pantalla
numero_inv = digito_3 * 100 + digito_2 * 10 + digito_1

# Salida de datos
print(numero_inv)

# Fin del programa
input("Pulse una tecla para finalizar...") #'Pausa