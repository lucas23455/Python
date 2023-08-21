#Desenvolva um programa que leia 6 valores inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar,desconsidere-o
soma=0
cont=0
for c in range(0,7):
   num=int(input(f"O digite um num{c+1}°:"))
   if num %2==0:    
    soma+=num
    cont+=1 
    
print(f"voce informou {cont} numeros pares e a soma será {soma}")
    
