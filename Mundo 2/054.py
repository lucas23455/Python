#Crie um programa que leia o ano de nascimento de sete pessoas.No final,mostre quantas pessoas ainda nao atingiram a maioridade e quantas já sao de maior

from datetime import date
atual=date.today().year

totmaior=0
totmenor=0

for pess in range(1,7+1):
    
    nasc=int(input(f"ano do seu nascimento {pess}°:"))
    idade=atual-nasc

    if idade>=21:
     totmaior+=1   
    
    else:
     totmenor+=1   
     
print(f"temos {totmaior} de maiores")
print(f"temos {totmenor} de menores")