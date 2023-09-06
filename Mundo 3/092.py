#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um dicionario se acaso a ctps for diferente de zero, o dicionario receberá tambem o ano de contratacao e o salario. Calcule e acrescente, alem da idade, com quantos anos a pessoa vai se aposentar

from datetime import datetime

dados={}

dados["nome"]=str(input("Nome:"))
nasc=int(input("Ano de nascimento:"))

dados["idade"] = datetime.now().year-nasc
dados["CTPS"]  = int(input("carteira de trabalho (0 nao tem):"))


if dados["CTPS"] !=0:
    dados["contrataçao"]= int(input("Ano de contrataçao:"))
    dados["salario"]= float(input("Salario: R$"))
    dados["aposentadoria"]= dados["idade"]+ ((dados["contrataçao"]+ 35)-datetime.now().year)
    
print("="*30)
for k,v in dados.items():
      print(f"-{k}: {v}")