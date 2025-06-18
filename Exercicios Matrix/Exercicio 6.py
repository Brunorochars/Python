#   Escrever um programa que leia do usuário as dimensões "m" e "n" de uma matriz, 
# receba m×n valores inteiros e armazene-os em uma lista de listas, e então exiba 
# a matriz formatada.

# Função para ler a matriz do usuário
def ler_matriz(m, n):
    """
    Lê os elementos de uma matriz m x n (m linhas, n colunas) fornecidos pelo usuário.
    Retorna a matriz como uma lista de listas.
    """
    matriz = []  # Lista para armazenar a matriz

    print(f"\nDigite os {m * n} elementos inteiros da matriz ({m}x{n}):")

    # Loop para ler cada linha da matriz
    for i in range(m):
        linha = []  # Lista para armazenar os elementos da linha atual
        for j in range(n):
            # Lê um valor inteiro do usuário para a posição [i][j]
            valor = int(input(f"Elemento [{i}][{j}]: "))
            linha.append(valor)  # Adiciona o valor à linha
        matriz.append(linha)  # Adiciona a linha completa à matriz

    return matriz  # Retorna a matriz preenchida

# Função para exibir a matriz formatada
def exibir_matriz(matriz):
    """
    Exibe a matriz de forma formatada, com os elementos organizados em linhas e colunas.
    """
    print("\nMatriz formatada:")

    # Loop para percorrer cada linha da matriz
    for linha in matriz:
        # Exibe os elementos da linha separados por espaço
        for elemento in linha:
            print(f"{elemento:5}", end=" ")  # Formatação com espaçamento fixo
        print()  # Pula para a próxima linha após cada linha da matriz

# Função principal
def main():
    """
    Função principal que coordena a execução do programa.
    """
    # Lê as dimensões da matriz
    m = int(input("Digite o número de linhas (m): "))
    n = int(input("Digite o número de colunas (n): "))

    # Lê os elementos da matriz
    matriz = ler_matriz(m, n)

    # Exibe a matriz formatada
    exibir_matriz(matriz)

# Executa o programa
if __name__ == "__main__":
    main()
