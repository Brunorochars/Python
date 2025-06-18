# Escrever um programa que leia do usuário um valor "n" a ser o tamanho de uma matriz quadrada (n×n), 
# receba n×n valores inteiros e armazene-os em uma lista de listas.
# 
#  Em seguida, o programa deve:

#  1. Salvar a diagonal principal da matriz em uma lista separada.
#  2. Exibir os elementos da diagonal principal armazenados na lista separada.
#  3. Exibir a soma dos elementos da diagonal principal.

# Função para ler a matriz do usuário
def ler_matriz(n):
    """
    Lê os elementos de uma matriz n x n do usuário e retorna como uma lista de listas.
    """
    matriz = []  # Lista para armazenar a matriz
    print(f"Digite os {n * n} elementos da matriz ({n}x{n}):")
    
    for i in range(n):
        linha = []  # Lista para armazenar uma linha da matriz
        for j in range(n):
            valor = int(input(f"Elemento [{i}][{j}]: "))  # Lê um valor inteiro do usuário
            linha.append(valor)  # Adiciona o valor à linha
        matriz.append(linha)  # Adiciona a linha completa à matriz
    
    return matriz

# Função para obter a diagonal principal da matriz
def obter_diagonal_principal(matriz):
    """
    Retorna uma lista contendo os elementos da diagonal principal da matriz.
    """
    diagonal = []  # Lista para armazenar os elementos da diagonal principal
    for i in range(len(matriz)):
        diagonal.append(matriz[i][i])  # Elemento onde a linha e a coluna são iguais
    return diagonal

# Função principal do programa
def main():
    """
    Função principal que coordena a execução do programa.
    """
    # Lê o tamanho da matriz
    n = int(input("Digite o tamanho da matriz (n): "))

    # Lê a matriz do usuário
    matriz = ler_matriz(n)

    # Obtém a diagonal principal
    diagonal = obter_diagonal_principal(matriz)

    # Exibe os elementos da diagonal principal
    print("\nElementos da diagonal principal:")
    print(diagonal)

    # Calcula e exibe a soma dos elementos da diagonal principal
    soma_diagonal = sum(diagonal)  # Calcula a soma da lista diagonal
    print(f"\nSoma dos elementos da diagonal principal: {soma_diagonal}")

# Executa o programa
if __name__ == "__main__":
    main()
