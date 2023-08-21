#Faca um programa que leia uma frase pelo teclado e mostre quantas vezes aparece o "a" em que posicao ela aparece a primeira vez, em que posicao ela aparace a ultima vez

frase=str(input("digite uma frase:")).upper().strip()

print("A letras A aparece {} vezes ".format(frase.count("A")))

print("A primeira letra A apareceu na posicao:{}".format(frase.find("A")+1))
print("A ultima letra A apareceu na posicao:{}".format(frase.rfind("A")+1))


