#Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programador vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar. Calcule o valor da prestaçao mensal, sabendo que ela nao pode exceder 30% do salario ou entao o emprestimo será negado.
print("*="*20)
v=float(input("\033[0;33mQual é o valor da casa?\033[m"))

s=float(input("\033[0;33mQual é o valor do seu salario?\033[m"))

a=float(input("\033[0;33mEm quantos anos ira pagar?\033[m"))


p= v/(a*12)

l=s*0.3

if p<=l:
    print("\033[0;32mParabens! Emprestimo aprovado")
    print(f"Valor da prestaçao mensal: R${p:.2f}\033[m")
else:
    print("\033[0;31mEmprestimo negado\033[m!")
        
