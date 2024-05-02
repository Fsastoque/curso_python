import matplotlib.pyplot as plt
import re

def get_population_by_continent(data, continent):
    result = list(filter(lambda item : item['Continent'] == continent, data))    
    return result

def get_population_percentage(data): 
    result = {item['Country/Territory'] : float(item['World Population Percentage']) for item in data}   
    return result.keys(), result.values()

def generate_pie_chart(labels, values):      
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.show()