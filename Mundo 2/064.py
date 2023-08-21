#Crie um programa que leia varios numeros inteiros pelo teclado.O programa só vai parar quando o usuario digitar o valor 999, que é a parada. No final mostre quantos numeros foram digitados e qual é soma entre eles, desconsiderano o 999
soma = 0
contador = 0
while True:
    numero = int(input("Digite um número inteiro (999 para parar): "))
    
    if numero == 999:
        break
    
    soma += numero
    contador += 1

print("Foram digitados", contador, "números.")
print("A soma dos números é:", soma)
