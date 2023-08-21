#Crie um programa que leia varios numeros inteiros pelo teclado.No final da execucao,mostre a media entre todos os valores eo maior e o menor valores lidos.O programa deve perguntar ao usuario se ele quer continuar ou nao a digitar os valores
total_numeros = 0
soma = 0
maior_valor = float('-inf')
menor_valor = float('inf')

while True:
    numero = int(input("Digite um número inteiro (ou digite 0 para parar): "))
    
    if numero == 0:
        break
    
    total_numeros += 1
    soma += numero
    
    if numero > maior_valor:
        maior_valor = numero
        
    if numero < menor_valor:
        menor_valor = numero
    
    continuar = input("Deseja continuar? (S/N): ").strip().upper()
    if continuar != 'S':
        break

if total_numeros == 0:
    print("Nenhum número foi digitado.")
else:
    media = soma / total_numeros
    print("Média dos números:", media)
    print("Maior valor digitado:", maior_valor)
    print("Menor valor digitado:", menor_valor)
