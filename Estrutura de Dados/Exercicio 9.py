# Programa para gerenciar uma biblioteca de livros
# Permite adicionar, remover, buscar e listar livros
# Usa listas e dicionários para armazenar os dados

def adicionar_livro(livros):
    """
    Função que permite ao usuário adicionar um novo livro.
    """
    titulo = input("Digite o título do livro: ")  # Solicita o título do livro
    autor = input("Digite o autor do livro: ")  # Solicita o autor do livro
    ano = input("Digite o ano de publicação: ")  # Solicita o ano de publicação
    genero = input("Digite o gênero do livro: ")  # Solicita o gênero do livro

    # Cria um dicionário representando o livro
    livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": int(ano),
        "genero": genero
    }

    livros.append(livro)  # Adiciona o dicionário à lista de livros
    print("Livro adicionado com sucesso!")  # Mensagem de confirmação

def remover_livro(livros):
    """
    Função que permite remover um livro pelo título.
    """
    titulo = input("Digite o título do livro a remover: ")  # Solicita o título do livro a ser removido
    encontrado = False  # Variável para verificar se o livro foi encontrado

    for livro in livros:  # Percorre a lista de livros
        if livro["titulo"].lower() == titulo.lower():  # Compara o título ignorando maiúsculas/minúsculas
            livros.remove(livro)  # Remove o livro da lista
            print("Livro removido com sucesso!")  # Mensagem de confirmação
            encontrado = True  # Marca que encontrou
            break  # Sai do loop após remover

    if not encontrado:  # Se não encontrou o livro
        print("Livro não encontrado.")  # Mensagem de erro

def buscar_por_titulo(livros):
    """
    Função que busca livros pelo título.
    """
    titulo = input("Digite o título do livro a buscar: ")  # Solicita o título para busca
    encontrado = False  # Variável para verificar se encontrou algum livro

    for livro in livros:  # Percorre a lista de livros
        if livro["titulo"].lower() == titulo.lower():  # Compara o título ignorando maiúsculas/minúsculas
            print("\nLivro encontrado:")  # Mensagem de sucesso
            print(f"Título: {livro['titulo']}")  # Exibe o título
            print(f"Autor: {livro['autor']}")  # Exibe o autor
            print(f"Ano: {livro['ano']}")  # Exibe o ano
            print(f"Gênero: {livro['genero']}")  # Exibe o gênero
            encontrado = True  # Marca que encontrou
            break  # Sai do loop

    if not encontrado:  # Se não encontrou
        print("Livro não encontrado.")  # Mensagem de erro

def buscar_por_autor(livros):
    """
    Função que busca livros pelo autor.
    """
    autor = input("Digite o nome do autor a buscar: ")  # Solicita o nome do autor
    encontrados = []  # Lista para armazenar livros encontrados

    for livro in livros:  # Percorre a lista de livros
        if livro["autor"].lower() == autor.lower():  # Compara o autor ignorando maiúsculas/minúsculas
            encontrados.append(livro)  # Adiciona o livro à lista de encontrados

    if encontrados:  # Se encontrou livros
        print(f"\nLivros do autor '{autor}':")  # Mensagem de sucesso
        for livro in encontrados:  # Exibe cada livro encontrado
            print(f"Título: {livro['titulo']}, Ano: {livro['ano']}, Gênero: {livro['genero']}")  # Exibe os dados
    else:
        print("Nenhum livro encontrado para esse autor.")  # Mensagem se não encontrar

def visualizar_todos_livros(livros):
    """
    Função que exibe todos os livros cadastrados.
    """
    if not livros:  # Verifica se a lista está vazia
        print("Nenhum livro cadastrado.")  # Mensagem de aviso
        return  # Encerra a função

    print("\nLista de todos os livros:")  # Título da listagem
    for livro in livros:  # Percorre cada livro
        print(f"Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}, Gênero: {livro['genero']}")  # Exibe os dados

def filtrar_por_genero(livros):
    """
    Função que exibe livros de um gênero específico.
    """
    genero = input("Digite o gênero para filtrar: ")  # Solicita o gênero
    encontrados = []  # Lista para armazenar livros encontrados

    for livro in livros:  # Percorre todos os livros
        if livro["genero"].lower() == genero.lower():  # Compara o gênero ignorando maiúsculas/minúsculas
            encontrados.append(livro)  # Adiciona o livro à lista de encontrados

    if encontrados:  # Se encontrou livros
        print(f"\nLivros do gênero '{genero}':")  # Mensagem de sucesso
        for livro in encontrados:  # Exibe os livros encontrados
            print(f"Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}")  # Exibe os dados
    else:
        print("Nenhum livro encontrado para esse gênero.")  # Mensagem se não encontrar

def ordenar_por_ano(livros):
    """
    Função que ordena os livros por ano de publicação.
    """
    if not livros:  # Verifica se a lista está vazia
        print("Nenhum livro cadastrado.")  # Mensagem de erro
        return  # Encerra a função

    # Ordena a lista de livros pelo campo 'ano' em ordem crescente
    livros_ordenados = sorted(livros, key=lambda livro: livro["ano"])

    print("\nLivros ordenados por ano de publicação:")  # Título da listagem
    for livro in livros_ordenados:  # Percorre os livros ordenados
        print(f"Ano: {livro['ano']}, Título: {livro['titulo']}, Autor: {livro['autor']}, Gênero: {livro['genero']}")  # Exibe os dados

def menu():
    """
    Função principal que exibe o menu de opções e controla a execução do programa.
    """
    livros = []  # Lista para armazenar os livros cadastrados

    while True:  # Loop infinito para manter o menu ativo
        # Exibe o menu de opções
        print("\n=== Menu da Biblioteca ===")
        print("1 - Adicionar livro")
        print("2 - Remover livro")
        print("3 - Buscar livro por título")
        print("4 - Buscar livro por autor")
        print("5 - Visualizar todos os livros")
        print("6 - Filtrar livros por gênero")
        print("7 - Ordenar livros por ano de publicação")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")  # Lê a opção do usuário

        if opcao == "1":  # Se escolher adicionar livro
            adicionar_livro(livros)  # Chama a função correspondente
        elif opcao == "2":  # Se escolher remover livro
            remover_livro(livros)  # Chama a função correspondente
        elif opcao == "3":  # Se escolher buscar por título
            buscar_por_titulo(livros)  # Chama a função correspondente
        elif opcao == "4":  # Se escolher buscar por autor
            buscar_por_autor(livros)  # Chama a função correspondente
        elif opcao == "5":  # Se escolher visualizar todos
            visualizar_todos_livros(livros)  # Chama a função correspondente
        elif opcao == "6":  # Se escolher filtrar por gênero
            filtrar_por_genero(livros)  # Chama a função correspondente
        elif opcao == "7":  # Se escolher ordenar por ano
            ordenar_por_ano(livros)  # Chama a função correspondente
        elif opcao == "0":  # Se escolher sair
            print("Encerrando o programa...")  # Mensagem de saída
            break  # Encerra o loop
        else:
            print("Opção inválida. Tente novamente.")  # Mensagem de erro para opção inválida

# Verifica se o programa está sendo executado diretamente
if __name__ == "__main__":
    menu()  # Chama a função principal para iniciar o programa
