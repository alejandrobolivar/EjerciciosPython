
cadena = """978970686544 - Calculo diferencial e integral - James Stewart - 2007
978970686544 - Calculo diferencial e integral - James Stewart - 2007 
9702604486 - Introduccion al analisis de circuitos - Robert L. Boylestad - 2011 
9586001148 - Algebra y trigonometria - Dennis G. Zill, Jacqueline M. Dewar - 1992 
9786071507150 - Precalculo con avances de calculo - Dennis G. Zill, Jacqueline M. Dewar - 2012 
9789504926979 - Caballo de guerra - Michael Morpurgo - 2012 
958951250X - El testamento del paisa - Agustin Jaramillo Londoño - 2003 
9681643615 - La nueva mente del emperador - Roger Penrose - 2002"""

miDiccionario = {}

for line in cadena.splitlines():

    valores = line.split(" - ", 1)

    miDiccionario[valores[0].strip()] = valores[1].strip()
import operator 

valores_ord = dict(sorted(miDiccionario.items(), key=operator.itemgetter(1)))

for k, v in valores_ord.items():
    
    print("Clave:", k, "Valor:", v)