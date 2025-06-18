#  Escrever um programa que leia do usuário as dimensões "m" e "n" de uma matriz, receba m×n 
# valores reais e armazene-os em uma lista de listas.
#
# Na sequência, o programa deve identificar e exibir o maior e o menor valor da matriz, bem 
#como suas respectivas posições (linha e coluna de cada um desses dois valores).

# Função para ler a matriz do usuário
def ler_matriz(m, n):
    """
    Lê os elementos de uma matriz m x n (m linhas, n colunas) fornecidos pelo usuário.
    Retorna a matriz como uma lista de listas.
    """
    matriz = []  # Lista para armazenar a matriz

    print(f"\nDigite os {m * n} elementos da matriz ({m}x{n}):")

    for i in range(m):
        linha = []  # Lista para armazenar uma linha da matriz
        for j in range(n):
            # Lê um valor real (float) do usuário para cada posição
            valor = float(input(f"Elemento [{i}][{j}]: "))
            linha.append(valor)  # Adiciona o valor à linha
        matriz.append(linha)  # Adiciona a linha completa à matriz

    return matriz

# Função para encontrar o maior e o menor elemento da matriz, junto com suas posições
def encontrar_maior_menor(matriz):
    """
    Percorre a matriz para encontrar o maior e o menor valor, além de suas posições (linha e coluna).
    Retorna uma tupla com as informações.
    """
    # Inicializa as variáveis com o primeiro elemento da matriz
    maior = menor = matriz[0][0]
    pos_maior = pos_menor = (0, 0)  # Tuplas (linha, coluna)

    # Percorre toda a matriz
    for i in range(len(matriz)):          # Para cada linha
        for j in range(len(matriz[i])):   # Para cada coluna da linha
            valor = matriz[i][j]          # Valor atual da matriz

            # Verifica se encontrou um novo maior valor
            if valor > maior:
                maior = valor
                pos_maior = (i, j)  # Atualiza posição do maior

            # Verifica se encontrou um novo menor valor
            if valor < menor:
                menor = valor
                pos_menor = (i, j)  # Atualiza posição do menor

    return maior, pos_maior, menor, pos_menor

# Função principal
def main():
    """
    Função principal que coordena a execução do programa.
    """
    # Lê as dimensões da matriz
    m = int(input("Digite o número de linhas (m): "))
    n = int(input("Digite o número de colunas (n): "))

    # Lê a matriz do usuário
    matriz = ler_matriz(m, n)

    # Encontra o maior e o menor valor e suas posições
    maior, pos_maior, menor, pos_menor = encontrar_maior_menor(matriz)

    # Exibe os resultados
    print("\nResultado:")
    print(f"Maior valor: {maior} encontrado na posição (linha={pos_maior[0]}, coluna={pos_maior[1]})")
    print(f"Menor valor: {menor} encontrado na posição (linha={pos_menor[0]}, coluna={pos_menor[1]})")

# Executa o programa
if __name__ == "__main__":
    main()
