def calcular_imc():
    try: 
        peso =   float(input("Digite seu peso (kg): "))
        altura = float(input("Digite sua altura (m): "))

        imc = peso / (altura ** 2) 

        print(f"Seu IMC é: {imc:.2f}")

        if imc < 18.9:
            print ("CLASSIFICAÇÃO: Magro")
        elif imc <= 24.9: 
         print ("CLASSIFICAÇÃO: Normal")
        else: 
         print("CLASSIFICAÇÃO: Acima do peso")

    except: 
            print ("ERRO: Digite valores validos")

calcular_imc()            