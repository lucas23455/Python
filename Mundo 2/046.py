#Faça um programa que mostre na tela uma contagem regressiva pra o estouro de fogos de artificio,ido de 10 a 0,com uma pausa de 1 segundo entre eles

from time import sleep

for c in range(10,-1,-1):
    print(c)
    sleep(1)
print("\033[1;32mOs fogos de artificio estão estorando!!\033[m")    