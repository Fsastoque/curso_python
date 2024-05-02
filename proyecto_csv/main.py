import utils
import read_csv

def run():
    data= read_csv.read_csv('./manejo_archivos/data.csv')
    continent = input("Digite el continente => ")
    result = utils.get_population_by_continent(data, continent) 
  
    if len(result) > 0:
        labels, values = utils.get_population_percentage(result)
        utils.generate_pie_chart(labels, values)    
        

if __name__ == '__main__':
     run()