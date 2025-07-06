"""

Este é o trabalho final da disciplina de Algoritmos e Programação.

Você deve desenvolver um programa em Python que implemente as funcionalidades descritas abaixo.

O trabalho deve ser realizado individualmente e os artefatos (código-fonte, apresentação, etc.) devem ser entregues até o dia 16/07/2025 às 18h no Moodle da disciplina.

A avaliação consistirá na análise do código, execução do programa e apresentação oral, que deve durar entre 5 e 10 minutos. Durante a apresentação, os professores da disciplina poderão fazer perguntas sobre o código e o funcionamento do programa para avaliar o entendimento do aluno sobre a implementação.


Abaixo está uma descrição do projeto a ser desenvolvido.


“IndieFlix” – Catálogo de filmes independentes

Crie um sistema que permita ao usuário gerenciar um acervo pessoal de curtas, documentários e filmes independentes.

A tela inicial do programa deve exibir um menu com as seguintes opções:

1. Listar filmes

2. Adicionar filme

3. Editar filme

4. Remover filme

5. Buscar filme

6. Sair

O programa deve ser modularizado em três arquivos:

•⁠ menu.py: responsável pela interface do usuário e navegação.

•⁠ catalogo.py: contém a lógica de manipulação dos filmes (adicionar, editar, remover, listar).

•⁠ busca.py: implementa a busca e filtragem de filmes.

O programa deve permitir que o usuário informe, para cada filme, os seguintes dados:

•⁠ Título

•⁠ Diretor

•⁠ Ano de lançamento

•⁠ Gênero

•⁠ Duração

•⁠ Nota pessoal

O usuário deve poder buscar filmes por título, diretor e ano de lançamento, com suporte a filtros combinados (por exemplo, gênero = “documentário” AND ano ≥ 2018). Além disso, deve ser possível ordenar os resultados por ano de lançamento.

Os dados dos filmes devem ser armazenados em um arquivo JSON, permitindo persistência entre execuções do programa.

"""
import catalogo
import busca

def main():
    filmes = catalogo.ler_arquivo("filmes.json")
    
    while True:
        print("======================================")
        print("============ Indie Flix ==============")
        print("======================================")
        print("")
        print("Bem vindo ao Indie Flix!!!")
        print("Escolha uma opção: ")
        print("")
        print("1. Listar Filmes")
        print("2. Adicionar Filme")
        print("3. Editar Filme")
        print("4. Remover Filme")
        print("5. Buscar Filme")
        print("6. Sair")
        print("")

        opcao_usuario = input("Escolha a opção desejada de 1 a 6: ")

        if opcao_usuario == "1":
            catalogo.listar_filmes(filmes)
        elif opcao_usuario == "2":
           filmes = catalogo.adicionar_filme(filmes=filmes)
        elif opcao_usuario == "3":
            ...
        elif opcao_usuario == "4":
            filmes = catalogo.remover_filme(filmes=filmes)
        elif opcao_usuario == "5":
            filmes = busca.buscar_filme(filmes=filmes)
        elif opcao_usuario == "6":
            print("\n\n")
            print("Até logo!!!!")
            break

main()