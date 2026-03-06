notas = [7.5, 8.0, 9.5, 6,0, 8.5]
print("NOTAS: ", notas)

print("MENOR: ", min(notas))
print("MAIOR: ", max(notas))
print("SOMA: ", sum(notas))
print("MÉDIA: ", sum(notas) / len (notas))

nomes = ["Adriana", "Breno", "Carla", "Daniel"]

#apenas o elemento 
print ("Usando FOR simples: ")
for nome in nomes: 
    print(f"Olá, {nome}!")


#indice e elemento
print("\n Usando enumerate: ")
for indice, nome in enumerate(nomes):
    print(f"Posição {indice}: {nome}")


original = ["A", "B", "C"]
copia = list(original)

print("ORIGINAL: ", original)
print("CÓPIA: ", copia)
print("SÃO IGUAIS: ", original == copia)

copia.append("D")
print("ORIGINAL: ", original)
print("CÓPIA: ", copia)
print("SÃO IGUAIS: ", original == copia) 