#Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla. No final mostre:

#quantas vezes parareceu o valor 9
#em que posicao foi digitado o primeiro valor 3
#quais foram os numeros pares

n1= int(input("digite o primeiro valor:"))
n2= int(input("digite o segundo valor:"))
n3= int(input("digite o terceiro valor:"))
n4= int(input("digite o quarto valor:"))

numeros_guardados = (n1, n2, n3, n4)

print(f"Números guardados: {numeros_guardados}")

# Conta quantas vezes o valor 9 aparece
quantidade_de_9 = numeros_guardados.count(9)

print(f"Quantidade de vezes que apareceu o valor 9: {quantidade_de_9}")

# Em que posiçao esta o numero 3
if 3 in numeros_guardados:
    posiçao_de_3=numeros_guardados.index(3)+1
else:
    print("O valor de 3 não foi digitado")

# os valores pares encontrados
print("ps valores pares digitados foram:",end=" ")
for numeros_pares in numeros_guardados:
    if numeros_pares % 2 == 0:
        print(numeros_pares, end=" ")