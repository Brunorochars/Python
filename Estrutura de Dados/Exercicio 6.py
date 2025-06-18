# Escrever um programa que gerencia uma lista de tarefas, permitindo adicionar, 
# remover e editar tarefas. Cada tarefa deve ter um título, descrição, status 
# (pendente ou concluída) e data de vencimento. O usuário deve poder visualizar 
# todas as tarefas, filtrar por status e ordenar por data de vencimento.

from datetime import datetime

# Função que exibe o menu principal do sistema
def exibir_menu():
    print("\n===== GERENCIADOR DE TAREFAS =====")
    print("1 - Adicionar tarefa")
    print("2 - Remover tarefa")
    print("3 - Editar tarefa")
    print("4 - Visualizar todas as tarefas")
    print("5 - Filtrar tarefas por status")
    print("6 - Ordenar tarefas por data de vencimento")
    print("0 - Sair")

# Função para adicionar uma nova tarefa à lista
def adicionar_tarefa(tarefas):
    titulo = input("Título: ").strip()  # Lê o título da tarefa
    descricao = input("Descrição: ").strip()  # Lê a descrição
    status = input("Status (pendente/concluída): ").strip().lower()  # Lê e padroniza o status
    data_str = input("Data de vencimento (dd/mm/aaaa): ").strip()

    try:
        data_vencimento = datetime.strptime(data_str, "%d/%m/%Y")  # Converte a data
    except ValueError:
        print("Data inválida! Tarefa não adicionada.")
        return

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "status": status,
        "vencimento": data_vencimento
    }

    tarefas.append(tarefa)  # Adiciona à lista
    print(f"Tarefa '{titulo}' adicionada com sucesso.")

# Função para remover uma tarefa com base no título
def remover_tarefa(tarefas):
    titulo = input("Digite o título da tarefa que deseja remover: ").strip()

    for tarefa in tarefas:
        if tarefa["titulo"].lower() == titulo.lower():
            tarefas.remove(tarefa)
            print(f"Tarefa '{titulo}' removida.")
            return
    print("Tarefa não encontrada.")

# Função para editar uma tarefa existente
def editar_tarefa(tarefas):
    titulo = input("Digite o título da tarefa que deseja editar: ").strip()

    for tarefa in tarefas:
        if tarefa["titulo"].lower() == titulo.lower():
            print("Deixe em branco para manter o valor atual.")
            novo_titulo = input(f"Novo título [{tarefa['titulo']}]: ").strip()
            nova_descricao = input(f"Nova descrição [{tarefa['descricao']}]: ").strip()
            novo_status = input(f"Novo status (pendente/concluída) [{tarefa['status']}]: ").strip().lower()
            nova_data_str = input(f"Nova data de vencimento (dd/mm/aaaa) [{tarefa['vencimento'].strftime('%d/%m/%Y')}]: ").strip()

            if novo_titulo:
                tarefa["titulo"] = novo_titulo
            if nova_descricao:
                tarefa["descricao"] = nova_descricao
            if novo_status:
                tarefa["status"] = novo_status
            if nova_data_str:
                try:
                    tarefa["vencimento"] = datetime.strptime(nova_data_str, "%d/%m/%Y")
                except ValueError:
                    print("Data inválida! A data anterior será mantida.")

            print("Tarefa atualizada com sucesso.")
            return

    print("Tarefa não encontrada.")

# Função para exibir todas as tarefas
def visualizar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for i, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa {i}:")
        print(f"Título: {tarefa['titulo']}")
        print(f"Descrição: {tarefa['descricao']}")
        print(f"Status: {tarefa['status'].capitalize()}")
        print(f"Vencimento: {tarefa['vencimento'].strftime('%d/%m/%Y')}")

# Função para filtrar tarefas por status
def filtrar_por_status(tarefas):
    status_desejado = input("Filtrar por status (pendente/concluída): ").strip().lower()
    filtradas = [t for t in tarefas if t["status"] == status_desejado]

    if not filtradas:
        print(f"Nenhuma tarefa com status '{status_desejado}'.")
    else:
        visualizar_tarefas(filtradas)

# Função para ordenar as tarefas pela data de vencimento
def ordenar_por_data(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    # Ordena usando a chave 'vencimento'
    ordenadas = sorted(tarefas, key=lambda t: t["vencimento"])
    print("\nTarefas ordenadas por data de vencimento:")
    visualizar_tarefas(ordenadas)

# Função principal que executa o sistema
def main():
    tarefas = []  # Lista que armazenará todas as tarefas

    while True:
        exibir_menu()  # Mostra o menu principal
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            adicionar_tarefa(tarefas)
        elif opcao == "2":
            remover_tarefa(tarefas)
        elif opcao == "3":
            editar_tarefa(tarefas)
        elif opcao == "4":
            visualizar_tarefas(tarefas)
        elif opcao == "5":
            filtrar_por_status(tarefas)
        elif opcao == "6":
            ordenar_por_data(tarefas)
        elif opcao == "0":
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Ponto de entrada do programa
if __name__ == "__main__":
    main()
