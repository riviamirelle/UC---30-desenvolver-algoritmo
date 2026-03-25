r = float(input("Digite o 1° número: "))
m = float(input("Digite o 2° número: "))

def soma(r, m):
    return r + m

def subtracao(r, m):
    return r - m

def multiplicacao(a, b):
    return r * m

def divisao(r, m):
    if m == 0:
        return "erro (divisão por zero)"
    return r / m

print("Soma:", soma(r, m))
print("Subtração:", subtracao(r, m))
print("Multiplicação:", multiplicacao(r, m))
print("Divisão:", divisao(r, m))