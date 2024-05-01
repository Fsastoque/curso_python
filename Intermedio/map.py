#Funcion Map

numbers = [1 ,2, 3,4]
numbers_v2 =[]

for x in numbers:
    numbers_v2.append(x * 2)

print("numbers", numbers)
print("numbers_v2", numbers_v2)

numbers_v3 = map(lambda x: x * 2, numbers)#numbers es la lista que quiero transformar
print("numbers_v3",list(numbers_v3))

numbers_1 = [1 ,2, 3, 4]
numbers_2 = [5, 6, 7]

print("numbers_1", numbers_1)
print("numbers_2", numbers_2)
result = list(map(lambda x , y : x + y, numbers_1, numbers_2))

print("numbers3", result)