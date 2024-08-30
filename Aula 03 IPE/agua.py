print("Digite 1 para Líquido.\n")
print("Digite 2 para Vapor.\n")
print("Digite 3 para Sólido.\n")
x = int(input("Digite o valor desejado: "))
if(x == 1):
    print("\nO valor escolhido foi Líquido.")
    print("Menos de 100 graus centigrados")
elif(x == 2):
    print("\nO valor escolhido foi Vapor.")
    print("Mais de 100 graus centigrados")
elif(x == 3):
    print("\nO valor escolhido foi Sólido.")
    print("Menos de 0 graus centigrados")  
else:
    print("Valor invalido")