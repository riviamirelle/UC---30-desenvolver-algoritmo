contato = {
    "@camila": "Camila",
    "@paola": "Paola",
    "@sheron": "Sheron",
    "@bruna": "Bruna",
}

# obter chave
print("Chaves: ")
for insta in contato.keys():
    print(insta)

# obter valores
print("\n Valores: ")
for nome in contato.value():
    print(nome)

# obter pares
print("\n Pares: ")
for insta, nome in contato.items():
    print(f"{insta} --> {nome}")


contato = {
    "@camila": 1.70,
    "@paola": 1.80,
    "@sheron": 1.55,
    "@bruna": 1.60,
}

print("Ordenando por chave: ")
for insta in sorted(contato.keys()):
    print(f"{insta} --> {contato[insta]: .2f}m")

from operador import itemgetter
print("\n Ordenado por valor (altura): ")
for insta, estatura in sorted(contato.items(), key = itemgetter(1)):
    print(f"{insta} --> {estatura: .2f}m")    