#crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com o nome "SANTO"

c=str(input("digite um nome de uma cidade:")).strip()

print(c[:5].upper() == "SANTO")

