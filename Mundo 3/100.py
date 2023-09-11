#Faça um programa que tenha uma lista chamada numeros e duas funcoes chamada sorteie() e somaPar().A primeira funcao vai sortear 5 numeros e vai colocar-los dentro da lista e o segunda funcao vai mostrar a soma entre todos os valores pares sorteados pela funcao anterior

from random import randint
from time   import sleep

def sorteie(numeros):
    print("Sorteando 5 números:")
    for i in range(5):
        n=(randint(1,10))
        numeros.append(n)
        print(f"{n}", end=" ",flush=True)
        sleep(0.3)
    print("pronto!")    

def somaPar(numeros):
    soma=0
    for valor in numeros:
        if valor %2 ==0:
            soma+= valor
    print(f"somando os numeros pares de {numeros}, temos {soma}")        


numeros = []
sorteie(numeros)
somaPar(numeros)




