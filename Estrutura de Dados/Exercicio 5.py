# screver um programa em python que gerencia contatos de uma agenda telefônica, permitindo 
# adicionar, remover e buscar contatos por nome. Cada contato deve ter um nome, número de 
# telefone e e-mail.

# Função que exibe o menu de opções da agenda
def exibir_menu():
    print("\n===== AGENDA TELEFÔNICA =====")  # Título do menu
    print("1 - Adicionar contato")          # Opção 1: adicionar um novo contato
    print("2 - Remover contato")            # Opção 2: remover um contato existente
    print("3 - Buscar contato por nome")    # Opção 3: buscar contato pelo nome
    print("4 - Listar todos os contatos")   # Opção 4: mostrar todos os contatos
    print("0 - Sair")                       # Opção 0: encerrar o programa

# Função que adiciona um novo contato à agenda
def adicionar_contato(agenda):
    # Solicita o nome do contato ao usuário
    nome = input("Nome: ").strip()
    # .strip() remove espaços em branco extras no início e fim da string
    # Isso evita problemas com nomes digitados com espaço acidental

    # Solicita o telefone do contato
    telefone = input("Telefone: ").strip()

    # Solicita o e-mail do contato
    email = input("E-mail: ").strip()

    # Cria um dicionário com as informações do contato
    contato = {"nome": nome, "telefone": telefone, "email": email}

    # Adiciona o contato à lista de contatos (agenda)
    agenda.append(contato)

    # Mensagem de confirmação
    print(f"Contato '{nome}' adicionado com sucesso.")

# Função que remove um contato pelo nome
def remover_contato(agenda):
    # Solicita o nome do contato a ser removido
    nome = input("Digite o nome do contato que deseja remover: ").strip()

    # Percorre cada contato da lista
    for contato in agenda:
        # Compara os nomes sem considerar letras maiúsculas/minúsculas
        if contato["nome"].lower() == nome.lower():
            agenda.remove(contato)  # Remove o contato da lista
            print(f"Contato '{nome}' removido com sucesso.")
            return  # Encerra a função após encontrar e remover
    # Se não encontrar o nome, exibe mensagem
    print(f"Contato '{nome}' não encontrado.")

# Função que busca um contato pelo nome
def buscar_contato(agenda):
    # Solicita o nome a ser buscado
    nome = input("Digite o nome do contato que deseja buscar: ").strip()

    # Filtra os contatos com nome igual (ignorando maiúsculas/minúsculas)
    encontrados = [c for c in agenda if c["nome"].lower() == nome.lower()]

    # Se encontrar um ou mais contatos com o nome buscado
    if encontrados:
        print("\nContatos encontrados:")
        # Exibe os contatos encontrados
        for c in encontrados:
            print(f"Nome: {c['nome']}, Telefone: {c['telefone']}, E-mail: {c['email']}")
    else:
        # Caso nenhum contato seja encontrado
        print(f"Nenhum contato encontrado com o nome '{nome}'.")

# Função que lista todos os contatos cadastrados na agenda
def listar_contatos(agenda):
    if not agenda:  # Verifica se a lista está vazia
        print("Nenhum contato cadastrado.")
        return  # Sai da função

    print("\nLista de contatos:")
    # Percorre e exibe cada contato da agenda
    for c in agenda:
        print(f"Nome: {c['nome']}, Telefone: {c['telefone']}, E-mail: {c['email']}")

# Função principal que gerencia a execução do programa
def main():
    agenda = []  # Cria uma lista vazia para armazenar os contatos

    # Inicia um loop que continuará até o usuário escolher sair
    while True:
        exibir_menu()  # Exibe o menu de opções

        # Lê a opção escolhida pelo usuário, removendo espaços extras
        opcao = input("Escolha uma opção: ").strip()

        # Compara a opção escolhida e chama a função correspondente
        if opcao == "1":
            adicionar_contato(agenda)
        elif opcao == "2":
            remover_contato(agenda)
        elif opcao == "3":
            buscar_contato(agenda)
        elif opcao == "4":
            listar_contatos(agenda)
        elif opcao == "0":
            print("Encerrando a agenda. Até logo!")
            break  # Encerra o loop e o programa
        else:
            # Caso o usuário digite uma opção inválida
            print("Opção inválida. Tente novamente.")

# Verifica se este arquivo está sendo executado diretamente
if __name__ == "__main__":
    main()  # Chama a função principal para iniciar o programa
