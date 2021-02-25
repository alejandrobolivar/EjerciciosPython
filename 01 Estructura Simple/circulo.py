from math import pi
	
#Pedimos el radio del circulo
radio = int(input("Radio de la base [cm]: "))
	
#Luego calculamos el perimetro y area del circulo
perimetro = 2 * pi * radio
area = pi * radio ** 2
	
#Y finalmente los mostramos en pantalla
print ("Perimetro: %.2f" % perimetro,"[cm]")
print ("Area: %.2f" % area,"[cm²]")

# Fin del programa
input("Pulse una tecla para finalizar...") #'Pausa