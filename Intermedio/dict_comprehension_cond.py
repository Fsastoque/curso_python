import random

countries = ['col', 'mex', 'bol', 'pe']

population_v1 = {country : random.randint(1,100) for country in countries}
print(population_v1)

population_v2 ={country : population  for (country,population) in population_v1.items() if(population > 20)}
print(population_v2)

text = "hola soy fabian"
print(text)
unique = {c: text.count(c) for c in text if(c in 'aeiou')}
print(unique)