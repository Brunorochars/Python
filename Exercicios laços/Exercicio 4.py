# Escrever um programa que lê números inteiros positivos e calcula: (i) a soma dos números 
# pares, (ii) o produto dos números ímpares, e (iii) a quantidade de números lidos. O programa 
# deve parar de ler números quando o usuário digitar 0.

# Função para ler números inteiros positivos até que o usuário digite 0
def ler_numeros():
    numeros = []  # Lista para armazenar os números digitados
    while True:  # Loop infinito até o usuário digitar 0
        try:
            # Solicita ao usuário que digite um número inteiro
            numero = int(input("Digite um número inteiro positivo (0 para encerrar): "))
            if numero < 0:
                # Se o número for negativo, mostra uma mensagem e continua o loop
                print("Por favor, digite apenas números positivos ou 0 para sair.")
                continue  # Volta ao início do loop
            if numero == 0:
                # Se o número for 0, encerra a leitura
                break
            # Adiciona o número à lista
            numeros.append(numero)
        except ValueError:
            # Se a entrada não for um número inteiro, exibe uma mensagem de erro
            print("Entrada inválida. Digite um número inteiro.")
    # Retorna a lista de números digitados
    return numeros

# Função para calcular a soma de números pares
def somar_pares(numeros):
    # Usa compreensão de lista para somar apenas os números pares
    return sum(n for n in numeros if n % 2 == 0)

# Função para calcular o produto de números ímpares
def produto_impares(numeros):
    produto = 1  # Inicializa o produto como 1
    tem_impar = False  # Variável para verificar se há ímpares
    for n in numeros:
        if n % 2 != 0:  # Se o número for ímpar
            produto *= n  # Multiplica ao produto
            tem_impar = True  # Marca que encontrou um ímpar
    # Retorna o produto, ou 0 se não houver ímpares
    return produto if tem_impar else 0

# Função principal que coordena o programa
def main():
    # Chama a função para ler os números digitados
    numeros = ler_numeros()
    
    # Chama a função que soma os números pares
    soma_pares = somar_pares(numeros)
    
    # Chama a função que calcula o produto dos ímpares
    produto_dos_impares = produto_impares(numeros)
    
    # Calcula a quantidade total de números digitados (sem contar o 0)
    quantidade_total = len(numeros)

    # Exibe os resultados
    print(f"Soma dos números pares: {soma_pares}")
    print(f"Produto dos números ímpares: {produto_dos_impares}")
    print(f"Quantidade de números lidos: {quantidade_total}")

# Ponto de entrada do programa
if __name__ == "__main__":
    main()  # Executa a função principal
