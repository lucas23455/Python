#Crie um programa onde o usuario possa digitar cinco valores numeros e cadastre-os em uma lista, ja na posicao correta de insercao(sem usar o sort())

#No final , mostre a lista ordenada na tela

valores = []
cont=0
for i in range(5):
    valor=int(input(f"digite o {cont+1}° valor:"))
    cont+=1

    if valor not in valores:
        valores.append(valor)
    else:
        print("esse valor ja foi adicionado!")    