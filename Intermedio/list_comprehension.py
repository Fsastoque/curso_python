'''numbers = []

for element in range (1,11):
    numbers.append(element * 2)

print(numbers)

#list compehension
number_v2 = [element for element in range(1 ,11) ]
print(number_v2)

number_v2 = [element * 2 for element in range(1 ,11) ]
print(number_v2)
'''
#Condiciniones
numbers = []

for i in range (1,11):
    if(i % 2 == 0):
        numbers.append(i * 2)

print(numbers)

#list compehension
number_v2 = [i * 2 for i in range(1 ,11) if (i % 2 == 0)]
print(number_v2)