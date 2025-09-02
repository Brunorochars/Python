def buscar_filme(filmes: list):
    print("\n===========| Buscar Filmes |===========\n")
    print("Preencha somente os filtros que deseja utilizar na busca. " \
          "Caso contrario aperte [ENTER] para pular:")
    titulo = input("Título (ou parte): ").lower().strip()
    diretor = input("Diretor (ou parte): ").lower().strip()
    genero = ""
    opcao_busca_genero = input("Deseja filtrar por gênero? (S/N): ").lower()
    if opcao_busca_genero == "s":
        while True:
                print("|=====================================|")
                print("|========== Gênero do Filme ==========|")
                print("|=====================================|")
                print("|                                     |")
                print("|1 - Curta                            |")
                print("|2 - Documentário                     |")
                print("|3 - Filme                            |")
                print("---------------------------------------\n")
                opcao = input("Selecione o gênero do filme: ")
                if opcao == "1":
                    genero = "curta"
                    break
                elif opcao == "2":
                    genero = "documentario"
                    break
                elif opcao == "3":
                    genero = "filme"
                    break
                else:
                    print("Opação inválida!!!")
    
    ano_min = input("Ano mínimo: ").strip()
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