#Crie um programa que tenha a funcao leiaint(), que vai funcionar de forma semelhante a funcao input() do python, só que fazendo a validacao para aceitar apenas um valor numerioco

#ex: n=leiaint("digite um n")
def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("\033[0;31mErro! Digite um número inteiro válido.\033[m")
        if ok:
            break
    return valor

n = leiaint("Digite um número: ")
print(f"Você acabou de digitar o número {n}")
