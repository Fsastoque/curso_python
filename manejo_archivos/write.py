with open('./manejo_archivos/text.txt', 'w+',encoding="UTF-8") as file: #'r+' habilita lectura y estcritura en el archivo y w+ sobre escribe el archivo
    for line in file:
        print(line)
    file.write("Nuevas cosas en este archivo\n") 
    file.write("Otra linea\n")
    file.write("Otra linea\n")
    file.write("Otra cosa\n")