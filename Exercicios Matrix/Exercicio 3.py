n = int(input("Digite o número para verificar no vetor: "))
vetor = [ ]
contador = 0
i = 0
repetido =  0 


for i in range(5):

    elemento = int(input("Digite um número: "))
    vetor.append(elemento)
    i = i + 1

print(f"O número {repetido} repetiu {contador} vezes!")