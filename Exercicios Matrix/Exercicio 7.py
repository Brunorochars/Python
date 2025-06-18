#   Escrever um programa que leia do usuário as dimensões "m" e "n" de uma matriz, receba 
# m×n valores inteiros e armazene-os em uma lista de listas.  Na sequência, o programa 
# pedir ao usuário um valor inteiro correspondente a uma das linhas da matriz. Por fim, 
# o programa deve exibir todos os elementos (colunas) e a soma dos elementos dessa linha.

# Função para ler a matriz do usuário
def ler_matriz(m, n):
    """
    Lê os elementos de uma matriz m x n (m linhas, n colunas) fornecidos pelo usuário.
    Retorna a matriz como uma lista de listas.
    """
    matriz = []  # Lista para armazenar a matriz

    print(f"\nDigite os {m * n} elementos inteiros da matriz ({m}x{n}):")

    for i in range(m):
        linha = []  # Lista para armazenar os elementos da linha atual
        for j in range(n):
            # Lê um valor inteiro do usuário para a posição [i][j]
            valor = int(input(f"Elemento [{i}][{j}]: "))
            linha.append(valor)  # Adiciona o valor à linha
        matriz.append(linha)  # Adiciona a linha completa à matriz

    return matriz  # Retorna a matriz preenchida

# Função para exibir uma linha específica da matriz e sua soma
def exibir_linha_e_soma(matriz, linha_escolhida):
    """
    Exibe os elementos da linha escolhida da matriz e calcula a soma desses elementos.
    """
    # Verifica se a linha escolhida é válida
    if linha_escolhida < 0 or linha_escolhida >= len(matriz):
        print("\nNúmero de linha inválido!")
        return

    linha = matriz[linha_escolhida]  # Obtém a linha escolhida

    print(f"\nElementos da linha {linha_escolhida}: {linha}")

    soma = sum(linha)  # Calcula a soma dos elementos da linha

    print(f"Soma dos elementos da linha {linha_escolhida}: {soma}")

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

    # Solicita ao usuário o número da linha que deseja consultar
    linha_escolhida = int(input(f"\nDigite o número da linha que deseja visualizar (0 a {m - 1}): "))

    # Exibe a linha escolhida e sua soma
    exibir_linha_e_soma(matriz, linha_escolhida)

# Executa o programa
if __name__ == "__main__":
    main()
