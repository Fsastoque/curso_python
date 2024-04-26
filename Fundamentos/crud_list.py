#CRUD Create, Read, Update & Delete


#Create
numbers = [1,2,3,4,5]


#Read
print(numbers[1])


#Update
numbers[-1] = 10
print(numbers)


#Add al final
numbers.append(700)
print(numbers)


#Add inicio
numbers.insert(0,'hola') #parámetros(posicion, elemento)
print(numbers)


numbers.insert(3,'change')
print(numbers)


#Fusionar listas
tasks = ['todo1', 'todo2', 'todo3']
new_list = numbers + tasks
print(new_list)


#Obtener la posición de un elemento
print("Index", new_list.index('todo2'))
index = new_list.index('todo2')


#Update
new_list[index]= 'todo changed'
print(new_list)


#Delete
new_list.remove('todo1')
print(new_list)


#Eliminar ultimo elemento
new_list.pop()
print(new_list)


new_list.pop(0)#Parametro posicion
print(new_list)


#Invertir lista
new_list.reverse()
print(new_list)


#Ordenar listas
numbers_a= [1,4,2,6,3,5]
numbers_a.sort()
print(numbers_a)


strings = ['re', 'ab', 'ed']
strings.sort()
print(strings)
