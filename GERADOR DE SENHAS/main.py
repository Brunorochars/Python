from geracao_senhas import gerar_senhas


def menu():
    print("================ Menu ================")
    print()
    comprimento_senha = input("Defina o comprimento da senha: ")
    senha_possui_simbolos = input("A senha deve conter simbolos? (S/N): ")

    if senha_possui_simbolos == "S":
        senha_possui_simbolos = True
    else:
        senha_possui_simbolos = False