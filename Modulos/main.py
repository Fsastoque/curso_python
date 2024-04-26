import utils

data = [
        {
            'Country' : 'Colombia',
            'Population' : 400
        },
        {
            'Country' : 'Bolivia',
            'Population' : 300
        }

    ]

def run():
    keys, values = utils.get_population()

    print(keys, values)   

    country = input("Digite el pais => ")
    result = utils.get_population_by_country(data, country)
    print(result)

if __name__ == '__main__':# si es ejecutado desde la terminal como un script ingresa al if
    run()