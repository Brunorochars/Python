#Escrever um programa que recebe uma lista de produtos. Cada produto deve ter um nome 
# e um preço. O programa deve pedir informações de cada produto até que o usuário digite 
# "sair". Ao final, o programa deve exibir: (i) o número total de produtos cadastrados, 
# (ii) a lista completa de produtos, (iii) o produto mais barato, (iv) o produto mais 
# caro e (iv) o preço médio dos produtos.


# Função para ler os produtos até o usuário digitar "sair"
def ler_produtos():
    produtos = []  # Cria uma lista vazia para armazenar os produtos

    while True:  # Início de um loop que continua indefinidamente
        # Solicita ao usuário o nome do produto
        nome = input("Digite o nome do produto (ou 'sair' para encerrar): ").strip()

        if nome.lower() == "sair":  # Se o usuário digitar "sair", encerra o loop
            break

        try:
            # Solicita o preço do produto (convertendo a entrada para float)
            preco = float(input(f"Digite o preço do produto '{nome}': "))

            if preco < 0:  # Verifica se o preço é negativo
                print("O preço não pode ser negativo. Tente novamente.")
                continue  # Volta ao início do loop para pedir novamente

            # Adiciona um dicionário com nome e preço à lista de produtos
            produtos.append({"nome": nome, "preco": preco})

        except ValueError:
            # Trata erros se o usuário digitar algo que não seja número
            print("Preço inválido. Por favor, digite um número válido.")

    # Retorna a lista de produtos para ser usada em outras funções
    return produtos

# Função para exibir o relatório final dos produtos cadastrados
def exibir_relatorio(produtos):
    if not produtos:  # Se a lista estiver vazia
        print("Nenhum produto foi cadastrado.")  # Mensagem de aviso
        return  # Encerra a função

    total = len(produtos)  # Conta quantos produtos foram cadastrados

    # Encontra o produto mais barato usando a função min()
    mais_barato = min(produtos, key=lambda p: p["preco"])

    # Encontra o produto mais caro usando a função max()
    mais_caro = max(produtos, key=lambda p: p["preco"])

    # Calcula a soma total dos preços
    soma_precos = sum(p["preco"] for p in produtos)

    # Calcula o preço médio dos produtos
    media = soma_precos / total

    # Imprime o relatório com os resultados
    print("\n===== RELATÓRIO DE PRODUTOS =====")
    print(f"Total de produtos cadastrados: {total}")

    print("\nLista de produtos:")
    for p in produtos:  # Percorre a lista e imprime cada produto
        print(f"- {p['nome']}: R$ {p['preco']:.2f}")

    # Exibe o produto mais barato
    print(f"\nProduto mais barato: {mais_barato['nome']} (R$ {mais_barato['preco']:.2f})")

    # Exibe o produto mais caro
    print(f"Produto mais caro: {mais_caro['nome']} (R$ {mais_caro['preco']:.2f})")

    # Exibe o preço médio
    print(f"Preço médio dos produtos: R$ {media:.2f}")

# Função principal que organiza o fluxo do programa
def main():
    produtos = ler_produtos()  # Chama a função para ler os produtos
    exibir_relatorio(produtos)  # Chama a função para exibir o relatório final

# Ponto de entrada do programa: executa main() apenas se o script for executado diretamente
if __name__ == "__main__":
    main()  # Inicia a execução do programa
