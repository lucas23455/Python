#crie um programa que leia o nome completo de uma pessoa e mostre o nome em maiusculo,minusculo, quantas letras ao todo, quantas letra tem o primeiro nome

nome=str(input("digite seu nome completo:")).strip()#ira cortar os espaços

print("Seu nome em letras maiusculas:{}".format(nome.upper()))

print("seu nome em minuscula:{}".format(nome.lower()))

print("A quantidade de letras no nome completo: {}".format(len(nome)-nome.count(" ")))#ira contar apenas as letras, tirando os espaços
separa=nome.split()
print("O nome {} tem a quantidade de {}letras".format(separa[0],len(separa[0]))) 




