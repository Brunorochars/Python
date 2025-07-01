"""
Crie um programa que faça o gerenciamento de bebidas para um apreciador de bebidas.

O programa deve permitir que o usuário adicione bebidas, remova bebidas, liste todas as bebidas e busque uma bebida específica pelo nome.

Os dados devem ser armazenados em um arquivo JSON.

------------

=============================================================
==== COISAS QUE PRECISO FAZER PARA IMPLEMENTAR O PROJETO ====
=============================================================
1. Criar um menu com as opções para o usuário:
    - Listar Bebidas
    - Adicionar Bebida
    - Remover Bebida
    - Buscar Bebida
    - Sair
2. Criar funções vazias para cada uma das opções do menu (exceto "Sair").
3. Criar 2 funções específicas para manipulação do arquivo JSON (uma para ler os dados e outra para escrever os dados).
4. Definir estrutura para armazenar as bebidas (como o dicionário vai se parecer).
    {
        "id": [int autoincrement],
        "nome": [str],
        "data_aquisicao": [str],
        "tipo": [str],
        "percentual_alcoolico": [float],
    }
5. Implementar a lógica de cada função do menu.
    - "Sair"
        1. Finalizar o while principal que controla o menu.
    - "Listar Bebidas"
        1. Ler os dados das minhas bebidas (lista de dicionários). 
        2. Itero sobre cada bebida imprimindo os seus dados.
    - "Adicionar Bebida"
        1. Ler os dados das minhas bebidas (lista de dicionários). 
        2. Solicitar os dados da bebida ao usuário.
        3. Adicionar a bebida à lista de bebidas.
        4. Atualizar arquivo JSON.
    - "Remover Bebida"
        1. Executar função "Listar Bebidas".
        2. Solicitar ao usuário o identificador da bebida a ser removida.
        3. Remover a bebida da lista de bebidas.*
        4. Atualizar arquivo JSON.
    - "Buscar Bebida"
        1. Solicitar ao usuário o nome da bebida a ser buscada.
        2. Percorrer os dados das minhas bebidas (lista de dicionários).
        3. Verificar se alguma das bebidas sendo manipuladas possui o nome buscado.
            -> Se sim, imprimir os dados da bebida.
            -> Se não, imprimir mensagem de que a bebida não foi encontrada.
"""

# Importando módulo JSON para persistir os dados das bebidas em disco
import json

# Importando a função system do módulo os para limpar a tela do console
from os import system, name


def escrever_arquivo(nome_arquivo: str, bebidas: list):
    """Escreve a lista de bebidas em um arquivo JSON.

    Args:
        nome_arquivo (str): Nome do arquivo JSON onde as bebidas serão armazenadas.
        bebidas (list): Lista de bebidas a serem armazenadas no arquivo.
    """
    # Abrindo um arquivo chamado "nome_arquivo" no modo de escrita
    with open(nome_arquivo, "w", encoding="utf-8") as escritor:
        # Convertendo a lista de bebidas para o formato JSON e escrevendo no arquivo
        json.dump(bebidas, escritor, indent=4)


def ler_arquivo(nome_arquivo: str):
    """Lê o arquivo JSON contendo as bebidas.

    Args:
        nome_arquivo (str): Nome do arquivo JSON a ser lido.

    Returns:
        bebidas (list): Lista de bebidas lidas do arquivo.
    """
    with open(nome_arquivo, "r", encoding="utf-8") as leitor:
        bebidas = json.load(leitor)
    return bebidas


def listar_bebidas(bebidas: list):
    """Lista as bebidas armazenadas.

    Args:
        bebidas (list): Lista de bebidas.
    """
    print("\n\n")
    print("---- Listando Bebidas ----")
    for bebida in bebidas:
        print(
            f"[{bebida['id']}] Nome: {bebida['nome']}. Data de aquisição: {bebida['data_aquisicao']}. Tipo: {bebida['tipo']}. Percentual alcoólico: {bebida['percentual_alcoolico']}%."
        )


def adicionar_bebida(bebidas: list):
    # Solicitando ao usuário informações sobre a bebida a ser adicionada
    nome = input("Digite o nome da bebida: ")
    data_aquisicao = input("Digite a data de aquisição (DD/MM/AAAA): ")
    tipo = input("Digite o tipo da bebida: ")
    percentual_alcoolico = float(input("Digite o percentual alcoólico da bebida: "))

    # Atribuindo as informações da nova bebida a um dicionário
    nova_bebida = {
        "id": bebidas[-1]["id"] + 1,  # Atribuindo um ID autoincremental baseado no último ID da lista
        "nome": nome,
        "data_aquisicao": data_aquisicao,
        "tipo": tipo,
        "percentual_alcoolico": percentual_alcoolico,
    }

    # Adicionando a nova bebida à lista de bebidas
    bebidas.append(nova_bebida)

    # Atualizando o arquivo JSON com a nova lista de bebidas
    escrever_arquivo(nome_arquivo="bebidas.json", bebidas=bebidas)

    # Exibindo a nova bebida adicionada
    print("\n\n")
    print("---- Bebida Adicionada com Sucesso ----")
    print("Dados da nova bebida:")
    print(
        f"[{nova_bebida['id']}] Nome: {nova_bebida['nome']}. Data de aquisição: {nova_bebida['data_aquisicao']}. Tipo: {nova_bebida['tipo']}. Percentual alcoólico: {nova_bebida['percentual_alcoolico']}%."
    )

    # Retornando a lista atualizada de bebidas
    return bebidas


def remover_bebida(bebidas: list):
    print("\n\n")
    print("---- Removendo Bebida ----")
    listar_bebidas(bebidas=bebidas)
    print("\n\n")
    id_bebida = int(input("Selecione o identificador bebida que deseja remover: "))

    # Definindo uma variável para armazenar a bebida a ser removida (inicialmente None)
    bebida = None

    # Iterando sobre a lista de bebidas para encontrar a bebida com o ID fornecido
    for bebida_existente in bebidas:
        if bebida_existente["id"] == id_bebida:
            bebida = bebida_existente
            break

    # Removendo a bebida da lista se ela foi encontrada
    if bebida != None:
        # Exibindo os dados da bebida que será removida
        print("\n\n")
        print("---- Dados da Bebida a ser Removida ----")
        print(
            f"[{bebida['id']}] Nome: {bebida['nome']}. Data de aquisição: {bebida['data_aquisicao']}. Tipo: {bebida['tipo']}. Percentual alcoólico: {bebida['percentual_alcoolico']}%."
        )

        confirmacao = input("Você tem certeza que deseja remover essa bebida? (s/n): ").lower()

        if confirmacao == "s":
            bebidas.remove(bebida)
            escrever_arquivo(nome_arquivo="bebidas.json", bebidas=bebidas)
            print("\n\n")
            print("---- Bebida Removida com Sucesso ----")

    return bebidas


def buscar_bebida_por_nome(bebidas: list):
    nome = input("Digite o nome da bebida que deseja buscar: ")

    bebida_encontrada = None

    for bebida in bebidas:
        if bebida["nome"] == nome:
            bebida_encontrada = bebida
            break

    if bebida_encontrada != None:
        print("\n\n")
        print("---- Bebida Encontrada ----")
        print(
            f"[{bebida_encontrada['id']}] Nome: {bebida_encontrada['nome']}. Data de aquisição: {bebida_encontrada['data_aquisicao']}. Tipo: {bebida_encontrada['tipo']}. Percentual alcoólico: {bebida_encontrada['percentual_alcoolico']}%."
        )
    else:
        print("\n\n")
        print("---- Bebida Não Encontrada ----")

    return bebida_encontrada


def main():
    bebidas = ler_arquivo("bebidas.json")

    while True:
        print("================================")
        print("==== GERENCIADOR DE BEBIDAS ====")
        print("================================")
        print("")
        print("Bem-vindo ao Gerenciador de Bebidas!")
        print("Este é um sistema simples para gerenciar bebidas. Você pode adicionar, listar e remover bebidas.")
        print("")
        print("Escolha uma das seguintes opções:")
        print("")
        print("1. Listar Bebidas")
        print("2. Adicionar Bebida")
        print("3. Remover Bebida")
        print("4. Buscar Bebida")
        print("5. Sair")
        print("")

        opcao_usuario = input("Escolha a opção desejada (1-5): ")

        if opcao_usuario == "1":
            listar_bebidas(bebidas=bebidas)

        elif opcao_usuario == "2":
            bebidas = adicionar_bebida(bebidas=bebidas)

        elif opcao_usuario == "3":
            bebidas = remover_bebida(bebidas=bebidas)

        elif opcao_usuario == "4":
            bebida_encontrada = buscar_bebida_por_nome(bebidas=bebidas)

        elif opcao_usuario == "5":
            print("\n\n")
            print("Saindo do programa. Até logo!")
            break

        print("\n\n")
        input("Pressione qualquer tecla para continuar...")
        if name == "nt":
            system("cls")
        else:
            system("clear")


main()
