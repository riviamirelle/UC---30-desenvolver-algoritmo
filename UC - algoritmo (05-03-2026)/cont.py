dados = [10, 20, 30, 60, 30]
print (dados)

# número de elementos -> o 'len' ele vai contar a quantidade de numeros na "variavel"
print("Comprimento: ", len(dados))

# conta ocorrências -> conta a quantidades de vezes que determinado num. se repete
print("Quantas vezes o 30 aparece: ", dados.count(30))

# index - encontrar posição -> em qual 'ordem' ele está
print("Indice de 20: ", dados.index(30))

#in verificar a existência -> se o dado estiver na "variavel", aparece 'TRUE', se caso não, aparece 'FALSE', quando faz a leitura
print("20 está na lista? ", 20 in dados)
print("100 está na lista? ", 100 in dados)

