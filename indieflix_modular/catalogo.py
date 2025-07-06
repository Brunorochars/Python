import json

def ler_arquivo(nome_arquivo: str):
    
    with open(nome_arquivo, "r", encoding="utf-8") as leitor:
        return json.load(leitor)
    

def escrever_arquivo(nome_arquivo: str, filmes: list):
    with open(nome_arquivo, "w", encoding="utf-8") as escritor:
        json.dump(filmes, escritor, indent=4)

def adicionar_filme(filmes: list):
    titulo = input("Digite o título do filme: ")
    diretor = input("Digite o nome do diretor: ")
    while True:
        try:
            ano_lancamento = int(input("Digite o ano de lançamento (AAAA): "))
            break
        except ValueError:
            print("Ano inválido.")
    genero = input("Digite o gênero do filme: ")
    while True:
        try:
            duracao = float(input("Digite a duração do filme (minutos): "))
            break
        except ValueError:
            print("Duração inválida.")
    nota_pessoal = input("Nota pessoal: ")
    novo_filme = {
        "id": filmes[-1]["id"] + 1 if filmes else 1,
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
    print("\n==============================| Lista de Filmes |==============================")
    if not filmes:
        print("Nenhum filme cadastrado.")
    for filme in filmes:
        print(f"|[{filme['id']}] {filme['titulo']} | {filme['diretor']} | {filme['ano_lancamento']} | {filme['genero']} | {filme['duracao']} min | Nota: {filme['nota_pessoal']}|")

def remover_filme(filmes: list):
    listar_filmes(filmes)
    try:
        id_remover = int(input("\nID do filme a remover: "))
    except ValueError:
        print("ID inválido.")
        return filmes
    filme = next((f for f in filmes if f["id"] == id_remover), None)
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
    try:
        id_editar = int(input("\nID do filme a editar: "))
    except ValueError:
        print("ID inválido.")
        return filmes
    filme = next((f for f in filmes if f["id"] == id_editar), None)
    if not filme:
        print("Filme não encontrado.")
        return filmes
    print("Pressione Enter para manter o valor atual.")
    novo = input(f"Título [{filme['titulo']}]: ").strip()
    if novo: filme["titulo"] = novo
    novo = input(f"Diretor [{filme['diretor']}]: ").strip()
    if novo: filme["diretor"] = novo
    novo = input(f"Gênero [{filme['genero']}]: ").strip()
    if novo: filme["genero"] = novo
    novo = input(f"Ano [{filme['ano_lancamento']}]: ").strip()
    if novo.isdigit(): filme["ano_lancamento"] = int(novo)
    novo = input(f"Duração [{filme['duracao']}]: ").strip()
    if novo:
        try:
            filme["duracao"] = float(novo)
        except ValueError:
            pass
    novo = input(f"Nota pessoal [{filme['nota_pessoal']}]: ").strip()
    if novo: filme["nota_pessoal"] = novo
    escrever_arquivo("filmes.json", filmes)
    print("Filme editado com sucesso.")
    return filmes