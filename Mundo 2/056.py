#Desenvolva um programa que leia o nome,idade e sexo de 4 pessoas. no final do programa, mostre:
#A media de idade do grupo
#qual é o nome do homem mais velho
#quantas mulheres tem menos de 20 anos
somaidade=0
media=0

maioridhomem=0
nomevelho=""

totmulher20=0

for p in range(1,5):
    print(f"----{p} PESSOA----")
    nome=str(input("Nome:")).strip()
    idade=int(input("Idade:"))
    sexo=str(input("Sexo[M/F]:")).strip().upper()
    somaidade+=idade
    if p==1 and sexo == "M":
        maioridhomem=idade
        nomevelho=nome
    if sexo == "M" and idade>maioridhomem:
        maioridhomem=idade
        nomevelho=nome
    if sexo == "F" and idade <20:
        totmulher20+=1   
media=somaidade/4
print(f"A media de idade do grupo é de {media} anos") 
print(f"O homem mais velho tem {maioridhomem} anos e se chama {nomevelho}") 
print(f"Ao todo sao {totmulher20} mulheres com menos de 20 anos")  