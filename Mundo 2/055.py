#Faça um programa que leia o peso de 5 pessoas. No FINAL, mostre qual foi o menor e qual foi a maior
maior=0
menor=0
for p in range(1,6):
    peso=float(input(f"Peso da pessoa {p}:"))
    if p == 1:
        maior=peso
        menor=peso
    else:
        if peso > maior:
            maior=peso
        if peso < menor:
            menor=peso 
print("="*20)                   
print(f"O maior peso lido foi {maior}Kg")
print(f"O menor peso lido foi {menor}Kg")