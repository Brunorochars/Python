def criar_conta():
    usuario = {}
    usuario["Nome: "] = input("Digite o seu nome: ")
    usuario["idade: "] = int(input("Digite a sua idade: "))
    usuario["email: "] = input("Digite o seu email: ")

    return usuario

novo_usuario = criar_conta()
print(novo_usuario)
