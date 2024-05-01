import random

'''dict ={}
for i in range(5):
    dict[i] = i * 2

print(dict)

#Comprehension
#par clave - valor
dict_v2 = {i :i * 2 for i in range(5)}
print(dict_v2)'''

'''countries = ['col', 'mex', 'bol', 'pe']
population = {}

for country in countries:
    population[country] = random.randint(1,100)

print(population)

#Comprehension
population_v2 = {country : random.randint(1,100) for country in countries}
print(population_v2)'''

#Condiciones
names = ['leidy','fabian', 'alex']
ages = ['30','40','45']

#Unir listas
print(list(zip(names,ages)))

new_dict ={name : age for (name,age) in list(zip(names,ages))}

print("dict", new_dict)
