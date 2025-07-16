import catalogo
import busca

def exibir_menu():
    filmes = catalogo.ler_arquivo("filmes.json")

    while True:
        print("\n|=====================================|")
        print("|============ Indie Flix =============|")
        print("|=====================================|")
        print("|       Bem-vindo ao Indie Flix!      |")
        print("|         Escolha uma opção:          |")
        print("|_______________ MENU ________________|")
        print("| 1. Listar Filmes                    |")
        print("| 2. Adicionar Filme                  |")
        print("| 3. Editar Filme                     |")
        print("| 4. Remover Filme                    |")
        print("| 5. Buscar Filme                     |")
        print("| 6. Sair                             |")
        print("---------------------------------------\n")
        

        opcao = input("Escolha uma opção de (1 a 6): ").strip()
        print("\n")

        if opcao == "1":
            catalogo.listar_filmes(filmes)
        elif opcao == "2":
            filmes = catalogo.adicionar_filme(filmes)
        elif opcao == "3":
            filmes = catalogo.editar_filme(filmes)
        elif opcao == "4":
            filmes = catalogo.remover_filme(filmes)
        elif opcao == "5":
            busca.buscar_filme(filmes)
        elif opcao == "6":
            print("\nAté logo!\n")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    exibir_menu()