items= [
    {
        'product' : 'camisa',
        'price' : 300
    },
    {
        'product' : 'pantalon',
        'price' : 500
    },
    {
        'product' : 'gorra',
        'price' : 100
    }
]

#Adicionar una nueva llave al objeto
def add_taxes(item):
    new_item = item.copy() #Se crea una copia de la lista principal
    new_item['taxes'] = item['price'] * .19 #modifica la refenetcia en memoria y modifica los dos diccionarios
    return new_item

new_items = list(map(add_taxes, items))
print('New list')
print(new_items)
print('Old list')
print(items)

