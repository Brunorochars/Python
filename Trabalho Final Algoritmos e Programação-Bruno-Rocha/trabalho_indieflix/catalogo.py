import json

def ler_arquivo(nome_arquivo: str):
    
    with open(nome_arquivo, "r", encoding="utf-8") as leitor:
        return json.load(leitor)
    
def escrever_arquivo(nome_arquivo: str, filmes: list):
    with open(nome_arquivo, "w", encoding="utf-8") as escritor:
        json.dump(filmes, escritor, indent=4)

def adicionar_filme(filmes: list):
    print("=======================================")
    print("========== Adicionar Filmes ===========")
    print("=======================================\n")
    titulo = input("Digite o título do filme: ")
    diretor = input("Digite o nome do diretor: ")
    while True:
        try:
            ano_lancamento = int(input("Digite o ano de lançamento (AAAA): "))
            break
        except ValueError:
            print("Ano inválido.")
    while True:
        print("|=====================================|")
        print("|========== Gênero do Filme ==========|")
        print("|=====================================|")
        print("|                                     |")
        print("|1 - Curta                            |")
        print("|2 - Documentário                     |")
        print("|3 - Filme                            |")
        print("---------------------------------------\n")
        opcao = input("Selecione o gênero do filme:")
        if opcao == "1":
            genero = "Curta"
            break
        elif opcao == "2":
            genero = "Documentário"
            break
        elif opcao == "3":
            genero = "Filme"
            break
        else:
            print("Opção inválida!!")

    while True:
        try:
            duracao = float(input("Digite a duração do filme (minutos): "))
            break
        except ValueError:
            print("Duração inválida.")
    
    while True:
        try:
            nota = float(input("Nota pessoal: "))
            if nota >= 0 and nota <= 10:
                nota_pessoal = nota
                break
            else:
                print("A nota deve ser de 0 a 10!!!")
        except ValueError:
            print("Digite uma nota válida (número)!")

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
    escrever_arquivo("filmes.json", filmes)
    print("Filme adicionado com sucesso!")
    return filmes

def listar_filmes(filmes: list):
    print("\n=====================================| Lista de Filmes |=====================================")
    if not filmes:
        print("Nenhum filme cadastrado.")
    for filme in filmes:
        print(f"|[{filme['id']}] {filme['titulo']} | {filme['diretor']} | {filme['ano_lancamento']} | {filme['genero']} | {filme['duracao']} min | Nota: {filme['nota_pessoal']}|")

def remover_filme(filmes: list):

    listar_filmes(filmes)
    filme = None

    try:
        id_remover = int(input("\nID do filme a remover: "))
    except ValueError:
        print("ID inválido.")
        return filmes
    
    for filme_existente in filmes:
        if filme_existente["id"] == id_remover:
            filme = filme_existente
            break

    if not filme:
        print("Filme não encontrado.")
        return filmes
    
    confirmar = input(f"Remover '{filme['titulo']}'? (s/n): ").lower()

    if confirmar == "s":
        filmes.remove(filme)
        escrever_arquivo("filmes.json", filmes)
        print("Filme removido com sucesso.")
    return filmes

def editar_filme(filmes: list):
    
    listar_filmes(filmes)

    filme = None
    while True:
        try:
            id_editar = int(input("\nDigite o ID do filme que você deseja editar: \n"))
            break
        except ValueError:
            print("O ID digitado é inválido inválido.")
        
    
    for filme_existente in filmes:
        if filme_existente["id"] == id_editar:
            filme = filme_existente
            break

    if not filme:
        print("Filme não encontrado.")
        return filmes
    
    print("Pressione Enter para manter o valor atual.")

    novo = input(f"Título [{filme['titulo']}]: ").strip()
    if novo: filme["titulo"] = novo
    novo = input(f"Diretor [{filme['diretor']}]: ").strip()
    if novo: filme["diretor"] = novo
    opcao_editar_genero = input("Deseja alterar o gênero? (S/N): ").lower()

    if opcao_editar_genero == "s":
        while True:
            print("|=====================================|")
            print("|========== Gênero do Filme ==========|")
            print("|=====================================|")
            print("|                                     |")
            print("|1 - Curta                            |")
            print("|2 - Documentário                     |")
            print("|3 - Filme                            |")
            print("---------------------------------------\n")
            opcao = input("Selecione o gênero do filme:")
            if opcao == "1":
                filme['genero'] = "Curta"
                break
            elif opcao == "2":
                filme['genero'] = "Documentário"
                break
            elif opcao == "3":
                filme['genero'] = "Filme"
                break
            else:
                print("Opção inválida!!")
    else:
        print("Gênero: " + filme['genero'])
        
    novo = input(f"Ano [{filme['ano_lancamento']}]: ").strip()
    if novo.isdigit(): filme["ano_lancamento"] = int(novo)
    novo = input(f"Duração [{filme['duracao']}]: ").strip()
    if novo:
        try:
            filme["duracao"] = float(novo)
        except ValueError:
            pass
    while True:
        try:
            novo = float(input(f"Nota pessoal [{filme['nota_pessoal']}]: "))
            if novo >= 0 and novo <= 10:
                filme["nota_pessoal"] = novo
                break
            else:
                print("A nota deve ser de 0 a 10!!!")
        except ValueError:
            print("Digite uma nota válida (número)!")

    if novo: 
        filme["nota_pessoal"] = novo
    escrever_arquivo("filmes.json", filmes)
    print("Filme editado com sucesso.")
    return filmes