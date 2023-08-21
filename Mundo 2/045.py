#crie um programa que faça o computador jogar jokenpo com voce

from random import randint
from time import sleep

itens=("pedra","papel","tesoura")
computador=randint(0,2)
print('''Suas opçoes
[0]PEDRA
[1]PAPEL
[2]TESOURA''')
jogador=int(input("qual é sua jogada?"))
print("jo")
sleep(1)
print("ken")
sleep(1)
print("pô!!!")
print("\033[1;31m=\033[m"*20)
print("computador jogou {}".format(itens[computador]))
print("jogador jogou {}".format(itens[jogador]))
print("\033[1;31m=\033[m"*20)
if computador==0: #pedra
    if jogador ==0:
        print("empate")
    elif jogador==1:
        print("jogador vence")
    elif jogador==2:
        print("computador vence") 
    else:
        print("jogada invalida")       
                  
elif computador==1: #papel
    if jogador == 0 :
        print ("computador vence ")
    elif jogador==1:
        print("empate")
    elif jogador==2:
        print("jogador vence")
    else:
        print("jogada invalida")           
elif computador==2: #tesoura 
    if jogador == 0 :
        print("jogador vence")
    elif jogador==1:
        print("computador vence")
    elif jogador==2:
        print("empate")
    else:
        print("jogada invalida")