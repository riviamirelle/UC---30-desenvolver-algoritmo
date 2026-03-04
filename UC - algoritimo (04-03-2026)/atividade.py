# Crie uma lista de COMPRAS com pelo menos 5 itens
# Adicione um novo item à lista de forma que o usuário digite

lista = ["Feijão", "Arroz", "Carne", "Refrigerante", "Batata Frita"]
print("ITENS",lista)

compras = input("Adicione produto: ")
lista.append(compras)
print(lista)