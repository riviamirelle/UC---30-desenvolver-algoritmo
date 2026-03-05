import random

numeros = [45, 12, 78, 56]
print("Lista original: ", numeros)

# sort -> crescente 
numeros.sort()
print("Após sort(): ", numeros)

# sort -> decrescente 
numeros.sort(reverse=True)
print("Após sort(): ", numeros)

#embaralhar
random.shuffle(numeros)
print("Lista embaralhada", numeros)

