#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

nome=str(input("digite seu nome:")).strip()

print("Seu nome tem silva:{}".format("silva" in nome.lower()))