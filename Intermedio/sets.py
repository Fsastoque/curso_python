#Conjuntos
set_countries = {'col', 'mex', 'bol'}
print(set_countries)
print(type(set_countries))

#Elimina el dato repetido
set_countries = {'col', 'mex', 'col','bol'}
print(set_countries)

set_countries = {4, 2, 2,5,7}
print(set_countries)

set_types = {1, 'hola', 12, 12}
print(set_types)

#set a partir de un string
set_from_string = set('hola')
print(set_from_string)

#set a partir de una tupla
set_from_tuple = set(('abc','cfr','oiu','abc'))
print(set_from_tuple)

#set a partir de una lista
numbers = [1,2,4,5,9,7,5,6]
set_from_lista = set(numbers)
#Retornando de nuevo una lista
print(list(set_from_lista))




