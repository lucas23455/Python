#Crie um programa que crie uma matriz de dimensao 3x3 e preencha com valores lidos pelo teclado


#criara uma matriz 3x3
matriz=[[0,0,0]*3 for _ in range(3)]

# o primeiro FOR é pra colocar os dados 
for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna]=int(input(f"digite um valor para [{linha},{coluna}]:"))


# o segundo FOR é pra mostrar a estrutura do dado na tela
print("="*40)
for linha in range(3):
    for coluna in range(3):
       print(f"[{matriz[linha][coluna]:^5}]",end=" ")
    print()    
print("="*40)



