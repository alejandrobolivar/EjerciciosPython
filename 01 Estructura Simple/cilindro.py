# Determinar si el valor leido es par o impar
# Entrada del dato
radio = float(input("Radio de la base [cm]: "))
altura = float(input("Altura del cilindro [cm]: "))

# Procesamiento
area = 3.141516*radio*radio
volumen= (2*3.141516*radio)*altura

#salida de datos
print ("Area del Cilindro= %.2f" % area,"[cm²]")
print ("Volumen del Cilindro= %.2f" % volumen,"[cm³]")

input("Pulse una tecla para finalizar...") #'Pausa
