"""
Crie uma função que receba dois números como parâmetros e retorne a soma deles.
"""

n1 = int(input("Digite o numero 1: "))
n2 = int(input("Digite o numero 2: "))

def soma(numero1, numero2):
    """
    Função somar de 2 numeros e retorna o valor da soma | Pede 2 numeros ao utilizador
    """
    return numero1 + numero2
print(f"A soma é {soma(n1, n2)}")

