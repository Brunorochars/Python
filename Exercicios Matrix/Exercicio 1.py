#n = int(input("Digite o tamanho do vetor: "))
vetor = [ ]

maior = 0
menor = 999
i=0
soma = 0

for i in range(5):
    elemento = int(input("Digite um número: "))
    vetor.append(elemento)
    i = i + 1
    soma = soma + elemento
    if elemento > maior:
        maior = elemento
    if elemento < menor:
        menor = elemento    

print(f"Maior: {maior}")
print(f"Menor: {menor}")
print(f"Soma: {soma}")
print (f"Média: {soma/5}")