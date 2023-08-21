#Crie um programa que leia duas notas de um aluno e calcule suas media,mostrando uma mensagem no final de acordo com a media atingida

n1=float(input("digite a primeira nota:"))
n2=float(input("digite a segunda nota:"))

media=(n1+n2)/2

if media >= 7.0:
    print("\033[1;32mAPROVADO\033[m")
elif media >= 5.0 and media < 7.0:
    print("Recuperaçao")
else:
    print("\033[1;31mREPROVADO\033[m")        
