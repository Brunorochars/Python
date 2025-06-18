# Escrever um programa que lê números inteiros e imprime a soma dos números positivos 
# e a quantidade de números negativos. O programa deve parar de ler números quando o 
# usuário digitar -1.

# Função para ler números do usuário até que -1 seja digitado
def ler_numeros():
    numeros = []
    while True:
        try:
            numero = int(input("Digite um número inteiro (-1 para sair): "))
            if numero == -1:
                break
            numeros.append(numero)
        except ValueError:
            print("Por favor, digite um número inteiro válido.")
    return numeros

# Função que calcula a soma dos números positivos
def soma_positivos(numeros):
    soma = sum(n for n in numeros if n > 0)
    return soma

# Função que conta quantos números negativos foram digitados
def contar_negativos(numeros):
    negativos = sum(1 for n in numeros if n < 0)
    return negativos

# Função principal que organiza o fluxo do programa
def main():
    # Lê os números digitados pelo usuário
    numeros = ler_numeros()
    
    # Calcula a soma dos positivos e a quantidade de negativos
    soma = soma_positivos(numeros)
    quantidade_negativos = contar_negativos(numeros)
    
    # Exibe os resultados
    print(f"Soma dos números positivos: {soma}")
    print(f"Quantidade de números negativos: {quantidade_negativos}")

# Chamada da função principal para iniciar o programa
if __name__ == "__main__":
    main()
