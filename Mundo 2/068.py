#Faça um programa que jogue par ou impar com o computador.O jogo só será interrompido quando o jogador perder,mostrando o total de vitorias consecutivas que ele conquistou no final do jogo

from random import randint
v=0
while True:
    jogador=int(input("diga um valor:"))
    computador = randint (0,10)
    total =jogador+computador
    tipo=" "
    while tipo not in 'PI':
        tipo=str(input('Par ou Impar? [P/I]')).strip().upper()[0]
      
    print (f"voce escolheu {jogador} e o computador {computador}.Total de {total}")
    print("DEU PAR" if total%2==0 else "DEU IMPAR")
    if tipo=="P":
        if total %2==0:
            print("voce venceu")
            v+=1
        else:
            print("voce perdeu!")
            break
    elif tipo=="I":
        if  total%2!=0 :
            print ("você ganhou ")
            v+=1
        else:
            print ('Você Perdeu')
            break
    print("vamos jogar novamente!")
print(f"GAME OVER! voce venceu {v} vezes")        