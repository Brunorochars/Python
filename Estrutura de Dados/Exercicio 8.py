# Programa para gerenciar uma locadora de filmes
# Permite adicionar, remover, buscar e visualizar filmes
# Usa listas e dicionários para armazenar os dados

def adicionar_filme(filmes):
    """
    Função que permite ao usuário adicionar um novo filme.
    """
    titulo = input("Digite o título do filme: ")  # Solicita o título do filme ao usuário
    genero = input("Digite o gênero do filme: ")  # Solicita o gênero do filme ao usuário
    ano = input("Digite o ano de lançamento: ")  # Solicita o ano de lançamento
    classificacao = input("Digite a classificação indicativa: ")  # Solicita a classificação indicativa

    # Cria um dicionário com os dados do filme
    filme = {
        "titulo": titulo,
        "genero": genero,
        "ano": int(ano),
        "classificacao": classificacao
    }

    filmes.append(filme)  # Adiciona o dicionário do filme à lista de filmes
    print("Filme adicionado com sucesso!")  # Confirmação de adição

def remover_filme(filmes):
    """
    Função que permite remover um filme pelo título.
    """
    titulo = input("Digite o título do filme a remover: ")  # Solicita o título do filme a ser removido
    encontrado = False  # Variável de controle para verificar se o filme foi encontrado

    for filme in filmes:  # Percorre a lista de filmes
        if filme["titulo"].lower() == titulo.lower():  # Verifica se o título corresponde (ignorando maiúsculas/minúsculas)
            filmes.remove(filme)  # Remove o filme da lista
            print("Filme removido com sucesso!")  # Confirmação de remoção
            encontrado = True  # Marca que o filme foi encontrado
            break  # Sai do loop após remover

    if not encontrado:  # Se o filme não foi encontrado
        print("Filme não encontrado.")  # Mensagem de erro

def buscar_filme(filmes):
    """
    Função que permite buscar um filme pelo título.
    """
    titulo = input("Digite o título do filme a buscar: ")  # Solicita o título para busca
    encontrado = False  # Variável de controle para verificar se o filme foi encontrado

    for filme in filmes:  # Percorre a lista de filmes
        if filme["titulo"].lower() == titulo.lower():  # Verifica se o título corresponde
            print("\nFilme encontrado:")  # Mensagem de sucesso
            print(f"Título: {filme['titulo']}")  # Exibe o título
            print(f"Gênero: {filme['genero']}")  # Exibe o gênero
            print(f"Ano: {filme['ano']}")  # Exibe o ano
            print(f"Classificação: {filme['classificacao']}")  # Exibe a classificação
            encontrado = True  # Marca que o filme foi encontrado
            break  # Sai do loop após encontrar

    if not encontrado:  # Se o filme não foi encontrado
        print("Filme não encontrado.")  # Mensagem de erro

def visualizar_todos_filmes(filmes):
    """
    Função que exibe todos os filmes cadastrados.
    """
    if not filmes:  # Verifica se a lista está vazia
        print("Nenhum filme cadastrado.")  # Mensagem se não houver filmes
        return  # Encerra a função

    print("\nLista de todos os filmes:")  # Título da listagem
    for filme in filmes:  # Percorre cada filme
        print(f"Título: {filme['titulo']}, Gênero: {filme['genero']}, Ano: {filme['ano']}, Classificação: {filme['classificacao']}")  # Exibe os dados

def filtrar_por_genero(filmes):
    """
    Função que exibe os filmes filtrados por um gênero específico.
    """
    genero = input("Digite o gênero para filtrar: ")  # Solicita o gênero ao usuário
    encontrados = []  # Lista para armazenar filmes encontrados

    for filme in filmes:  # Percorre todos os filmes
        if filme["genero"].lower() == genero.lower():  # Verifica se o gênero corresponde
            encontrados.append(filme)  # Adiciona o filme à lista de encontrados

    if encontrados:  # Se houver filmes encontrados
        print(f"\nFilmes do gênero '{genero}':")  # Título da listagem
        for filme in encontrados:  # Exibe os filmes encontrados
            print(f"Título: {filme['titulo']}, Ano: {filme['ano']}, Classificação: {filme['classificacao']}")  # Exibe os dados
    else:
        print("Nenhum filme encontrado para esse gênero.")  # Mensagem se não encontrar

def ordenar_por_ano(filmes):
    """
    Função que ordena os filmes por ano de lançamento.
    """
    if not filmes:  # Verifica se a lista está vazia
        print("Nenhum filme cadastrado.")  # Mensagem de erro
        return  # Encerra a função

    # Ordena a lista de filmes pelo campo 'ano' em ordem crescente
    filmes_ordenados = sorted(filmes, key=lambda filme: filme["ano"])

    print("\nFilmes ordenados por ano de lançamento:")  # Título da listagem
    for filme in filmes_ordenados:  # Percorre os filmes ordenados
        print(f"Ano: {filme['ano']}, Título: {filme['titulo']}, Gênero: {filme['genero']}, Classificação: {filme['classificacao']}")  # Exibe os dados

def menu():
    """
    Função principal que exibe o menu de opções para o usuário.
    """
    filmes = []  # Lista para armazenar os filmes

    while True:  # Loop infinito para manter o menu ativo
        # Exibe o menu de opções
        print("\n=== Menu da Locadora ===")
        print("1 - Adicionar filme")
        print("2 - Remover filme")
        print("3 - Buscar filme por título")
        print("4 - Visualizar todos os filmes")
        print("5 - Filtrar filmes por gênero")
        print("6 - Ordenar filmes por ano de lançamento")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")  # Lê a opção escolhida pelo usuário

        if opcao == "1":  # Se o usuário escolher adicionar filme
            adicionar_filme(filmes)  # Chama a função correspondente
        elif opcao == "2":  # Se escolher remover
            remover_filme(filmes)  # Chama a função correspondente
        elif opcao == "3":  # Se escolher buscar
            buscar_filme(filmes)  # Chama a função correspondente
        elif opcao == "4":  # Se escolher visualizar todos
            visualizar_todos_filmes(filmes)  # Chama a função correspondente
        elif opcao == "5":  # Se escolher filtrar por gênero
            filtrar_por_genero(filmes)  # Chama a função correspondente
        elif opcao == "6":  # Se escolher ordenar por ano
            ordenar_por_ano(filmes)  # Chama a função correspondente
        elif opcao == "0":  # Se escolher sair
            print("Encerrando o programa...")  # Mensagem de encerramento
            break  # Sai do loop, encerrando o programa
        else:
            print("Opção inválida. Tente novamente.")  # Mensagem se a opção for inválida

# Verifica se o programa está sendo executado diretamente
if __name__ == "__main__":
    menu()  # Chama a função principal para iniciar o programa
