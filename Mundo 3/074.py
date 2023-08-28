#Crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla
#Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que esta na tupla

from random import randint
#ira procurar 5 numeros aleatorios usando a estrutura for
numeros_aleatorios= (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10) )
print("Os valores sortados foram:")

for n in numeros_aleatorios:
    print(n, end=" ")

#usando metodos max e min    
print(f"\no maior valor sorteado foi:{max(numeros_aleatorios)}") 
print(f"o menor valor sorteado foi:{min(numeros_aleatorios)}")   
