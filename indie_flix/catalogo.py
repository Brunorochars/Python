"""

•⁠ catalogo.py: contém a lógica de manipulação dos filmes (adicionar, editar, remover, listar).

O programa deve permitir que o usuário informe, para cada filme, os seguintes dados:

•⁠ Título

•⁠ Diretor

•⁠ Ano de lançamento

•⁠ Gênero

•⁠ Duração

•⁠ Nota pessoal

"""

import json

def ler_arquivo(nome_arquivo: str, filmes: list):
    with open(nome_arquivo, "r", encoding="utf-8") as leitor:
        filmes = json.load(leitor)
    return filmes

def escrever_arquivo(nome_arquivo: str, filmes: list):
    with open(nome_arquivo, "w", encoding="utf-8") as escritor:
        json.dump(filmes, escritor, indent=4)

def adicionar_filme(filmes: list):

    titulo = input("Digite o titulo do filme:")
    diretor = input("Digite o nome do diretor: ")
    ano_lancamento = input("Digite o ano de lançamento (DD/MM/AAAA)")
    genero = input("Digite o genero do filme: ")
    duracao = float(input("Digite a duração do filme: "))
    nota_pessoal = input("Adicione uma nota pessoal: ")

    novo_filme = {
        "id": filmes[-1]["id"] + 1,
        "titulo": titulo,
        "diretor": diretor,
        "ano_lancamento": ano_lancamento,
        "genero": genero,
        "duracao": duracao,
        "nota_pessoal": nota_pessoal
    }

    filmes.append(novo_filme)

    escrever_arquivo(nome_arquivo="filmes.json", filmes=filmes)

    print("\n\n")
    print("Filme adicionado com sucesso!!!")
    
    return filmes

def listar_filmes(filmes:list):
    print("\n\n")
    print("=====| Listando Filmes |=====")
    for filme in filmes:
        print(
            f"[{filme['id']}] Titulo: {filme['titulo']}. Diretor: {filme['diretor']}. Ano de lançamento: {filme['ano_lancamento']}. Genero: {filme['genero']}. Duração: {filme['duracao']}. Nota pessoal: {filme['nota_pessoal']}."
        )

def remover_filme(filmes:list):
    print("\n\n")
    print("=====| Removendo Filme |=====")
    listar_filmes(filmes=filmes)
    print("\n\n")
    id_filme = int(input("Selecione o ID do filme a ser removido: "))

    filme = None

    for filme_existente in filmes:
        if filme_existente["id"] == id_filme:
            filme = filme_existente
            break
    
    if filme != None:
        print("\n\n")
        print("=====| Dados do Filme a ser removido |=====")
        print(
            f"[{filme['id']}] Titulo: {filme['titulo']}. Diretor: {filme['diretor']}. Ano de lançamento: {filme['ano_lancamento']}. Genero: {filme['genero']}. Duração: {filme['duracao']}. Nota pessoal: {filme['nota_pessoal']}."
        )

        confirmacao = input("Deseja remover o filme? (s/n)").lower()

        if confirmacao == "s":
            filmes.remove(filme)
            escrever_arquivo(nome_arquivo="filmes.json", filmes=filmes)
            print("\n\n")

    return filmes
