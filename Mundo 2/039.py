#faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade
#se ele ainda vai se alistar ao serviço militar
#se é a hora de se alistar
#Se já passou do tempo de alistamento

from datetime import date

ano=int(input("ano de nascimento:"))
atual=date.today().year

idade=atual-ano

if idade <18:
    print(f'Voce tem {idade} anos .AINDA VAI SE ALISTAR AO SERVIÇO MILITAR')
elif idade == 18:
    print(f"Voce tem {idade} anos. É A HORA DE SE ALISTAR")
else:
    print(f"Voce tem {idade} anos. Já passou do tempo de alistamento")        

