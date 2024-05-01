import matplotlib.pyplot as plt


def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [200, 500, 100]

    #Generar grafica
    #Obtener Figura y coordenadas
    fig, ax = plt.subplots()
    #Generar pie chart
    ax.pie(values, labels=labels)

    plt.savefig('pie.png')
    plt.close()
