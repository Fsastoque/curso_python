#Tuplas
numbers = (1,2,3,4,5)
strings = ("fabian" , "leidy", "carlos", "fabian")
print("numbers", numbers)
print(type(numbers))

print("strings", strings)
print(type(strings))

print(numbers[0])
print(numbers[-1])

print("Index",strings.index('leidy'))
print("count", strings.count('fabian'))

#Convertir a lista la tupla
lists = list(strings)
print(lists)
print(type(lists))

lists[0] = 'alex'
print(lists)

#Convertir a tupla la lista
my_tuple = tuple(lists)
print(my_tuple)
print(type(my_tuple))
