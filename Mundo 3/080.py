##Crie um programa onde o usuario possa digitar cinco valores numeros e cadastre-os em uma lista, ja na posicao correta de insercao(sem usar o sort())


lista = []

for c in range(5):
    n = int(input("Digite um valor:"))

    if c == 0 or n >= lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print("=" * 30)
print(f"Os valores digitados em ordem foram {lista}")








