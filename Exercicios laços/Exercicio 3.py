# Escrever um programa que lê números inteiros positivos e calcula 
# a média desses números. O programa deve parar de ler números 
# quando o usuário digitar 0.


contador = -1
numero = 1
soma = 0

while (numero != 0):

    numero = int(input("Digite o número: "))
    soma = soma + numero
    contador = contador + 1

print(f"A média é: {soma/contador}")

