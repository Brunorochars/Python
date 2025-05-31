#Escrever um programa que lê o valor de um produto e a 
# quantidade comprada e exibe o valor total a ser pago 
# com desconto de acordo com a quantidade comprada, con
# siderando as seguintes regras:
# - Quantidade até 10 unidades: sem desconto
# - Quantidade de 11 a 20 unidades: 10% de desconto
# - Quantidade acima de 20 unidades: 20% de desconto

def calcular_valor_total(quantidade):

    if(quantidade <= 10):
        return valor * quantidade
    elif(quantidade > 10 and quantidade <= 20):
        total = valor * quantidade
        return total - (total * 0.1)
    else:
        total = valor * quantidade
        return total - (total * 0.2)


valor = float(input("Digite o valor: "))
quantidade = int(input("Digite a guantidade: "))

print(f"O valor total é: {calcular_valor_total(quantidade)}")



