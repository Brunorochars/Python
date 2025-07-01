import manipula_lista

def exibir_menu():
    opcao = int(input("\n===== ANIME MANIA ====="
    "1 -  Listar animes disponíveis"
    "2 -  Exibir detalhes de um anime"
    "3 -  Adicionar anime à lista de favoritos"
    "4 -  Modificar um anime existente"
    "5 -  Remover anime da lista de favoritos"
    "6 -  Sair"))


def escolher_opcao(opcao):
    if(opcao == 1):
        return manipula_lista.listar_animes()
    elif(opcao == 2):
        return manipula_lista.exibir_detalhes_anime()
    elif(opcao == 3):
        return manipula_lista.adicionar_anime()
    elif(opcao == 4):
        return manipula_lista.modificar_anime()
    elif(opcao == 5):
        return manipula_lista.remover_anime()
    elif(opcao == 6):
        return "Você saiu!!!"
    else: "Número inválido"