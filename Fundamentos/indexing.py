#Indexing
print("Indexing")
text = "Ella sabe Python"
print(text[0])
print(text[1])
size = len(text)
print("Ultimo caracter", text[size-1])
print("Ultimo caracter", text[-1])#Muestra el utimo caracter

print("*" * 10)
print("slicing")
print(text[0:5])
print(text[:10])
print(text[5:])

#Saltos
print(text[10:16:1])
print(text[10:16:2])
print(text[::2])
