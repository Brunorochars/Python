#   Escrever um programa de um banco que permite criar 
# contas: 
# =======================
# Cada conta deve ter:
#
# - Número da conta
# - Senha
# - Nome do titular
# - Saldo
# =======================
# O usuário de poder:
#
# - Criar conta
# - Logar na conta
# - Realizar transações
# - Visualizar saldo
# ========================
#   Usuários podem enviar dinheiro entre contas, e o programa deve 
# garantir que o saldo não fique negativo.
# =============================================================================

def criar_conta(numero_de_contas_existentes):

    nome_titular = input("Digite o seu nome: ")
    senha = input("Digite a sua senha: ")
    
    nova_conta = {

        "numero_conta": numero_de_contas_existentes + 1,
        "saldo":0,
        "nome_titular": nome_titular,
        "senha": senha,

    }

    return nova_conta

def fazer_login(contas_existentes):

    numero_conta =int(input("Digite o número da conta: "))
    senha = input("Digite a senha: ")

    for conta_existente in contas_existentes:

        if numero_conta == conta_existente["numero"] and senha == conta_existente["senha"]:
            return conta_existente

def main():

    contas = []

    while True:

        print("========== MENU ==========")
        print()
        print("1 - Criar conta") 
        print("2 - Depositar/Sacar") 
        print("3 - Sair")
   
        opcao_usuario = input("Digite a o opção desejada:")

        if opcao_usuario == "3":
            
            print()
            print("Até logo!!!")
            print()
            break 

        if opcao_usuario == "1":
            nova_conta = criar_conta(numero_de_contas_existentes=len(contas))
            contas.append(nova_conta)

        if opcao_usuario == "2":
            conta_usuario = None
            while conta_usuario is None:
                fazer_login(contas_existentes=contas) ## Passa a lista de contas para contas_existentes
        
main()

    





