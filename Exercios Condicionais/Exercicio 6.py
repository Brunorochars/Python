#  Escrever um programa que pede o peso e a altura de uma 
# pessoa e calcula o IMC (Índice de Massa Corporal). O pro
# grama deve informar o estado da pessoa em relação ao IMC 
# de acordo com as seguintes faixas:
# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 24.9: Peso normal
# - Entre 25 e 29.9: Acima do peso
# - Entre 30 e 34.9: Obesidade grau 1
# - Entre 35 e 39.9: Obesidade grau 2
# - Acima de 40: Obesidade grau 3

def calcular_imc(imc):

    if(imc < 18.5):
        return "abaixo do peso."
    elif(imc >= 18.5 and imc <= 29.9):
        return "acima do peso."
    elif(imc > 29.9 and imc <= 34.9):
        return "com obesidade grau 1."
    elif(imc > 34.9 and imc <= 39.9):
        return "com obesidade grau 2."
    else:
        return "com obesidade grau 3."
    
altura = float(input("Digite a sua altura: "))
peso = float(input("Digite o seu peso: "))

imc = peso / (altura * altura)


print (f"Com relação ao seu IMC, você está {calcular_imc(imc)}")