#Aprimore o desafio anterior, mostrando no final:
#a soma de todos os valores pares digitados
#a soma dos valores da terceira coluna
#o maior valor da segunda coluna

# Inicializa uma matriz 3x4 com valores zero
matriz = [[0] * 3 for _ in range(3)]

# Preenche a matriz com valores lidos pelo teclado
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f"Digite o valor para a posição ({i}, {j}): "))

# Mostra a matriz preenchida
print("Matriz preenchida:")
for linha in matriz:
    for valor in linha:
        print(f"[{valor}]", end=" ")
    print()  # Pula para a próxima linha após cada linha da matriz

# Calcula a soma de todos os valores pares digitados
soma_pares = sum(valor for linha in matriz for valor in linha if valor % 2 == 0)
print("Soma dos valores pares:", soma_pares)

# Calcula a soma dos valores da terceira coluna
soma_terceira_coluna = sum(matriz[i][2] for i in range(3))
print("Soma dos valores da terceira coluna:", soma_terceira_coluna)

# Encontra o maior valor da segunda coluna
maior_segunda_coluna = max(matriz[i][1] for i in range(3))
print("Maior valor da segunda coluna:", maior_segunda_coluna)
