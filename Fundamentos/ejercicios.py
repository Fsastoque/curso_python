'''Para resolver este desafío, tu reto es utilizar la función map de Python y una función lambda para 
transformar una lista de números. Debes retornar una lista en la que cada número de la lista original sea multiplicado por dos.

La función multiply_numbers recibirá como entrada una lista con números. Finalmente, la función retornará la lista transformada.

Ejemplo 1:

Input: [2, 4, 5, 6, 8]
Output: [4, 8, 10, 12, 16]

Ejemplo 2:

Input: [1, 1, -2, -3]
Output: [2, 2, -4, -6]'''

print("map")
def multiply_numbers(numbers):
    # Escribe tu solución 👇
    result = list(map(lambda number : number * 2 , numbers))
    return result

numbers = [1, 1, -2, -3]
response = multiply_numbers(numbers)
print(response)

print("#" * 40)
print("filter")

'''Para resolver este desafío, tu reto es usar la función filter de Python y una función lambda para 
filtrar una lista de palabras, retornando una lista solo con las que cumplan con la condición de tener 4 o más letras.
La función filter_by_length recibirá como entrada una lista con palabras. Finalmente, la función retornará la lista filtrada.

Ejemplo 1:

Input: ['amor', 'sol', 'piedra', 'día']
Output: [ 'amor', 'piedra' ]

Ejemplo 2:

Input: ['rosa', 'gol', 'pez', 'día', 'gafas']
Output: [ 'rosa', 'gafas' ]'''

def filter_by_length(words):
   # Escribe tu solución 👇
   result = list(filter(lambda word : len(word) >= 4 , words))
   return result

words = ['amor', 'sol', 'piedra', 'día']
response = filter_by_length(words)
print(response)