#faça um programa que leia 5 valores numericos e guarde-os em uma lista
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posicoes na lista

# Inicializa a lista vazia para armazenar os valores
# Inicializa a lista vazia para armazenar os valores
lista = []
# Loop para ler 5 valores numéricos
for i in range(5):
    lista.append(int(input(f"Digite um valor para a posicao {i}:")))


print(f"Valores digitados: {lista}")

maior_valor = max(lista)
menor_valor = min(lista)



print(f"Maior valor: {maior_valor}",end=" " "nas posiçoes")
for c,v in enumerate(lista):
    if v == maior_valor:
        print(f" {c}...",end=" ")

print()
print(f"Menor valor: {menor_valor}",end=" " "nas posiçoes")
for c,v in enumerate(lista):
    if v == menor_valor:
        print(f" {c}...",end=" ")
print()

