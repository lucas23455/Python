#Aprimore o desafio 093 para que ele funcione com varios jogadores,incluindo um sistema de visualizaçao de detalhes do aproveitamento de cada jogador

jogadores = []

while True:
    jogador = {}
    jogador["Nome"] = input("Digite o nome do jogador: ")
    partidas = int(input(f"Quantas partidas {jogador['Nome']} jogou? "))

    gols_por_partida = []
    total_gols = 0

    for partida in range(1, partidas + 1):
        gols = int(input(f"Quantos gols {jogador['Nome']} fez na partida {partida}? "))
        gols_por_partida.append(gols)
        total_gols += gols

    jogador["Gols por Partida"] = gols_por_partida
    jogador["Total de Gols"] = total_gols

    jogadores.append(jogador)

    continuar = input("Deseja cadastrar outro jogador? (S/N): ").strip().upper()
    if continuar != "S":
        break

print("\nRelatório de Jogadores:")
for idx, jogador in enumerate(jogadores):
    print(f"\nJogador {idx + 1}:")
    for chave, valor in jogador.items():
        if chave == "Gols por Partida":
            print(f"{chave}:")
            for partida, gols in enumerate(valor, start=1):
                print(f"  Partida {partida}: {gols} gols")
        else:
            print(f"{chave}: {valor}")

while True:
    detalhes = int(input("\nDigite o número do jogador para ver detalhes ou 0 para sair: "))
    
    if detalhes == 0:
        break
    
    if 1 <= detalhes <= len(jogadores):
        jogador = jogadores[detalhes - 1]
        print(f"\nDetalhes do Jogador {detalhes}:")
        for chave, valor in jogador.items():
            if chave == "Gols por Partida":
                print(f"{chave}:")
                for partida, gols in enumerate(valor, start=1):
                    print(f"  Partida {partida}: {gols} gols")
            else:
                print(f"{chave}: {valor}")
    else:
        print("Número de jogador inválido. Tente novamente.")
