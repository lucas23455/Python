#Crie um programa onde o usuario possa digitar varios valores numericos e cadatre-os em uma lista.Caso o numero ja exita lá dentro, ele nao será adicionado. NO final, serao exibidos todos os valores unicos digitados, em ordem crescente


valores = []
cont = 0

while True:
    valor = int(input(f"Digite o {cont+1}º valor (999 para parar): "))
    cont += 1

    if valor == 999:
        break

    # Se o valor que foi digitado não estiver na lista 'valores', ele será adicionado
    if valor not in valores:
        valores.append(valor)
    else:
        print("Esse valor já existe na lista. Não será adicionado novamente")

# Ira ordenar os valores da lista
valores.sort()

print("Valores únicos digitados em ordem crescente:")
for v in valores:
    print(v, end=" ")
