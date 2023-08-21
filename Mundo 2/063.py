#Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequencia fibonacci
n = int(input("Digite o número de elementos da sequência Fibonacci que você deseja mostrar: "))

a, b = 0, 1
count = 0

while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
