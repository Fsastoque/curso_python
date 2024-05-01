#print(0 /0 )
#print(b)

suma = lambda x, y : x + y
assert suma(2 , 2) == 4
# assert hace una verificación y manda un AssertionError cuando no se cumple el “statement”

print("hola")

age = 10

if age < 18:
    raise Exception("No se permite menores de edad")

#raise Exception() levanta un error creado por nosotros mismo