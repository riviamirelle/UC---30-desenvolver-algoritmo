# Gere uma função que mostre a soma e o produto de dois números. (COM DUAS FUNÇÔES)
numero1 = float(input("Digite o 1º numero: "))
numero2 = float(input("Digite o 2º numero: "))


def somaNumeros (numero1, numero2):
    soma = (numero1 + numero2)
    return soma

def multiplicarNumero(numero1,numero2):
    multiplicacao = (numero1 * numero2)
    return multiplicacao


resultado1 = somaNumeros (numero1, numero2)
resultado2 = multiplicarNumero(numero1,numero2)

print(f"A soma é: {resultado1}")
print(f"A multiplicação é: {resultado2}")
    