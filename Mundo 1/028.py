#escreva um programa que faça o computador "pensar" em numero inteiro entre 0 e 5 e peça para o usuario tentar descobir qual foi o numero escolhido pelo computador


import random
from time import sleep

numero_escolhido = random.randint(0, 5)   

print("Tente adivinhar o número escolhido pelo computador (entre 0 e 5):")
tentativa = int(input())
print("processando...")
sleep(3)
if tentativa == numero_escolhido:
    print("Parabéns! Você acertou o número.")
else:
    print("Você errou. O número escolhido pelo computador foi:", numero_escolhido)
