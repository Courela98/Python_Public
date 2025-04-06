import math

n=int(input("Digite um numero para calcular o fatorial: "))

def fatorialnumber(num):
    """
    Função para calcular o fatorial.
    """
    fatorial = math.factorial(num)
    return fatorial

print(f"A soma fatorial do numero {n} é {fatorialnumber(n)}")