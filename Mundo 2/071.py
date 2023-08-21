#Crie um programa que simule o funcionamento de um caixa eletronico. No inicio, pergunte ao usuario qual sera o valor sacado(numero inteiro) e o programa vai informar quantas cedulas de cada valor serão entregues:
#Considere que o caixa possue cedulas de R$50 R$20 R$10 e R$1

valor_sacado = int(input("Digite o valor que deseja sacar: R$ "))

cedula_50 = 0
cedula_20 = 0
cedula_10 = 0
cedula_1 = 0

while valor_sacado > 0:
    if valor_sacado >= 50:
        cedula_50 += 1
        valor_sacado -= 50
    elif valor_sacado >= 20:
        cedula_20 += 1
        valor_sacado -= 20
    elif valor_sacado >= 10:
        cedula_10 += 1
        valor_sacado -= 10
    else:
        cedula_1 += 1
        valor_sacado -= 1

print("\nQuantidade de cédulas entregues:")
print("Cédulas de R$50:", cedula_50)
print("Cédulas de R$20:", cedula_20)
print("Cédulas de R$10:", cedula_10)
print("Cédulas de R$1:", cedula_1)
