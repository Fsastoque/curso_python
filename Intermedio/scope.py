price = 100 #Variable global

#Contexto definido
def increment():
    price = 200 #Variable local
    result = price + 10 #Para Result el ambito solo pertenece a la función
    #print(price)
    return result

price_2 = increment()
print(price)
print(price_2)
