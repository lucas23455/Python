#Faça um programa que tenha uma funcao chamada ficha(), que receba dois parametros opcionais: o nome de um jogador e quantas gols ele marcou

#o programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado nao tenha sido informado corretamente

def ficha(nome="Desconhecido", gols=0):
    """
    Função que exibe a ficha de um jogador.

    :param nome: O nome do jogador (padrão é "Desconhecido").
    :param gols: A quantidade de gols marcados pelo jogador (padrão é 0).
    """
    print(f"Nome do jogador: {nome}")
    print(f"Gols marcados: {gols}")

# Solicita o nome e a quantidade de gols ao usuário
nome_jogador = input("Digite o nome do jogador: ").strip()
gols_jogador = input("Digite a quantidade de gols marcados: ")

# Verifica se o valor de gols é um número válido
if gols_jogador.isnumeric():
    gols_jogador = int(gols_jogador)
else:
    gols_jogador = 0

# Chama a função com os dados fornecidos ou os valores padrão
ficha(nome_jogador, gols_jogador)
help(ficha)