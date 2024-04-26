#HOF una función dentro de otra función 

def increment(x):
    return x +1

def high_ord_func(x, func): #Recibe como paramettro la función
    return x + func(x)

result = high_ord_func(2, increment)

print(result)

#Utilizando Lambdas
increment_v2 =lambda x : x + 1
high_ord_func_v2 = lambda x , func : x + func(x)
result_v2 =   high_ord_func_v2(2, increment_v2) 
print(result_v2)
result_v2 =   high_ord_func_v2(2, lambda x : x + 2)
print(result_v2)
result_v2 =   high_ord_func_v2(2, lambda x : x * 5)
print(result_v2)