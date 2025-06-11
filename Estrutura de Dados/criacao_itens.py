def criar_item() -> dict:
    """Função que cria um novo item.

    Returns:
        (dict): Dicionário representando o item criado.
    """
    # Criando dicionário vazio para armazenar o item
    item = {}

    # Definindo chaves para o dicionário e atribuindo valores a essas chaves conforme o que o usuário digita
    item["nome"] = input("\tDigite o nome do item: ")
    item["quantidade"] = int(input("\tDigite a quantidade do item: "))  # Convertemos o valor digitado para inteiro

    # Retornando o dicionário final
    return item


# Solicitando ao usuário a quantidade de itens que ele deseja criar
quantidade_de_itens = int(input("Digite a quantidade de itens que você deseja criar: "))

# Definindo uma lista vazia para armazenarmos todos os itens
itens_criados = []

print("")
print("==== Começando a Criação de Itens ====")

# Iterando X vezes, onde X é o valor que recém armazenamos em "quantidade_de_itens"
for indice in range(quantidade_de_itens):
    print(f"Criando Item {indice}")

    # Chamando a função "criar_item()" que nos devolve um dicionário com informações que adicionamos
    # O resultado da função "criar_item()" é armazenado na variável "item_criado"
    item_criado = criar_item()

    print(f"\t\tAdicionando Item {indice} à Lista de Itens")

    # Adicionando "item_criado" à lista "itens_criados"
    itens_criados.append(item_criado)
    print("\n")

print("===== Exibindo Itens Adicionados à Lista de Itens =====")
# Iterando sobre os itens presentes na lista "itens_criados"
for item in itens_criados:
    print(item)
