"""Exercício 01: Escrever um programa que lê nomes até que o usuário digite sair. Ao 
final, o programa deve exibir: (i) o número total de nomes lidos e (ii) a lista 
completa de nomes."""

def criar_usuario():
    
    usuario =  {} #Cria um dicionario vazio
    usuario["nome"] = input("Digite o nome: ") #Recebe o nome do usuario digitado pelo usuario

    return usuario #Retorna o nome digitado

usuarios = [] #Cria uma lista vazia de usuarios

total_nomes = 0 #Inicializa a variavel que contara o número de usuarios digitados

#   Nós estamos manipulando um dicionario inteiro no nosso while, precisamos declarar
# esse dicionario inteiro, para usarmos ele no while desde a primeira iteração.
#   A chave do dicionario que usamos no while é chave nome, então o nosso dicionário
# original precisa ter a chave nome, com um valor que o while entre na primeira vez.

usuario = {"nome": ""} 

while usuario["nome"].upper() != "SAIR": #upper() torna o nome digitado, todo em maiusculo
    
    usuario = criar_usuario()
    if usuario["nome"].upper() != "SAIR":

        usuarios.append(usuario)
        total_nomes = total_nomes + 1

print(usuarios)
print(total_nomes)








