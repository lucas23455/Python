#Crie um programa que leia varios numeros inteiros pelo teclado. O programa só vai parar quando o usuario digitar o valor 999, que é a condicao de parada. No final, mostre quantos numeros foram digitados e qual foi a soma entre eles(desconsiderando o fleg)

s=0
cont=0
while True:
    n=int(input("Digite um numero (999 para parar):"))
    if n == 999:
        break;
    s+=n
    cont+=1
print(f"A soma dos {cont} numeros foram {s}")