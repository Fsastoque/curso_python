import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text) 
    print(type(r.text)) # validar que tipo de dato es
   
    categories = r.json() #Formarto json
    for category in categories:
        print(category['name'])
