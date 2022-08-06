
print("Escolha:\n \n(a) para adição, \n(s) para subtraçção!\n ")


a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))

escolha = input("Escolha a operação: ")

# adição
if escolha == 'a': 
    resultado = a + b
    
# subtração
if escolha == 's':  
    resultado = a - b
    

print(resultado)

