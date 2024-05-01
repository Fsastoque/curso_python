import random

def choose_options():
    options = ('piedra' , 'papel', 'tijera')
    user_option = input("piedra, papel o tijera => ").lower()

    if not user_option in options:
        print("Opción no valida")
        #continue
        return None, None
    #else:
    #Escoje de forma aleatoria la opción
    computer_option = random.choice(options)
    
    print('User option => ', user_option)
    print('Computer option => ', computer_option)

    return user_option, computer_option
    
def check_rules(user_option, computer_option, user_wins, computer_wins):
        if(user_option == computer_option):
            print("Empate!")
        elif(user_option == "piedra"):
            if(computer_option == "tijera"):
                print("piedra gana a tijera")
                print("User gano!")
                user_wins += 1
            else:
                print("papel gana a piedra")
                print("Computer gano!")
                computer_wins += 1
        elif(user_option == "papel"):
            if(computer_option == "piedra"):
                print("papel gana a piedra")
                print("User gano!")
                user_wins += 1
            else:
                print("tijera gana a papel")
                print("Computer gano!")
                computer_wins += 1
        elif(user_option == "tijera"):
            if(computer_option == "papel"):
                print("tijera gana a papel")
                print("User gano!")
                user_wins += 1
            else:
                print("piedra gana a tijera")
                print("Computer gano!")
                computer_wins += 1
        return user_wins, computer_wins

def wins(user_wins,computer_wins):

    if computer_wins ==2:
            print('-' * 60)
            print('Puntaje Final Computer =>', computer_wins, '|', 'Puntaje Final User =>', user_wins)
            print('-' * 60)
            print("El ganador es el computer \o/")
            
            return True
           
    if user_wins ==2:
            print('-' * 60)
            print('Puntaje Final Computer =>', computer_wins, '|', 'Puntaje Final User =>', user_wins)
            print('-' * 60)
            print("El ganador es el user \o/")

            return True

def run_game():
    user_wins = 0
    computer_wins = 0
    rounds = 1

    while True:

        print('*' * 10)
        print('ROUND', rounds)
        print('*' * 10)
        
        print('-' * 40)
        print('Puntaje Computer =>', computer_wins, '|', 'Puntaje User =>', user_wins)
        print('-' * 40)

        user_option, computer_option = choose_options() 

        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins) 

        end = wins(user_wins, computer_wins)
        
        if end:
             break

        rounds += 1

run_game()