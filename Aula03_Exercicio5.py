temperatura = float(input("Celsius: "))

def celsius_fahrenheit(celsius):
    """
    Função para converter celsius e fahrenheit
    """
    fahre = celsius * 9 / 5 + 32
    return fahre

print(f"A temperatura em Celsius é {temperatura} e em Fahrenheit é {celsius_fahrenheit(temperatura)}")