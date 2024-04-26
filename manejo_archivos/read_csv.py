import csv

def read_csv(path):
    #Función para abrir el archivo
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile,delimiter=',')#Reader es un iterable
        
        #Nombre de las columnas se encuentra en la primera fila
        header = next(reader)
        data = []
        #print(next(header))
        for row in reader:
            iterable =zip(header, row) #Unir las dos listas HEADER y FILAS en un array de tuplas
            #print("***" * 5)
            #print(list(iterable))        
            country_dict = {key : value for key, value in iterable}#dict_comprehension            
            data.append(country_dict)
        
        return data
            
#Ejecutar archivo como script desde la terminal
if __name__ == '__main__':
    data= read_csv('./manejo_archivos/data.csv')
    result = list(filter(lambda x : x['Country/Territory'] == 'Colombia', data))    
    print(result)
