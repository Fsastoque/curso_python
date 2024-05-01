name = "Fabian"
last_name = "Sastoque"
print(name)
print(last_name)

#Concatenación
full_name = name + " " + last_name
print(full_name)


quote = "I'm Fabian"
print(quote)

quote2 = 'She said "Hello" '
print(quote2)

#Formato
#Dar un formato al texto

template = "Hola mi nombre es " + name + " y mi apellido es " + last_name
print("v1",template)

template = "Hola mi nombre es {} y mi apellido es {}".format(name, last_name)
print("v2",template)

template = f"Hola mi nombre es {name} y mi apellido es {last_name}"
print("v3",template)
