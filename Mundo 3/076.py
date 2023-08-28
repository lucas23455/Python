#Crie um programa que tenha uma tupla unica com nomes de produtos e seus rspectivos preços, na sequecia
#no final, mostre uma listagem de preços, organizando os dados em forma tabular
# Tupla de produtos e preços

# Tupla de produtos e preços
produtos_e_precos = ("Lapis",1.75,"borracha",2,"caderno",15.90,"estojo",25,"transferidor",4.90,"compasso",9.99,"mochila",123.00,"canetas",22.30,"livro",23.90)
print("-"*40)
titulo="\033[1;34mlistagem de preços\033[m"
print(titulo.center(50))
print("-"*40)
total=0
for pos in range(0,len(produtos_e_precos)):
    if pos % 2==0:
        print(f"{produtos_e_precos[pos]:.<30}R$", end=" ")
    else:
        print(f"{produtos_e_precos[pos]:>4.2f}")
        total += produtos_e_precos[pos]
print("-"*40)
print(f"\033[1;34mTotal\033[m:R${total:>4.2f}")        

