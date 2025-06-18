#   Escrever um programa que recebe um texto livre digitado pelo usuário. O programa deve:
# (i) quebrar o texto em palavras, 
# (ii) contar a frequência de cada palavra usando um dicionário palavra → contagem, 
# (iii) exibir o número total de palavras, 
# (iv) exibir as cinco palavras mais frequentes e suas contagens.

# Programa para contar a frequência das palavras em um texto digitado pelo usuário

def receber_texto():
    """
    Função que recebe um texto livre do usuário.
    """
    texto = input("\nDigite um texto livre:\n> ")  # Solicita ao usuário que digite um texto
    return texto  # Retorna o texto digitado

def contar_palavras(texto):
    """
    Função que:
    - Quebra o texto em palavras.
    - Conta a frequência de cada palavra usando um dicionário.
    """
    palavras = texto.lower().split()  # Converte o texto para minúsculas e divide em palavras por espaços
    frequencia = {}  # Cria um dicionário vazio para armazenar a frequência de cada palavra

    for palavra in palavras:  # Percorre cada palavra da lista de palavras
        palavra = palavra.strip('.,!?()[]{}"\'')  # Remove pontuações comuns da palavra

        if palavra in frequencia:  # Verifica se a palavra já está no dicionário
            frequencia[palavra] += 1  # Se já existir, incrementa o contador
        else:
            frequencia[palavra] = 1  # Se for a primeira ocorrência, adiciona com valor 1

    return frequencia  # Retorna o dicionário com as frequências das palavras

def exibir_total_palavras(frequencia):
    """
    Função que exibe o número total de palavras no texto.
    """
    total = sum(frequencia.values())  # Soma todas as contagens de palavras
    print(f"\nNúmero total de palavras: {total}")  # Exibe o total de palavras

def exibir_top_palavras(frequencia, n=5):
    """
    Função que exibe as N palavras mais frequentes e suas contagens.
    """
    print(f"\nTop {n} palavras mais frequentes:")  # Exibe um título com o número de palavras que serão mostradas
    top = sorted(frequencia.items(), key=lambda item: item[1], reverse=True)[:n]  
    # Ordena o dicionário por frequência (valor), em ordem decrescente, e pega as N primeiras palavras

    for palavra, contagem in top:  # Percorre a lista das palavras mais frequentes
        print(f"- '{palavra}' aparece {contagem} vezes.")  # Exibe cada palavra com sua respectiva contagem

def menu():
    """
    Função principal que exibe o menu de opções para o usuário.
    """
    texto = ""  # Variável para armazenar o texto digitado pelo usuário
    frequencia = {}  # Variável para armazenar o dicionário de frequência das palavras

    while True:  # Início de um loop infinito para manter o menu ativo
        # Exibe o menu de opções
        print("\n=== Menu ===")
        print("1 - Digitar um novo texto")
        print("2 - Exibir número total de palavras")
        print("3 - Exibir as 5 palavras mais frequentes")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")  # Lê a escolha do usuário

        if opcao == "1":  # Se o usuário escolher a opção 1
            texto = receber_texto()  # Chama a função para receber o texto
            frequencia = contar_palavras(texto)  # Chama a função para contar as palavras

        elif opcao == "2":  # Se o usuário escolher a opção 2
            if frequencia:  # Verifica se já existe um texto processado
                exibir_total_palavras(frequencia)  # Chama a função para exibir o total de palavras
            else:
                print("Por favor, digite um texto primeiro (opção 1).")  # Mensagem de aviso se não houver texto

        elif opcao == "3":  # Se o usuário escolher a opção 3
            if frequencia:  # Verifica se já existe um texto processado
                exibir_top_palavras(frequencia)  # Chama a função para exibir as 5 palavras mais frequentes
            else:
                print("Por favor, digite um texto primeiro (opção 1).")  # Mensagem de aviso se não houver texto

        elif opcao == "0":  # Se o usuário escolher a opção 0
            print("Encerrando o programa...")  # Mensagem de encerramento
            break  # Sai do loop, encerrando o programa

        else:  # Caso o usuário digite uma opção inválida
            print("Opção inválida. Tente novamente.")  # Mensagem de erro para opção inválida

# Verifica se o programa está sendo executado diretamente (e não importado como módulo)
if __name__ == "__main__":
    menu()  # Chama a função principal para iniciar o programa
