#crie um programa que leia dois valores e mostre um menu na tela
from time import sleep
n1=int(input("digite o primeiro valor:"))
n2=int(input("digite o segundo valor:"))
op=0
while op !=5:
 print("[1]somar")
 print("[2]mutiplicar")
 print("[3]maior")
 print("[4]novos numeros")
 print("[5]sair do programa")

 op=int(input("qual opcao deseja escolher?"))

 if op==1:
    res=n1+n2
    print(f"A soma entre {n1} e {n2} é igual {res}")
 elif op==2:
   res=n1*n2
   print (f"A multiplicao entre {n1} e {n2} é igual {res}")
 elif op ==3:
    if n1>n2:
        print("O 1° valor é maior")
    elif n2>n1:
        print("O 2° valor é maior")
    else:
        print("Os dois são iguais!")
 elif op==4:
    n1=int(input("digite o primeiro novo valor:"))        
    n2=int(input("digite o segundo novo valor:")) 
 elif op==5:
   print("Finalizando...")            
 else:
    print("\033[0;31mOpção invalida!\033[m")
 print("=-="*10)
 sleep(2)  
print("\033[0;34mSaindo do programa...\033[m")     