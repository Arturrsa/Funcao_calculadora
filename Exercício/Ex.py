
# funçao +

def adicao(valor_1, valor_2):
    return valor_1 + valor_2 

# funçao -
def subtracao(valor_1, valor_2):
    return valor_1 - valor_2

# funçao *
def multiplicacao(valor_1, valor_2):
    return valor_1 * valor_2

# funçao /
def divisao(valor_1, valor_2):
    return valor_1 / valor_2


print("Escolha:\n \n(a) para adicao, \n(s) para subtracao, \n(m) para multiplicação, \n(d) para divisão!\n ")


a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))

escolha = input("Escolha a operação: ")
    


# adição
if escolha == 'a': 
    print(adicao(a, b))
    
# subtração
elif escolha == 's':  
    print(subtracao(a, b))
   
# Multiplicação
elif escolha == 'm':
    print(multiplicacao(a, b))
    
# Divisão
elif escolha == 'd':
    print(divisao(a, b))
    
else:
     print(0)
 
    
    