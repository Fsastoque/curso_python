#Lambda

def increment(x):
    return x +1

#Lambda funcion
increment_v2 =lambda x: x + 1

result = increment(10)
print(result)

result_v2 = increment_v2(50)
print(result_v2)

full_name = lambda name, last_name : f'Full name is {name.title()} {last_name.title()}'

text = full_name('fabian', 'sastoque')
print(text)
