#  Escrever um programa que recebe o salário de um funcionário e 
# calcula o valor do aumento salarial, de acordo com as seguintes 
# regras:
# - Salário até R$ 1.000,00: aumento de 20%
# - Salário entre R$ 1.000,01 e R$ 2.000,00: aumento de 15%
# - Salário entre R$ 2.000,01 e R$ 3.000,00: aumento de 10%
# - Salário acima de R$ 3.000,00: aumento de 5%

def calcular_aumento_salario(salario):
    if(salario <= 1000):
        salario = salario + (salario * 0.2)
        return salario
    elif(salario > 1000 and salario <= 2000):
        salario = salario + (salario * 0.15)
        return salario
    elif(salario > 2000 and salario <= 3000):
        return salario + (salario * 0.1)
    else:
        return salario + (salario * 0.05)

salario = float(input("Digite o seu salário: "))

print(f"O seu salário com o aumento ficará R$ {calcular_aumento_salario(salario)}")
