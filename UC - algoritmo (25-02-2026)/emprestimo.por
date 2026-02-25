programa{
    funcao inicio (){
        real valorCasa, salario, prestacao
        inteiro anos, meses

        escreva ("Qual o valor da casa: ")
        leia (valorCasa)


        escreva ("Qual o valor do seu salario? ")
        leia (salario)

        escreva ("Em quantos anos você deseja pagar? ")
        leia (leia)

        meses = anos * 12
        prestacao = valorCasa / meses

        se (prestacao <= salario * 0.30) {
            escreva("Empréstimo aprovado \n")

        } senao {
            escreva("Empréstimo negado \n")
        }

    }

}