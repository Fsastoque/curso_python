import matplotlib.pyplot as plt
import re

def get_population_by_country(data, country):
    result = list(filter(lambda item : item['Country/Territory'] == country, data))
    return result

def get_population_by_country_year(data):   
    keys =['2022 Population', '2020 Population', '2015 Population', '2010 Population', '2000 Population', '1990 Population', '1980 Population' , '1970 Population']   
    result = {key : int(data[0][key]) for (key) in keys  }  
    labels = list(map(lambda item : item[:4] , result.keys()))  
    return labels, result.values()

def generate_bar_chart(labels, values):      
    fig, ax = plt.subplots()
    ax.bar(labels, values)  
    plt.show()


#Solucion Curso
def get_population(country_dict):
  population_dict = {
    '2022': int(country_dict['2022 Population']),
    '2020': int(country_dict['2020 Population']),
    '2015': int(country_dict['2015 Population']),
    '2010': int(country_dict['2010 Population']),
    '2000': int(country_dict['2000 Population']),
    '1990': int(country_dict['1990 Population']),
    '1980': int(country_dict['1980 Population']),
    '1970': int(country_dict['1970 Population'])
  }
  labels = population_dict.keys()
  values = population_dict.values()
  return labels, values
