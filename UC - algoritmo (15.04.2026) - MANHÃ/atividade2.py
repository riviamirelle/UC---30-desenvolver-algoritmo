def total_compra():
    try: 
        preco1 = float(input("Digite o preço do primeiro produto: "))
        preco1 = float(input("Digite o preço do primeiro produto: "))

        total = preco1 + preco2

        print(f"Total de compra: R$ {total:.2f}")

    except ValueError: 
        print("Erro: os preços devem ser números!")

total_compra()        