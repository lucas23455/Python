#Escreva um programa que leia um num inteiro qualquer e peça para o usuario escolher qual será a base de conversao

#1 para binario
#2 para octal
#3para hedecimal

num = int(input("Digite um número inteiro: "))

print("\nEscolha uma das bases de conversão:\n")
print("=" * 20)
print("[1] Binário")
print("[2] Octal")
print("[3] Hexadecimal")
print("=" * 20)

op = int(input("Digite o número da opção desejada: "))

if op == 1:
    res = bin(num)[2:]  # Removendo o prefixo '0b'
    print("{} convertido para BINÁRIO é igual a {}".format(num, res))
elif op == 2:
    res = oct(num)[2:]  # Removendo o prefixo '0o'
    print("{} convertido para OCTAL é igual a {}".format(num, res))
elif op == 3:
    res = hex(num)[2:].upper()  # Removendo o prefixo '0x' e colocando em letras maiúsculas
    print("{} convertido para HEXADECIMAL é igual a {}".format(num, res))
else:
    print("\033[1;31mOPÇÃO INVÁLIDA!!!\033[m")
