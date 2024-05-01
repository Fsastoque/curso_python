#CRUD Conjuntos
set_countries = {'col', 'mex', 'bol'}
print(set_countries)
print(type(set_countries))

#Tamaño
size = len(set_countries)
print("size", size)

# Busqueda
print('col =>','col' in set_countries)
print('pe =>','pe' in set_countries)

#Adicionar

set_countries.add('pe')
print(set_countries)

#Update
set_countries.update({'ar','ecua','pe'})
print(set_countries)

#delete
set_countries.remove('col')
print(set_countries)

set_countries.remove('ar')
print(set_countries)

#Genera error ya que no existe en el conjunto
'''set_countries.remove('ar')
print(set_countries)'''

#Si no existe no genera error
set_countries.discard('ar')
print(set_countries)

#Limpiar completamente el conjunto
set_countries.clear()
print(set_countries)