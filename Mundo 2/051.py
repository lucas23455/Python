#Desenvolva um prgrama que leia o primeiro termo e a razao de uma P.A.
#NO final,mostre os 10 primeiros termos dessa progressao
primeiro=int(input("digite o primeiro termo da P.A.:"))
razao=int(input("Digite a Razão:"))
decimo=primeiro+(10-1)*razao

for c in range(primeiro,decimo+razao,razao):
    print(c, end= " > ")
    
print("acabou!!")



