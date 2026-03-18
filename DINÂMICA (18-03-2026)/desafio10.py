def receba_numero(numero):
    if numero > 0:
        return "POSITIVO"
    elif numero < 0: 
        return "NEGATIVO"
    else: 
        return "ZERO"  
    
print(receba_numero(10))