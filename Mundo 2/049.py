#refaça o desafio 009,mostrando a tabuada de um numero que o usuario escolher,só que agora utilizando um laço for

n=int(input("qual numero deseja ver a tabuada:"))
for c in range(0,10+1):
    print(f" {n} X {c}={n*c}")