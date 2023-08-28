#crie um programa que tenha uma tupla com varias palavras(nao usar acentos).
#Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
# Tupla com várias palavras


palavras = ("python", "programacao", "linguagem", "computádor", "desenvolvimento")

for p in palavras:
    print(f"\nNa palavra {p.upper()} temos:",end="")
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra, end=" ")
         