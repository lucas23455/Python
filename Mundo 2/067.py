#Faça um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuario.O programa será interrompido quando o numero solicidado for negativo
while True:
    n=int(input("Digite um numero(negativo pra sair):"))

    if n<0:
        print("PROGRAMA ENCERRADO...")
        break
    print(f"Tabuada do {n}")
    cont=0
    while cont <= 10:
        print(f"{n} X {cont} = {n*cont}")
        cont+=1
    print("="*20)    