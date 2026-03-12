# Gere uma função que mostre a soma e o produto de dois números. 
numero1 = float(input("Digite o 1º numero: "))
numero2 = float(input("Digite o 2º numero: "))

def calcularNumeros (numero1, numero2):
    soma = (numero1 + numero2)
    multiplicacao = (numero1 * numero2)
    return soma, multiplicacao

resultado = calcularNumeros(numero1, numero2)
print(f"O resultado é {resultado}")