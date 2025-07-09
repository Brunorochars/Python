def buscar_filme(filmes: list):
    print("\n===========| Buscar Filmes |===========\n")
    print("Informe o Título ou aperte enter para passar:")
    titulo = input("Título (ou parte): ").lower().strip()
    print("Informe o Diretor ou aperte enter para passar:")
    diretor = input("Diretor (ou parte): ").lower().strip()
    print("Informe o Gênero ou aperte enter para passar:")
    genero = input("Gênero: ").lower().strip()
    print("Informe o Ano Mínimo ou aperte enter para passar:")
    ano_min = input("Ano mínimo: ").strip()
    print("Informe o Ano Mínimo ou aperte enter para passar:")
    ano_max = input("Ano máximo: ").strip()
    ordenar = input("Ordenar por ano? (s/n): ").lower().strip() == "s"
    resultados = []
    for filme in filmes:
        if titulo and titulo not in filme["titulo"].lower():
            continue
        if diretor and diretor not in filme["diretor"].lower():
            continue
        if genero and genero not in filme["genero"].lower():
            continue
        if ano_min and filme["ano_lancamento"] < int(ano_min):
            continue
        if ano_max and filme["ano_lancamento"] > int(ano_max):
            continue
        resultados.append(filme)
    if ordenar:
        resultados.sort(key=lambda x: x["ano_lancamento"])
    print("\n===========| Resultados |===========")
    if not resultados:
        print("Nenhum filme encontrado.")
    else:
        for filme in resultados:
            print(f"[{filme['id']}] {filme['titulo']} | {filme['diretor']} | {filme['ano_lancamento']} | {filme['genero']} | {filme['duracao']} min | Nota: {filme['nota_pessoal']}")