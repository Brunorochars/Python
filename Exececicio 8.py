# Escrever um programa que lê o ano e o nome de um mês (janeiro, fevereiro, março, etc.) 
# e informa quantos dias tem esse mês. Considere as seguintes regras:
#
# - Janeiro, março, maio, julho, agosto, outubro e dezembro: 31 dias
# - Abril, junho, setembro e novembro: 30 dias
# - Fevereiro: 28 dias (29 dias em anos bissextos) 
# 
#  Para considerar se um ano é bissexto, o programa deve ler o ano e aplicar a regra: 
# Um ano é bissexto se for divisível por 4, exceto se for divisível por 100 e não for 
# divisível por 400.

def numero_dias_mes(mes):

    if(mes.lower() == 'fevereiro'):

        if(bissexto == True):
            return "28"
        else:
            return "29"
        
    elif(mes.lower() == 'janeiro' or mes.lower() == 'março' or mes.lower() == 'maio' or 
         mes.lower() == 'julho' or mes.lower() == 'agosto' or mes.lower() == 'outubro' or 
         mes.lower() == 'dezembro'):
        
        return "31"
      
    elif(mes.lower() == 'abril' or mes.lower() == 'junho' or mes.lower() == 'setembro' or 
         mes.lower() == 'novembro'):

        return "30"
    
    else:

        return "Mês inválido!"
    

ano = int(input("Digite o ano: "))
mes = input("Digite o mês: ")

if(ano % 4 == 0 and not ano % 100 == 0):
    bissexto = True
else:
    bissexto = False

print(f"Os números de dias do mês de {mes} é: {numero_dias_mes(mes)}")

