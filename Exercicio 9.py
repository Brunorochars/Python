#   Crie um programa que possua um menu com as opções "1 - Soma", "2 - Subtração", 
# "3 - Multiplicação", "4 - Divisão" e "5 - Sair", e leia a opção escolhida pelo 
# usuário e dois números inteiros, e exiba o resultado da operação escolhida. O 
# menu deve ser exibido até que o usuário escolha a opção "5 - Sair". A interação 
# com o menu deve ser feita usando chamadas de função.


opcao = int(input("----------- MENU-----------\n" \
                  "|Digite a opção desejada:  |\n" \
                  "|1 - Soma                  |\n" \
                  "|2 - Subtração             |\n" \
                  "|3 - Multiplicação         |\n" \
                  "|4 - Divisão               |\n" \
                  "|5 - SAIR                  |\n" \
                  "----------------------------\n" \
                  "Opção: "))

primeiro_numero = int(input("Digite o priemiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

if(opcao == 1):
    print(f"A soma dos dois número é {primeiro_numero + segundo_numero}!!!")
elif(opcao == 2):
    print(f"A soma dos dois número é {primeiro_numero - segundo_numero}!!!")
elif(opcao == 3):
    print(f"A soma dos dois número é {primeiro_numero * segundo_numero}!!!")
elif(opcao == 4):
    print(f"A soma dos dois número é {primeiro_numero / segundo_numero}!!!")
elif(opcao == 5):
    print("Você saiu!!!")
else:
    print("Número inválido!!!")


