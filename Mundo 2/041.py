#A confederaçao nacional de nataçao precisa de um programa que leia ano de nacimento de uma atleta e mostre sua categoria de acordo com a idade
from datetime import date

atual=date.today().year

ano=int(input("ano de nascimento:"))

idade=atual-ano

if idade <=9:
    print("mirim")
elif idade <=14:
    print("infantil")
elif idade <=19:
    print("junior")
elif idade <=20:
    print("senior")
else:
    print("master") 