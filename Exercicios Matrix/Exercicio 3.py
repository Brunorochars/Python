# Escrever um programa que receba um vetor conte quantas vezes cada 
# elemento aparece no vetor, exibindo o resultado.

# Função para ler o vetor do usuário
def ler_vetor():
    """
    Lê os elementos de um vetor de inteiros fornecidos pelo usuário.
    O usuário deve digitar os elementos separados por espaço.
    
    Retorna:
    - Uma lista contendo os elementos inteiros do vetor.
    """
    entrada = input("Digite os elementos do vetor separados por espaço: ")
    
    # Converte a entrada em uma lista de inteiros
    vetor = list(map(int, entrada.split()))
    
    return vetor

# Função para contar a frequência de cada elemento no vetor
def contar_frequencias(vetor):
    """
    Conta quantas vezes cada elemento aparece no vetor.
    
    Parâmetro:
    - vetor: lista de inteiros
    
    Retorna:
    - Um dicionário onde as chaves são os elementos e os valores são as quantidades de vezes que aparecem.
    """
    frequencias = {}  # Dicionário para armazenar as contagens

    # Percorre cada elemento do vetor
    for elemento in vetor:
        if elemento in frequencias:
            frequencias[elemento] += 1  # Incrementa o contador se o elemento já estiver no dicionário
        else:
            frequencias[elemento] = 1   # Adiciona o elemento no dicionário com contagem inicial 1

    return frequencias

# Função para exibir o resultado das frequências
def exibir_frequencias(frequencias):
    """
    Exibe quantas vezes cada elemento aparece no vetor.
    
    Parâmetro:
    - frequencias: dicionário com elementos e suas quantidades.
    """
    print("\nFrequência dos elementos no vetor:")

    # Percorre o dicionário de frequências
    for elemento, quantidade in frequencias.items():
        if quantidade == 1:
            print(f"{elemento} aparece 1 vez.")
        else:
            print(f"{elemento} aparece {quantidade} vezes.")

# Função principal que organiza a execução do programa
def main():
    """
    Função principal: lê o vetor, conta as frequências e exibe o resultado.
    """
    vetor = ler_vetor()  # Lê o vetor do usuário
    frequencias = contar_frequencias(vetor)  # Conta as frequências
    exibir_frequencias(frequencias)  # Exibe os resultados

# Executa o programa
if __name__ == "__main__":
    main()
