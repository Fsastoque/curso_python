print("if")

'''
if True:
    print("Deberia ejecutarse")

pet = input("¿Cual es tu mascota favorita? ")

if pet == "perro":
    print("genial tienes buen gusto")

elif pet == "gato":
    print("Espero tengas suerte")

elif pet == "pez":
    print("Eres lo maximo")
else:
    print("no tienes ninguna mascota interesante")
'''

'''
stock = int(input("Ingrese el numero de stock => "))

if (stock >= 100 and stock <= 1000):
    print("El stock es correcto")
else:
    print("El stock es incorrecto")
'''

number = int(input("Ingresa un numero para saber si es par => "))

print(''' Respuesta: ''') # para hacer un print de varias lineas
print ("*" * 20)
if(number % 2 == 0):
    print(f"El numero {number} es par")
else:
    print(f"El numero {number} es impar")
