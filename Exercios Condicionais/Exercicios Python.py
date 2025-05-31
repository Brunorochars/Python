atividade_A = int(input("Informe os dias para a atividade A: "))
atividade_B = int(input("Informe os dias para a atividade B: "))
atividade_C = int(input("Informe os dias para a atividade C: "))

if atividade_A < 0 or atividade_B < 0 or atividade_C < 0:
    print("Erro: Os dias não podem ser negativos.")
else:
    tempo_total = atividade_A + atividade_B + atividade_C
    print(f"O tempo total do projeto é de {tempo_total} dias.")




temperatura = float(input("Digite a temperatura atual: "))

if temperatura > 25:
    print("Alerta! Temperatura acima do limite permitido.")
else:
    print("Temperatura dentro do limite seguro.")




peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc < 25:
    print("Você está com peso normal.")
else:
    print("Você está acima do peso.")





limite = 3000.0
despesas = float(input("Digite o total de despesas do mês (R$): "))

if despesas > limite:
    print("Atenção! Você ultrapassou o limite do orçamento.")
else:
    print("Você está dentro do orçamento.")





hora_atual = int(input("Digite a hora atual (formato 24 horas): "))

if 8 <= hora_atual < 18:
    print("Acesso permitido.")
else:
    print("Acesso negado.")





nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("Aprovado")
elif 5 <= media < 7:
    print("Recuperação")
else:
    print("Reprovado")




distancia = float(input("Digite a distância percorrida (em km): "))

if distancia <= 100:
    print("Valor do pedágio: R$ 10,00")
elif 100 < distancia <= 200:
    print("Valor do pedágio: R$ 20,00")
else:
    print("Valor do pedágio: R$ 30,00")



# LAÇOS FOR E WHILE

#Imprime todos clientes um por vez

clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"]

for cliente in clientes:
    print(cliente)


#Imprime a mensagem 10X

contador = 0

while contador < 10:
    print("Processando dados...")
    contador += 1  # Atualiza o contador para evitar o loop infinito`


#Imprime a mensagem "Bem-vindo ao Buscante!" 5x.   

for i in range(5):
    print("Bem-vindo ao Buscante!")

# Soma todos os valores e no final imprime a soma deles

numeros = [10, 20, 30, 40, 50]

soma = 0
for numero in numeros:
    soma += numero

print(f"A soma total das receitas é: {soma}") # "f" e "{soma}" é a concatenação do valor da 
                                              # variavel soma com a mensagem impressa na tela.

# Percorre a lista, e vai imprimindo o nome dos projetos, ao encontrar um arquivo vazio "None", imprime a mensagem "Projeto ausente"

projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

for projeto in projetos:
    if projeto is None:
        print("Projeto ausente")
    else:
        print(projeto)

# Percorre a lista de livros e vai imprimindo os nomes até chegar no livro "O Hobbit", #
# daí para de percorrer a lista

livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]

for livro in livros:
    if livro == "O Hobbit":
        print(f"Livro encontrado: {livro}")
        break

# Decrementa o estoque até 0 e depois imprime a mensagem "Estoque esgotado"

estoque = 5

while estoque > 0:
    print(f"Venda realizada! Estoque restante: {estoque}")
    estoque -= 1 

print("Estoque esgotado")   


# Faz uma contagem regressiva alternando entre duas mensagens, decrementa a range e a mensagem 
# altera quando os nuúmeros são impares ou pares.

for segundos in range(10, 0, -1):  
    if segundos % 2 == 0: 
        print(f"Faltam apenas {segundos} segundos - Não perca essa oportunidade!")
    else: 
        print(f"A contagem continua: {segundos} segundos restantes.")

print("Aproveite a promoção agora!")

# Utilidade de "continue" em laço

livros = [
    {"nome": "1984", "estoque": 5},
    {"nome": "Dom Casmurro", "estoque": 0},
    {"nome": "O Pequeno Príncipe", "estoque": 3},
    {"nome": "O Hobbit", "estoque": 0},
    {"nome": "Orgulho e Preconceito", "estoque": 2}
]

for livro in livros:
    if livro["estoque"] == 0:
        continue
    print(f"Livro disponível: {livro['nome']}")

# Validação de entrada para login

while True:
    nome_usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    if len(nome_usuario) < 5:
        print("O nome de usuário deve ter pelo menos 5 caracteres.")
        continue

    if len(senha) < 8:
        print("A senha deve ter pelo menos 8 caracteres.")
        continue

    print("Cadastro realizado com sucesso!")
    break