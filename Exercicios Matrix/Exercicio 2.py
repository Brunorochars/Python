n = int(input("Digite o número para verificar no vetor: "))
vetor = [ ]
contador = 0
i=0

for i in range(5):

    elemento = int(input("Digite um número: "))
    vetor.append(elemento)
    i = i + 1

    if elemento == n:
        contador = contador + 1 
    else:
        contador = contador


print(f"O número {n} repetiu {contador} vezes!")