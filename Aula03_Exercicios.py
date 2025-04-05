def lista_ordenada():
    """
        Esta função consiste pedir ao utilizar um total de digitos e verificar se estão ordenados, não tiverem ficam ordenados.
    """

try:
    numeros = int(input("Digite o total de numeros: "))
    listanumeros = []

    for numero in range(numeros):
        numeroescolhido = int(input(f"Digite o numero {numero + 1}: "))
        listanumeros.append(numeroescolhido)

    if listanumeros == sorted(listanumeros):
        print("Lista Ordenada:")
    else:
        print("Lista Não Ordenada: ")

        print("Vamos ordenar a lista !")
        listanumeros.sort()
        print(f"Lista ordenada {listanumeros}")

except ValueError: (
    print("Digito incorreto !!! "))
