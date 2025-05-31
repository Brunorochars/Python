# Exercício 01: Escrever um programa que recebe três números e informa qual
# é o maior deles. Se os três números forem iguais, o programa deve informar 
# que todos são iguais.

maior = -float("inf") # Infinito negativo
anterior = 0
iguais = 0

for i in range(3):
    numero = int(input("Digite um número: "))
    if(numero > maior):
        maior = numero
    elif(numero == maior):
        iguais = iguais + 1
    else:
        maior = maior

if(iguais == 2):
    print("Todos são iguais!!!")
else:
    print(f"O maior número é {maior}!!!")