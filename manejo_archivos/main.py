import utils
import read_csv

def run():
    data= read_csv.read_csv('./manejo_archivos/data.csv')
    #print(data)
    country = input("Digite el pais => ")
    result = utils.get_population_by_country(data, country)
    if len(result) > 0:           
        labels, values = utils.get_population_by_country_year(result)  
        utils.generate_bar_chart(labels, values)

if __name__ == '__main__':
     run()