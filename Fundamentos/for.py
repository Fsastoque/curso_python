'''for element  in range(10):
    print(element)'''

'''my_list =[23,45,67,89,43]
for element in my_list: # Se itera uno por uno
    print(element)'''

'''my_tuple =('fabian', 'juli', 'leidy')
for element in my_tuple: # Se itera uno por uno
    print(element)'''

my_dict ={'name' : 'camisa',
          'precio' : 500,
          'stock' : 200}
'''
for key in my_dict: # Se itera uno por uno
    print(key,'=>', my_dict[key])'''

for key, value in my_dict.items(): # Se itera uno por uno
     print(key,'=>', value)

people =[{ 
            'name' : 'Fabian',
            'age' : 35       
        },
        {
            'name' : 'Leidy',
            'age' : 30
        },
        {
           'name' : 'Juli',
           'age' : 18
        }
       ]

for person in people:
     print(person)
     print('name =>' , person['name'])