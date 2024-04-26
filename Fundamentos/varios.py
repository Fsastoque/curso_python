'''print('Hola', end=' ') #Retira salto de linea
print('Mundo')

print('gatos', 'perros', 'ratones', sep=',')#Separador con ","

def a():
    print('a() comienza')
    b()
    d()
    print('a() regresa')

def b():
    print('b() comienza')
    c()
    print ('b() devuelve')

def c():
    print('c() inicia')
    print('c() devuelve')

def d():
    print('d() inicia')
    print('d () devuelve')

a()'''

#Variables globlales
def spam():
  global eggs
  eggs = 'spam'

eggs = 'global'
spam()
print(eggs)

#Explicación variables globales
def spam():
    global eggs
    eggs = 'spam' # this is the global

def bacon():
   eggs = 'bacon' # this is a local

def ham():
   print(eggs) # this is the global

eggs = 42 # this is the global
spam()
print(eggs)
'''
def spam():
     print(eggs) # ERROR!
     eggs = 'spam local'

eggs = 'global'
spam()'''

#Decorador
def mi_decorador(funcion):
    def wrapper():
        print("Antes de llamar a la función")
        funcion()
        print("Después de llamar a la función")
    return wrapper

@mi_decorador
def mi_funcion():
    print("¡Hola, mundo!")

mi_funcion()


import time, sys
indent = 0 # How many spaces to indent.
indentIncreasing = True # Whether the indentation is increasing or not.

try:
    while True: # The main program loop.
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # Pause for 1/10 of a second.

        if indentIncreasing:
            # Increase the number of spaces:
            indent = indent + 1
            if indent == 20:
                # Change direction:
                indentIncreasing = False

        else:
            # Decrease the number of spaces:
            indent = indent - 1
            if indent == 0:
                # Change direction:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()

