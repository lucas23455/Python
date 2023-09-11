#Faça um programa que tenha uma funcao chamada contador(), que receba tres paramnetros:incio, fim, e passo e realize a contagem

#Seu programa tem que realizar tres contagens atraves da funcao criada

#a)de 1 ate 10 de 1 em 1
#b)de 10 ate 0, de 2 em 2
#c)uma contagem personalizada

from time import sleep

def contador (inicio,fim,passo):
    if passo== 0:
        p=1
       
    if passo <0:
        p*=1 

    print("="*30)
    print(f"contagem de {inicio} ate {fim} em {passo}")
    sleep(2.5)    

    
    if inicio<=fim:
        for i in range(inicio,fim+1,passo):
            print(i, end=" ", flush=True)
            sleep(2)
            
    else:
        for i in range(inicio,fim-1,-passo):
            print(i, end=" ", flush=True)
            sleep(2)

# Contagem de 1 até 10 de 1 em 1
print("Contagem de 1 até 10 de 1 em 1:")
contador(1, 10, 1)


# Contagem de 10 até 0 de 2 em 2
print("\nContagem de 10 até 0 de 2 em 2:")
contador(10, 0, 2)   

# Contagem personalizada
inicio=int(input("\nINICIO:"))
fim=int(input("FIM:"))
passo=int(input("PASSO:"))

print("contagem personalizada:")
contador(inicio,fim,passo)
