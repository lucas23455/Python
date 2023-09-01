#Crie um programa que vai ler varios numeros e colocar em uma lista

#Depois disso, crie duas listas extras que vao conter apenas os valores pares e os valores impares digitados respectivamente

#ao final, mostre o conteudo dos tres gerados

lista=[]
pares=[]
impares=[]

while True:
    valores=int(input("digite os valores:"))

    lista.append(valores)
     


    if valores ==0:
        print("O programa parou...")
        break

    if valores %2==0:
        pares.append(valores)
    else:
        impares.append(valores)   


print(f"os valores digitados da lista: {lista}")
print(f"os valores pares digitados da lista: {pares}")
print(f"os valores impares digitados da lista: {impares}")
