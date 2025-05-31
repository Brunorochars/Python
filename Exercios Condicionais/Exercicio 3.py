# Exercício 03: Escrever um programa que recebe a nota de um aluno e informa se ele 
# foi aprovado, reprovado ou se está de recuperação. Considere as seguintes regras:
# - Nota maior ou igual a 7: Aprovado
# - Nota menor que 7 e maior ou igual a 5: Recuperação
# - Nota menor que 5: Reprovado 

def calcular_status_aluno(nota):
    if(nota >= 7):
        return "Aprovado!!!"
    elif(nota < 7 and nota >= 5):
        return "Recuperação!!!"
    else:
        return "Reprovado!!!"

nota = float(input("Digite a sua nota: "))
print(f"O status do aluno é : {calcular_status_aluno(nota)}")