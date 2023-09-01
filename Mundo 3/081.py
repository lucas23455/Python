#Crie um programa que vai ler varios numeros e colocados em uma lista
#depois disso, mostre quantos numeros foram digitados
#a lista de valores, ordenada de forma decrescente
#se o valor 5 foi digitado e está ou nao na lista
lista=[]
pos=0
while True:
    valor=(int(input(f"digite o {pos+1}° valor(digite 0 para parar):")))
    pos+=1

    if valor ==0:
        print(f"o programa parou...A quantidades de numeros que foram digitados foram {pos-1}")
        break
    
    lista.append(valor)
    

    
print(f"os valores digitados {lista}")

lista.sort(reverse=True)
print(f"Os valores em forma ordenada de forma decrescente:")

for ordenado in lista:
    print(ordenado, end=" ")


if 5 in lista:
    posicao= lista.index(5)
    print(f"\nO valor 5 foi digitado e esta na lista e esta na posicao {posicao+1}")
else:
    print("\nO valor 5 nao esta na lista")    