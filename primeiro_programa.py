
## nome = input("Escreva o seu nome: ") f(x) x é o argumento -- f(x)=x² é a função.
## Algumas funções tem restrições.
## Python 3 interpretador traduz o código python para binários.
## Compilada - mais rápida em execução.
## Interpretada - sintaxe mais alto nível, construir mais em menos tempo.

## identação usa para aninhar laços 
## Alt + Shift + a para comentar bloco do código

""" nome = "Bruno"
print (nome) """

""" def minha_func(numUm, numDois): ## numUm e numDois são parametros --- minha_func é a função
    print (numUm)
    print(numDois)
    return numUm + numDois

resultado = minha_func(3,5) ## 3 e 5 são os argumentos passado para a função minha_func
print(resultado)            ## A variavel resultado recebe os argumentos da função minha_func """

""" nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

print(f"Olá, {nome}! Você tem {idade} anos!")

altura = float(input("Digite a sua altura (em metros): "))
peso = float(input("Digite o seu peso (Em Kg): "))
altura_em_cm = altura * 100 """



""" print(f"Sua altura é {altura_em_cm} metros e seu peso é {peso} quilogramas") """

## Exercicio 00

""" numero = float(input("Digite um número: "))
numero_dois = float(input("Digite outro número: "))

print(f"A soma do dois números é: {numero + numero_dois}") """

## Exercicio 01

""" numero = int(input("Digite um número: "))
numero_dois = int(input("Digite outro número: "))

print(f"Soma: {numero + numero_dois}, Subtração: {numero - numero_dois}, Multiplicação: {numero * numero_dois}, Divisão: {numero / numero_dois}") """

## Exercicio 02

""" numero = int(input("Digite um número: "))
numero_dois = int(input("Digite outro número: "))

if(numero > numero_dois):
    maior = numero
else:
    maior = numero_dois

print(f"O numero maior é: {maior}") """

## Exercicio 03

""" salario = float(input("Digite o seu salário: "))

print(f"O seu salário com aumento ficou: {salario + (salario * 0.15)}") """

## Exercicio 04

""" soma = 0

for i in range(3):
    nota = int(input("Digite a nota: "))
    soma = nota + soma
print(f"Sua média é: {soma/3}") """

## Exercicio 05

""" valor_total = float(input("Digigite o valor total dos produtos: "))
porcentagem_gorjeta = float(input("Digite a porcentagem da gorjeta: "))

print(f"Valor da gorjeta é: {valor_total*(porcentagem_gorjeta/100)}") """

## Exercicio 06

""" idade = int(input(" Digite a sua idade: "))

if(idade >= 18):
    print("Você é maior de idade!!!")
else:
    print("Você é menor de idade!!!") """

## Exercicio 07

""" num = int(input("Digite um número: "))

if(num % 2 == 0):
    print("O número é par!!")
else:
    print("O número é ímpar!!") """

## If com valor booleano

""" casado = True

if casado:
    print("É casado!")
else:
    print("Não é casado!") """

## Utilizando função

""" def eh_par(num):
    return num % 2 == 0

num = int(input("Digite um número: "))

print(f"O número {num} é par?? {eh_par(num)}") """

# Exercício 01: Escrever um programa que recebe três números e informa qual
# é o maior deles. Se os três números forem iguais, o programa deve informar 
# que todos são iguais.

""" i = 1
maior = 0

for i in range(3):

    numero = int(input("Digite o número: "))
    
    if(numero > maior):
        maior = numero
    else:
        maior = maior

print(f"O número maior é: {maior}") """


# Exercício 02: Escrever um programa que pede uma temperatura e a unidade de 
# medida (Celsius ou Fahrenheit) e converte a temperatura para a outra unidade. 
# O programa deve informar a temperatura convertida.

""" unidade = int(input("Escolha a unidade: \n 1 - Celsius \n 2 - Fahrenheit \n Digite a opção: "))

temperatura = int(input("Digite a temperatura: "))

if(unidade == 1):
    fahrenheit = (9/5*temperatura) + 32
    print(f"A temperatura {temperatura} C° convertida para Fahrenheit é {fahrenheit} F°!!! ")
else:
    celcius = (temperatura - 32) * 5/9
    print(f"A temperatura {temperatura} F° convertida para Celcius é {celcius} C°!!! ") """

# Exercício 03: Escrever um programa que recebe a nota de um aluno e informa se ele 
# foi aprovado, reprovado ou se está de recuperação. Considere as seguintes regras:
# - Nota maior ou igual a 7: Aprovado
# - Nota menor que 7 e maior ou igual a 5: Recuperação
# - Nota menor que 5: Reprovado 


nota = float(input("Digite a sua nota: "))
    
if(nota >= 7):
    print("Aprovado!!!")
elif(nota < 7 and nota >= 5):
    print("Recuperação!!!")
else:
    print("Reprovado!!!")


    
   




