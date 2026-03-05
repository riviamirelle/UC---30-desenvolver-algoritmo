import random

numeros = [7, 14, 17, 22, 29, 34]
print("NUMEROS: FLU: ", numeros)

numeros.sort()
print("JOGADORES(): ", numeros)

numeros.sort(reverse=True)
print("JOGADORES DO FLU(): ", numeros)

random.shuffle(numeros)
print("Lista embaralhada", numeros) 