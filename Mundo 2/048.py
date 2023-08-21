#faça um programa que calcule a soma entre todos os numeros impares que sao multiplos de tres a que se encontram de 1 até 500
soma=0
cont=0
for c in range(1,501,2):
   if c % 3==0:
    cont=cont+1
    #duas formas     
    soma+=c
print(f"A soma de todos os {cont} valores solicitados: {soma}")    