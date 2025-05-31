# Escrever um programa que lê uma string e imprime cada caractere 
# da string em uma linha separada usando for. Junto de cada caractere, 
# imprimir sua posição na string.



def imprime_letras_palavra(palavra):
    print(f"As letras são: ")
    for letra in palavra:
        print (letra)


palavra = input("Digite uma palavra: ")
imprime_letras_palavra(palavra)


