def calcularSalario (valorHora, horasTrabalhadas): 
    salario = valorHora * horasTrabalhadas
    return salario 

valor = float(input("Qual o valor por horas do seu salário? "))
hora = float(input("Quantas horas foram trabalhadas? "))

resultado = calcularSalario (valor, hora)

print(f"O valor do seu salário total é: {resultado}")