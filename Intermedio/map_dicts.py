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

#Transforma list a numeros
prices = list(map(lambda item : item['price'], items))
print(prices)

#Adicionar una nueva llave al objeto
def add_taxes(item):
    item['taxes'] = item['price'] * .19
    return item

new_items = list(map(add_taxes, items))
print(new_items)


tax = .19 
new_items = list(map(lambda item: {**item, **{'tax':item['price']*tax}}, items)) 
print(new_items)