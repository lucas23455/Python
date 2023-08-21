#o mesmo professor do desafio anterior quer sortear a ordem de apresentaçao de trabalhos dos alunos .Faça um programa que leia o nome dos 4 alunos e mostre a ordem sorteada

import random 

n1=input("1°nome:")
n2=input("2°nome:")
n3=input("3°nome:")
n4=input("4°nome:")

lista=[n1,n2,n3,n4]

random.shuffle(lista)

print("a ordem de apresentaçao será")
print(lista)

