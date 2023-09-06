#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou.Depois vai ler a quantidades de gols feitos em cada partida. No final, tudo isso será guardado em um dicionario, incluindo o total de gols feitos durante o campeonato

jogador = {}
partidas= []

jogador["nome"]=str(input("Nome do jogador:"))

tot=int(input(f"quantas partidas {jogador['nome']} jogou?"))


for c in range(0,tot):
    partidas.append(int(input(f" Quantos gols na partida {c+1}: ")))

jogador["gols"]= partidas[:]
jogador["total"]= sum(partidas) 

print("="*30)
print(jogador)
print("="*30)
for k,v in jogador.items():
    print(f"{k} : {v}")
print("="*30)
print(f" o jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas")

for i,v in enumerate(jogador['gols']):
    print(f" Na partida {i+1}, fez {v} gols")

print(f" Foi um total de {jogador['total']} gols")    

