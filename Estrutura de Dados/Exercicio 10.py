# Escrever um programa de um banco que permite criar 
# contas, depositar e sacar dinheiro. Cada conta deve 
# ter um número de conta, senha, nome do titular e 
# saldo. O usuário deve poder se logar em um conta, 
# realizar transações e visualizar o saldo. Usuários 
# podem enviar dinheiro entre contas, e o programa deve 
# garantir que o saldo não fique negativo.

def criar_contas():
    conta = {}

    conta["numero_conta"] = int(input("Digite o número da sua conta: "))
    conta["senha"] = input("Digite uma senha: ")
    conta["nome_titular"] = input("Digite o seu nome: ")
    conta["saldo"] = float(input("Digite o saldo: "))

    return conta

contas = []

conta_criada = criar_contas()

conta = {"numero_conta":""}
conta = {"senha":""}
conta = {"nome_titular":""}
conta = {"saldo": ""}

while conta["saldo"] < 0:
    
    





