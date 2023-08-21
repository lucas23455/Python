#Crie um programa que leia nome e o preço de varios produtos.O programa deverá perguntar se o usuario vai continuar no final, mostre
#Qual é o total gasto na compra
#quantos produtos custam mais de R$1000
#qual é o nome do produto mais barato

total_gasto = 0
produtos_mais_de_1000 = 0
nome_produto_mais_barato = None
preco_produto_mais_barato = float('inf')

while True:
    nome_produto = input("Digite o nome do produto: ")
    preco_produto = float(input("Digite o preço do produto: R$ "))
    
    total_gasto += preco_produto
    
    if preco_produto > 1000:
        produtos_mais_de_1000 += 1
    
    if preco_produto < preco_produto_mais_barato:
        nome_produto_mais_barato = nome_produto
        preco_produto_mais_barato = preco_produto
    
    continuar = input("Deseja continuar? (S/N): ").upper()
    if continuar != 'S':
        break

print("\nResumo da Compra:")
print("Total gasto na compra: R$", total_gasto)
print("Quantidade de produtos com preço maior que R$1000:", produtos_mais_de_1000)
print("Nome do produto mais barato:", nome_produto_mais_barato)
print("Preço do produto mais barato: R$", preco_produto_mais_barato)
