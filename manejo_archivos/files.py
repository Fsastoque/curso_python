file = open('./manejo_archivos/text.txt')
#Leer archivo completo
#print(file.read())

#Leer linea por linea
'''print(file.readline())
print(file.readline())'''

'''for line in file:
    print(line)'''

#Cerrar archivo
#file.close()

#Metodo para cerrar automaticamente el archivo
with open('./manejo_archivos/text.txt', 'r',encoding="UTF-8") as file: #"r abre el archivo en modo lectura, y la codificación para caracteres especiales"
    for line in file:
        print(line)