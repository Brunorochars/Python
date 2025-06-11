#   Exercício 02: Escrever um programa que guarda notas (0-10)
# em lista até o usuário digitar "sair". Ao final, o programa 
# deve exibir: (i) o número total de notas lidas, (ii) a lista 
# completa de notas, (iii) a maior nota, (iv) a menor nota.

def criar_nota():

    aluno = {}
    aluno["nota"] = int(input("Digite a nota: "))

    return aluno

alunos = []

total_nota = 0
maior_nota = 0
menor_nota = 999


aluno = {"nota":""}

while aluno["nota"] != "SAIR":

    aluno = criar_nota()
    if aluno["nota"] > maior_nota:
        maior_nota = aluno["nota"]
        alunos.append(aluno)
    else:
        menor_nota = aluno["nota"]
        alunos.append(aluno)

print(alunos)
print(menor_nota)
print(maior_nota)
print(total_nota)