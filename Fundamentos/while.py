#while
'''
while True: # mientras la condicion se cumpla la intruccuon se ejecutara
     print("Se ejecuto")
'''
'''counter = 0

while counter < 10:
    counter += 1
    print(counter)'''

'''counter = 0

while counter < 20:
    counter += 1
    if (counter == 15):
        break #Romper el ciclo
    print(counter)'''

counter = 0

while counter < 20:
    counter += 1
    if (counter < 15):
        continue #Conitnua con la siguinete iteracion no tiene encuenta lo que esta debajo del conitnue
    print(counter)