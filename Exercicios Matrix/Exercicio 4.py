# Escrever um programa que receba dois vetores de mesmo tamanho e calcule o 
# produto escalar entre eles, exibindo o valor obtido.

# Função para ler um vetor do usuário
def ler_vetor(tamanho, numero_vetor):
    """
    Lê um vetor de inteiros do usuário.
    
    Parâmetros:
    - tamanho: número de elementos do vetor
    - numero_vetor: identificação do vetor (1º ou 2º) para exibir nas mensagens
    
    Retorna:
    - Lista contendo os elementos do vetor
    """
    vetor = []  # Cria uma lista vazia para armazenar os elementos

    print(f"\nDigite os {tamanho} elementos do vetor {numero_vetor}:")
    for i in range(tamanho):
        valor = int(input(f"Elemento {i}: "))  # Lê cada valor do vetor
        vetor.append(valor)  # Adiciona o valor à lista

    return vetor  # Retorna o vetor preenchido

# Função para calcular o produto escalar entre dois vetores
def calcular_produto_escalar(vetor1, vetor2):
    """
    Calcula o produto escalar entre dois vetores.
    
    Parâmetros:
    - vetor1: primeiro vetor (lista de inteiros)
    - vetor2: segundo vetor (lista de inteiros)
    
    Retorna:
    - O produto escalar (soma dos produtos dos elementos correspondentes)
    """
    produto = 0  # Variável para acumular a soma

    # Percorre os dois vetores ao mesmo tempo
    for i in range(len(vetor1)):
        produto += vetor1[i] * vetor2[i]  # Multiplica os elementos correspondentes e soma ao total

    return produto  # Retorna o produto escalar

# Função principal que coordena a execução do programa
def main():
    """
    Função principal do programa: lê os vetores, calcula e exibe o produto escalar.
    """
    # Lê o tamanho dos vetores
    tamanho = int(input("Digite o tamanho dos vetores: "))

    # Lê os dois vetores do usuário
    vetor1 = ler_vetor(tamanho, 1)
    vetor2 = ler_vetor(tamanho, 2)

    # Calcula o produto escalar
    resultado = calcular_produto_escalar(vetor1, vetor2)

    # Exibe o resultado
    print(f"\nO produto escalar entre os vetores é: {resultado}")

# Executa o programa
if __name__ == "__main__":
    main()
