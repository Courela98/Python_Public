import numpy

totalnumeros = int(input("Digite o total de numeros que pretende realizar a média: "))
listaNumeros = []

def calcular_media(totalnumeros):
    """
    Função para calcular a média, de um total de numeros inseridos pelo utilizador
    """
    for i in range(totalnumeros):
        numero = int(input(f"Digite o numero {i+1}: "))
        listaNumeros.append(numero)

    media = numpy.mean(listaNumeros)
    return media

print(f"A média é {calcular_media(totalnumeros)}")




