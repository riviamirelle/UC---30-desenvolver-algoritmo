# SISTEMA DE GESTÂO DE BIBLIOTECA

#Dicionario para armazenar os livros
catalogo = {}

# dicionario para armazenar os emprestimos 
emprestimoAtivo = {}

#lista para armazenar o histórico de transição
historico = []

def adicionarLivro(codigo, titulo, autor, quantidade):
    if codigo in catalogo: 
        print(f"ERRO: livro com código {codigo} já existe!")
        return False
    
    catalogo[codigo] = {
        "titulo": titulo,
        "autor": autor, 
        "quantidade": quantidade
    }

    print(f"LIVRO '{titulo}' adicionado com sucesso")
    return True 

# FUNÇÃO: EMPRESTAR LIVRO

def emprestarLivro(codigo, nome_aluno):

    if codigo not in catalogo: 
        print(f"ERRO: Livro com código {codigo} não encontrado")
        return False 
    
    if catalogo [codigo]["quantidade"] <=0:
        print(f"ERRO: '{catalogo[codigo['titulo']]}' não encontrado!")
        return False
    
    livroAluno = contarLivrosAlunos(nomeAluno)
    if livroAluno >= 2:
        print(f"ERRO: Aluno já pegou a quantidade máxima")
        return False 
    
    if codigo in emprestimos_ativos and nome_aluno in emprestimos_ativos[codigo]:
        print(f"ERRO: {nome_aluno} já pegou este livro!")
        return False
    
    if codigo not in emprestimos_ativos:
        emprestimos_ativos[codigo] = []

emprestimos_ativos[codigo].append(nome_aluno)


catalogo[codigo]["quantidade"] -= 1


historico.append({
    "tipo": "emprestimo",
    "codigo": codigo,
    "titulo": catalogo[codigo]["titulo"],
    "aluno": nome_aluno
})

print(f"(nome_aluno) pegou '{catalogo[codigo]['titulo']}' com sucesso!")
return True 