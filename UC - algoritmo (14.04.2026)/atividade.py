def soma_segura(a,b):
    try: 
        resultado = a+b
        return resultado
    except TypeError: 
        print ("entrada invalida")
        return 0