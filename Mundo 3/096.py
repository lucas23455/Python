#Faça um programa que tenha uma funcao chamada area(),que receba as dimensoes de um terreno tangular (largura e  comprimento) e mostre a area do terreno


def area(l,c):    
  a=l*c
  print(f"A area de um terreno {l} X {c} : {a} metros quadrados")


print("controle de Terreno")
print("="*30)
     
l=float(input("LARGURA (m):"))
c=float(input("COMPRIMENTO (c):"))
area(l,c)

