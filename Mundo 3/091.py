#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios. Guarde esses resultados em um dicionario.No final coloque esse dicionario em ordem,sabendo que o vencedor tirou o maior numero no dado

import random

# Dicionário para armazenar os resultados dos jogadores
resultados = {}

# Simule os lançamentos de dados para 4 jogadores
for jogador in range(1, 5):
    resultado = random.randint(1, 6)  # Simula um lançamento de dado de 1 a 6
    resultados[f'Jogador {jogador}'] = resultado

# Exiba os resultados dos jogadores
print("Resultados dos jogadores:")
for jogador, resultado in resultados.items():
    print(f"{jogador}: {resultado}")

# Classifique o dicionário pelos resultados em ordem decrescente
resultados_classificados = dict(sorted(resultados.items(), key=lambda item: item[1], reverse=True))

# Exiba o vencedor
vencedor = list(resultados_classificados.keys())[0]
print(f"\nO vencedor é: {vencedor} com um resultado de {resultados_classificados[vencedor]} no dado.")
