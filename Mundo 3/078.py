#faça um programa que leia 5 valores numericos e guarde-os em uma lista
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posicoes na lista
valores=[]

for cont in range(5):
    valores.append(int(input(f"digite o {cont}° valor:")))


maior_valor=max(valores)
menor_valor=min(valores)

posicao_maior = valores.index(maior_valor) + 1  
posicao_menor = valores.index(menor_valor) + 1

print("o maior valor digitado foi{maior_valor} e esta na posicao {posicao_maior}")
    
  

