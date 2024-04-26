import sys
import re
import time
import collections

#Manejo de datos de archivo
print(sys.path)

#Maneo de expresiones regulares
text = "Mi numero de telefono 311 456 98 65, el codigo del pais es 57, el numero de la suerte 3"
result = re.findall('[0-9]+', text) #Busca los que tengan coincidencia con numeros
print(result)

#Manejo de fechas
timestamp = time.time()
local = time.localtime()
result = time.asctime(local)
print(timestamp)
print(result)

#Manejo de listas
numbers = [1,1,2,2,2,3,3,4,5,6]
#Hallar la frecuencia de un numero
counter = collections.Counter(numbers)
print(counter)
