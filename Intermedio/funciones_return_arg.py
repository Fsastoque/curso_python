def find_volume(length=1, width=1, dpeth=1): #asigna valores por defecto
    return length* width * dpeth, width , "Hola" #Devuelver varios valores

result = find_volume(10,20,3)
print(result)

result = find_volume(width= 60) #se envia un valor en especifico
print(result)

result , width, text = find_volume(10,20,3) #Recibir los valores en cada variable
print(result)
print(width)
print(text)