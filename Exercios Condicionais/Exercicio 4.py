# Exercício 04: Escrever um programa que recebe a idade de uma 
# pessoa e informa se ela é criança, adolescente, adulto ou idoso, 
# de acordo com as seguintes faixas etárias:
# - Criança: 0 a 12 anos
# - Adolescente: 13 a 17 anos
# - Adulto: 18 a 59 anos
# - Idoso: 60 anos ou mais


def faixa_etaria(idade):
    if(idade <= 12):
        return "Criança"
    elif(idade > 12 and idade < 18):
        return "Adolescente"
    elif(idade > 17 and idade < 60):
        return "Adulto"
    else:
        return "Idoso"
    
idade = int(input("Digite a sua idade: "))
print(f"A sua faixa etária é: {faixa_etaria(idade)}")