#faça um programa que leia o sexo de uma pessoa,mas só aceite os valores "m" ou "f". caso esteja errado,peça a digitaçao novamente ate ter um valor correto



 #tira os espaços, deixa maiusculo, pega a primeira letra
sexo = input("Informe seu sexo[M/F]:").strip().upper()[0]

while sexo not in "MmFf":
    sexo=str(input("\033[0;31m Dados invalidos.Por favor, informe seu sexo:\033[m"))
if sexo=="M":
    print("voce é macho!!")
else:
    print("voce é femea")       
    
    
    