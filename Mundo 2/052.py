#Faça um programa que leia um numero inteiro e diga se ele é ou nao um numero primo


num = int(input("Digite um número inteiro: "))
tot=0
for c in range(1, num + 1):
    if num % c == 0:
        print("\033[1;33m",end=" ")
        tot += 1

    else:
        print("\033[1;31m", end=" ")   
    print(c, end=" ")
print(f"\no numero {num} foi divisivel {tot}vezes") 
if tot==2:
    print("ELE É PRIMO")
else:
    print("NÃO E UM NUMERO PRIMO")
    
    