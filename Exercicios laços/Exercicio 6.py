# Escrever um programa que funciona como uma calculadora simples. A calculadora 
# deve ter um menu com as seguintes opções: (1) Adição, (2) Subtração, (3) Multiplicação, 
# (4) Divisão, (0) Sair. O usuário escolhe uma opção e insere dois números. O programa 
# executa a operação escolhida e exibe o resultado. O programa deve continuar até que o 
# usuário escolha a opção 0.

# Função que exibe o menu de opções da calculadora
def exibir_menu():
    print("\n===== CALCULADORA SIMPLES =====")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

# Função que solicita ao usuário dois números e os retorna
def ler_numeros():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        return num1, num2
    except ValueError:
        print("Entrada inválida. Use apenas números.")
        return ler_numeros()  # Repete a leitura em caso de erro

# Função que executa a operação escolhida pelo usuário
def executar_operacao(opcao, num1, num2):
    if opcao == 1:
        resultado = num1 + num2
        print(f"Resultado da adição: {resultado}")
    elif opcao == 2:
        resultado = num1 - num2
        print(f"Resultado da subtração: {resultado}")
    elif opcao == 3:
        resultado = num1 * num2
        print(f"Resultado da multiplicação: {resultado}")
    elif opcao == 4:
        if num2 != 0:
            resultado = num1 / num2
            print(f"Resultado da divisão: {resultado}")
        else:
            print("Erro: divisão por zero não é permitida.")
    else:
        print("Opção inválida.")

# Função principal que controla o fluxo do programa
def main():
    while True:  # Loop infinito até o usuário escolher sair
        exibir_menu()  # Mostra o menu
        try:
            opcao = int(input("Escolha uma opção: "))  # Lê a opção do usuário
        except ValueError:
            print("Por favor, digite uma opção válida (número inteiro).")
            continue  # Volta ao início do loop

        if opcao == 0:
            print("Encerrando a calculadora. Até logo!")
            break  # Sai do loop e encerra o programa

        if opcao in [1, 2, 3, 4]:  # Verifica se a opção é válida
            num1, num2 = ler_numeros()  # Lê os dois números
            executar_operacao(opcao, num1, num2)  # Executa a operação
        else:
            print("Opção inválida. Tente novamente.")  # Mensagem para opção fora do menu

# Ponto de entrada do programa
if __name__ == "__main__":
    main()  # Chamada da função principal
