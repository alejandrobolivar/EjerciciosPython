# Propósito: Determinar el área y el volumen de un cilindro
# Autor:     Alejandro Bolívar
# Fecha:     25/02/2021

# Entrada del dato
radio = float(input("Radio de la base [cm]: "))
altura = float(input("Altura del cilindro [cm]: "))

# Procesamiento
area = 3.141516 * radio * radio
volumen= (2 * 3.141516 * radio) * altura

# Salida de datos
print ("Area del Cilindro= %.2f" % area,"[cm²]")
print ("Volumen del Cilindro= %.2f" % volumen,"[cm³]")

# Fin del programa
input("Pulse una tecla para finalizar...") #'Pausa
