# Crie um programa onde o usuario possa digitar sete valores numericos e cadastre-os em uma lista unica que mantenha separados os valores pares e impares. No final, mostre os valores pares e impares em ordem crescente

lista=[[],[]]

for i in range(7):
    valor=int(input(f"digite o {i+1}° valor:"))
    
    if valor %2==0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print("="*30)
print(f"Todos os valores:{lista}") 
print(f"Os valores pares:{sorted(lista[0])}")
print(f"Os valores impares:{sorted(lista[1])}")         

    