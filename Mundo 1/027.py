#faca um programa que leia o nome de uma pessoa, mostrando em seguida o primeiro e e ultimo nome separadamente

nome=input("digite seu nome:")

separa=nome.split()

print("o primeiro nome: {}".format(separa[0]))
print("o segundo nome: {}".format(separa[len(separa)-1]))