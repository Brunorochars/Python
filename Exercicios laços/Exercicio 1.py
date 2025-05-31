# Escrever um programa que lê um inteiro positivo n e 
# calcula a soma de 1 + 2 + … + n usando for. Ao final, 
# mostrar o valor total

i = 1
soma = 0
numero = int(input("Digite um número inteiro: "))


for i in range(numero):
    soma = soma + i
    i = i + 1

print(f"Resultado da soma: {soma}")

