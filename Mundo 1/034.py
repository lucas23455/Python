#Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento
#para salarios superiores a R$1250.00, calcule um aumento de 10%
#sobre o salário atual; para os inferiores ou iguais, o aumento é 15%

salario=float(input("Digite o valor do seu salario R$"))
if salario<=1250:
    nov=salario+(salario*15/100)
    #aumentando em 10% sobre o salario antigo
    print ("O seu salario com reajuste seria: ",nov)
else:
    nov =salario+(salario * 10/100)
    #aumentando em 15% sobre o salario antigo
    print ("O seu salario com reajuste seria:",nov)