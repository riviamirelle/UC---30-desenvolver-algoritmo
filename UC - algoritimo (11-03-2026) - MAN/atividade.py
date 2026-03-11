aluno = {}

aluno ["nome"] = input ("digite o nome do aluno: ")
aluno ["nota1"] = float(input("Digite a nota da prova 1: "))
aluno ["nota2"] = float(input("Digite a nota da prova 2: "))

media = aluno ["nota1"] + aluno ["nota2"] / 2

aluno ["media"] = media

if media >= 7: 
    situacao = "APROVADO"
elif media >= 5: 
    situacao = "RECUPERAÇÃO"
else: 
    situacao = "REPROVADO"

print("\n Dados do aluno: ")
for chave, valor in aluno.items(): 
   print(f"{chave}: {valor}")

print("Situação: ", situacao)

