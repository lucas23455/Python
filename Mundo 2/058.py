#Melhore o jogo do desafio 28 onde o computador vai "pensar" em numero entre 0 e 10.So que agora o jogador vai tentar advinhar até acertar,mostrando no final quantos palpites foram necessarios para vencer

from random import randint

computador= randint(0,10)
print("Sou seu COMPUTADOR...Acabei de pensar em um num entre 0 e 10")
print("Consegue advinhar qual foi?")

palpites=0
acertou=False
while not acertou:
    jogador=int(input("Qual é seu palpite?"))
    palpites +=1
    if jogador == computador:
        acertou=True
    else:
      if jogador<computador:
        print("Mais...TENTE outra vez")
      elif jogador>computador:
        print("Menos...TENTE mais uma vez")         

print(f"Acertou com {palpites} palpites")        