#um uso mais robusto é criar uma função que receba diversas notas de um aluno e retorne um resumo estatistico (soma, media e menor nota)

def somar_notas(*notas):
   #if not notas:
    #return 0,0,0,0 
   
    soma = sum(notas)
    media = soma / len(notas)
    maior = max(notas)
    menor = min(notas)   

    return soma, media, maior, menor


print(somar_notas(8.5, 7.0, 3.5, 7.14))