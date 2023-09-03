#Aprimore o desafio anterior, mostrando no final:
#a soma de todos os valores pares digitados
#a soma dos valores da terceira coluna
#o maior valor da segunda coluna

#Crie um programa que crie uma matriz de dimensao 3x3 e preencha com valores lidos pelo teclado


#matriz=[[0,0,0],[0,0,0],[0,0,0]]

#criara uma matriz 3x3 com estrutura FOR
#um jeito mais simplificado
matriz=[[0,0,0]*3 for _ in range(3)]
soma_par=0

soma_coluna=0

# o primeiro FOR é pra colocar os dados 
for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna]=int(input(f"digite um valor para [{linha},{coluna}]:"))


# o segundo FOR é pra mostrar a estrutura do dado na tela
print("="*40)
for linha in range(3):
    for coluna in range(3):
       print(f"[{matriz[linha][coluna]:^5}]",end=" ")
       if matriz [linha][coluna] %2 ==0:
        soma_par+=matriz[linha][coluna]
    print()
print("="*40)

print(f"A soma dos numeros pares na matriz:{soma_par}")

for linha in range(0,3):
    soma_coluna+=matriz[linha][2]
print(f"A soma dos valores terceira coluna:{soma_coluna}")


print(f"O maior da segunda linha :{max(matriz[1])}")             
