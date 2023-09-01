#faca um programa que leia nome e peso de varias pessoas guardando tudo em uma lista. No final mostre:

#quantas pessoas foram cadastradas
#uma listagem com as pessoas mais pesadas
#uma listagem com as pessoas mais leves


pessoa = []
lista_pessoa = []
cadas = 0
peso_maior=0
peso_menor=0
while True:
    pessoa.append(input("NOME: "))
    pessoa.append(int(input("PESO: ")))
    cadas += 1

    if len(lista_pessoa) == 0:
        peso_maior=peso_menor=pessoa[1]
    else:
        if pessoa[1]>peso_maior:
            peso_maior=pessoa[1]
        if pessoa[1]<peso_menor:
            peso_menor=pessoa[1]        


    #vai criar uma ligaçao entre as duas listas
    lista_pessoa.append(pessoa[:])

    #ira limpar a lista
    pessoa.clear()


    op = str(input("Quer continuar? [S/N] ")).upper()

    if op == "N":
        print("Encerrando o programa...")
        break

    


print("="*50)
titulo="Resultados"
print(titulo.center(50))
print("="*50)

print(f"Pessoas cadastradas: {cadas}")
print(f"Os dados foram {lista_pessoa}")
print(f"O peso maior foi:{peso_maior}Kg",end=" ")

for p in lista_pessoa:
    if p[1]==peso_maior:
        print(f"[{p[0]}]",end=" ")


print(f"\nO peso menor foi:{peso_menor}kg",end=" ")

for p in lista_pessoa:
    if p[1]==peso_menor:
        print(f"[{p[0]}]",end=" ")
