"""
Escreva uma função que verifique se um número é par ou ímpar.
"""
numero = int(input("Digite um numero: "))

def par (n):
    """
    Funçao que verifica se é par ou impar
    """
    if n % 2 == 0:
        n = "numero Par"
    else:
        n = "numero Impar"
    return n

print(f"É {par(numero)}")



