#crie um programa que leia um frase qualquer e diga se ela é um palindromo, desconsiderando os espaços

frase=str(input("digite uma frase:")).strip().upper()
palavras = frase.split() #separa as palavras da string em lista
junto=''.join(palavras)#junta as palavras
inverso=''
for letra in range(len(junto)-1,-1,-1):
    inverso+=junto[letra]
print(f"o inverso de {junto} é {inverso}")    
if inverso ==junto:    
   print("temos um palindromo")
else:
    print("a frase digitada nao é um palindromo")       

