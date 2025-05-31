# Exercício 02: Escrever um programa que pede uma temperatura e a unidade de 
# medida (Celsius ou Fahrenheit) e converte a temperatura para a outra unidade. 
# O programa deve informar a temperatura convertida.

def converter_temperatura(temperatura):
    if(unidade_original == "C"):
        fahrenheit = (9/5*temperatura) + 32
        return round(fahrenheit, 2)
    elif(unidade_original == "F"):
        celcius = (temperatura - 32) * 5/9
        return round(celcius, 2)
    else:
        print("Opção inválida!!!")

unidade_original = input("Escolha a unidade: \n C - Celsius \n F - Fahrenheit \n Digite a opção: ")
temperatura = float(input("Digite a temperatura: "))
unidade_convertida =  "F" if unidade_original == "C" else "C"

print(f"A temperatura convertida é: {converter_temperatura(temperatura)} {unidade_convertida}°")