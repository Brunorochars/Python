# Escrever um programa em python que lê temperaturas diárias (float) até que o usuário 
# digite sair. Ao final, o programa deve exibir: (i) o número total de temperaturas 
# lidas, (ii) a lista completa de temperaturas, (iii) a menor e a maior temperatura 
# registradas, (iv) a temperatura média do período.

# Função para ler as temperaturas inseridas pelo usuário
def ler_temperaturas():
    temperaturas = []  # Lista para armazenar as temperaturas digitadas

    while True:  # Loop infinito até o usuário digitar "sair"
        entrada = input("Digite a temperatura (ou 'sair' para encerrar): ").strip()

        if entrada.lower() == "sair":  # Verifica se o usuário quer encerrar
            break

        try:
            # Converte a entrada em float e adiciona à lista
            temperatura = float(entrada)
            temperaturas.append(temperatura)
        except ValueError:
            # Mostra mensagem se a entrada não for um número válido
            print("Entrada inválida. Por favor, digite um número ou 'sair'.")

    return temperaturas  # Retorna a lista de temperaturas

# Função para exibir o relatório final com estatísticas
def exibir_relatorio(temperaturas):
    if not temperaturas:  # Verifica se a lista está vazia
        print("Nenhuma temperatura foi registrada.")
        return  # Encerra a função se não houver dados

    total = len(temperaturas)  # Conta o total de temperaturas
    menor = min(temperaturas)  # Encontra a menor temperatura
    maior = max(temperaturas)  # Encontra a maior temperatura
    media = sum(temperaturas) / total  # Calcula a média das temperaturas

    # Exibe os resultados
    print("\n===== RELATÓRIO DE TEMPERATURAS =====")
    print(f"Total de temperaturas lidas: {total}")
    print("Lista de temperaturas:", temperaturas)
    print(f"Menor temperatura registrada: {menor:.2f}°")
    print(f"Maior temperatura registrada: {maior:.2f}°")
    print(f"Temperatura média do período: {media:.2f}°")

# Função principal que coordena o programa
def main():
    temperaturas = ler_temperaturas()  # Lê as temperaturas inseridas pelo usuário
    exibir_relatorio(temperaturas)     # Exibe o relatório com os dados coletados

# Ponto de entrada do programa
if __name__ == "__main__":
    main()  # Executa a função principal
