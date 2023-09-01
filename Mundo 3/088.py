#faca um programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntar quantos jogos serao gerados e vai sortear 6 numeros entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta

import random

# Pergunta quantos jogos o jogador quer gerar
quantidade_jogos = int(input("Quantos jogos você quer gerar? "))

# Função para gerar um jogo com 6 números
def gerar_jogo():
    return sorted(random.sample(range(1, 61), 6))

# Gera os jogos e armazena em uma lista composta
jogos = [gerar_jogo() for _ in range(quantidade_jogos)]

# Mostra os jogos gerados
print("\nJogos gerados:")
for jogo in jogos:
    print(jogo)
