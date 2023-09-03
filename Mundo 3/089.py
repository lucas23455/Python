#Crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta. No FINAL,mostre um boletim contendo a media de cada um e permita que o usuario possa mostrar as notas de cada aluno individualmente

ficha=[]

while True:
    nome=str(input("NOME:"))
    nota1=float(input("NOTA1:"))
    nota2=float(input("NOTA2:"))
    media=(nota1+nota2)/2

    ficha.append([nome,[nota1,nota2],media])

    resp=str(input("quer continuar?[S/N]")).upper()

    if resp =="N":
        print("encerrando...")
        break
print("-="*30)
print(f'{"No.":<4}{"Nome":<10}{"Media":>8}')
print("-"*26)
for i,a in enumerate(ficha):
    print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}")

while True:
    print("-"*35)
    opc=int(input("Mostre notas de qual aluno?(999 INTERROMPE):"))
    if opc== 999:
        print("finalizando...")
        break
    if opc <=len(ficha)-1:
        print(f"Notas de {ficha[opc][0]} sao {ficha[opc][1]}")
print("volte sempre!!")        



