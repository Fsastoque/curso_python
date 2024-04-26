#Definir función
def sum_whit_range(min, max):
    print(min, max)
    sum = 0
    for resp in range(min, max):
        sum +=resp

    return sum

result = sum_whit_range(1,10)
print(result)
result_1 = sum_whit_range(result,result +10)
print(result_1)
sum_whit_range(1,100)

