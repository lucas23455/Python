#Desenvolva um prgrama que leia o primeiro termo e a razao de uma P.A.
#NO final,mostre os 10 primeiros termos dessa progressao em while

primeiro_termo = int(input("Digite o primeiro termo da P.A.: "))
razao = int(input("Digite a razão da P.A.: "))

print("Os 10 primeiros termos da P.A. são:")
contador = 0

while contador < 10:
    termo = primeiro_termo + contador * razao
    print(termo, end="")
    contador += 1

print("\nFim da progressão.")
   