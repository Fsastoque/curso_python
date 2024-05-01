#Diccionario

my_dict = {}
print(type(my_dict))

my_dict = {
    'avion' : 'transporte',
    'name' :'Fabian',
    'last_name' : 'Sastoque Cubides',
    'age' : 40
}

print(my_dict)

#Cunatos elementos contiene el diccionario
print(len(my_dict))

#Obtener datos
print(my_dict['age'])
print(my_dict['last_name'])
print("Metodo get", my_dict.get('age')) 
print("Metodo in avion in my_dict", 'avion' in my_dict)
print("Metodo in bus in my_dict", 'bus' in my_dict)

person = {
    'name' :'Fabian',
    'last_name' : 'Sastoque Cubides',
    'langs' : ['python', 'javascript'],
    'age' : 40
}

print(person)

#Update
person['name'] = 'Alfonso'
print(person)

person['age'] -= 15
print(person)

#Insert
person['langs'].append('c#')
print(person)

#Delete
del person['last_name']
print(person)

person. pop('age')
print(person)

#Obtener los items
print('Items')
print(person.items())

#Obtener los items
print('keys')
print(person.keys())

#Obtener los valores
print('values')
print(person.values())