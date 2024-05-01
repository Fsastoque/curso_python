print(7 > 3)
print(7 < 3)
print(7 > 7)
print(2 >= 3)
print(2 >= 2)
print(5 == 5)
print(6 != 10)

#Flotantes

x =3.3
print(x)

y = 1.1 + 2.2
print(y)

print(x == y)

#Comparación flotantes

#Obtener solso 2 decimales con formart
y_str = format(y, ".2g")
print(y_str)

print(str(x) == y_str)

#Forma matematica

print('*' * 10)#Crear una linea divisoria

#Asignar una tolerancia para lso decimales

tolerance = 0.00001

#Se convierte en valor absoluto para no tener valores negativos
print(abs(x-y))
print(abs(x-y) < tolerance)
