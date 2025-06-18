# Escrever um programa que defina uma matriz 3×3 (como lista de listas) com valores inteiros 
# fixos (isto é, não solicitar entrada do usuário) e imprima todos os elementos no formato de matriz.
#   
# Por exemplo, para a matriz: [[1, 2, 3], [4, 5, 6], [7, 8, 9]], a saída deve ser: 
#
# 1 2 3 
# 4 5 6 
# 7 8 9

# Função para criar e retornar a matriz 3x3 com valores fixos
def criar_matriz_fixa():
    """
    Cria e retorna uma matriz 3x3 com valores inteiros fixos.
    """
    matriz = [
        [1, 2, 3],  # Primeira linha da matriz
        [4, 5, 6],  # Segunda linha da matriz
        [7, 8, 9]   # Terceira linha da matriz
    ]
    return matriz  # Retorna a matriz criada

# Função para exibir a matriz no formato de matriz
def exibir_matriz(matriz):
    """
    Exibe os elementos da matriz no formato de linhas e colunas.
    """
    print("Matriz 3x3:")

    # Loop para percorrer cada linha da matriz
    for linha in matriz:
        # Loop para exibir cada elemento da linha
        for elemento in linha:
            print(f"{elemento:3}", end=" ")  # Exibe o elemento com formatação de espaço fixo
        print()  # Pula para a próxima linha após exibir uma linha completa

# Função principal que coordena a execução do programa
def main():
    """
    Função principal: cria a matriz e exibe o conteúdo.
    """
    matriz = criar_matriz_fixa()  # Cria a matriz fixa
    exibir_matriz(matriz)          # Exibe a matriz

# Executa o programa
if __name__ == "__main__":
    main()
