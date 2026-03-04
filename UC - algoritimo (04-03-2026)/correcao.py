# QUESTÃO 1 - correta

numero1 = float(input ("Digite o primeiro numero: "))
numero2 = float(input ("Digite o segundo numero: "))

soma = numero1 + numero2 
produto = numero1 * numero2

#print ("A soma é {soma}")
print ("A soma é",soma)
print ("O produto é" ,produto) 


#QUESTÃO 2 - correta

numero = int(input("Digite um numero: "))

if numero %2==0: 
    print("O numero é par, e ele ao quadrado é: ", numero ** 2)
else: 
    print("O numero é impar, e ele ao cubo é: ", numero ** 3)   

# QUESTÃO 3 - correto 

nome = input ("Digite seu login: ")
senha = input ("Digite sua senha: ")

if (nome == "procopio" and senha =="12345") or (nome == "paiva" and senha == "54321"):
    print ("Seja Bem-Vindo!")
else: 
    print ("Usuário e senha não conferem")


# QUESTÃO 4 - (não fiz na aula - fazer + correção contra turno)

nome = input("Digite seu nome: ")
senhaCorreta = "123456"

tentativa = 3 

while tentativa > 0:
    senha = input("Digite sua senha: ")

    if senha == senhaCorreta:
        print(f"Olá, {nome}! Seja bem-vindo!")
    else: 
        tentativa -= 1

        if tentativa == 2:
           print ("Senha errada! Você tem 2 tentativas")
        elif tentativa == 1: 
            print ("Senha errada! Você tem 1 tentativa")
        else: 
            print("Senha bloqueada!")    
   