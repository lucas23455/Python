#um professor quer sotear um dos seus 4 alunos para apagar o quadro.faça um programa que ajude ele,lendo o nome deles e escrevendo o nome do escolhido

import random

n1=input("digite o 1°nome:")
n2=input("digite o 2°nome:")
n3=input("digite o 3°nome:")
n4=input("digite o 4°nome:")

lista=[n1,n2,n3,n4]

escolhido=random.choice(lista)

print("o aluno escolhido foi {}".format(escolhido))


