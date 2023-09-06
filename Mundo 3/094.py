#Crie um programa que leia nome, sexo e idade de varias pessoas, guardando os dados de cada pessoa em um dicionario e todos os dicionarios em uma lista. No final mostre
# quantas pessoas foram cadastradas
# a media de idade do grupo
# uma lista com todas as mulheres
# uma lista de todas as pessoas com idade acima da media
galera = []
soma = media = 0
while True:
    pessoa = {}  # Inicialize um novo dicionário para cada pessoa

    pessoa["nome"] = input("Nome: ")
    while True:
        pessoa["sexo"] = input("Sexo [M/F]: ").upper()
        if pessoa["sexo"] in 'MF':
            break
        print("ERRO! Por favor, digite apenas M ou F")

    pessoa["idade"] = int(input("Idade: "))
    soma+=pessoa["idade"]

    galera.append(pessoa)

    resp = input("Quer continuar [S/N]: ").upper()
    if resp == "N":
        print("Encerrando o programa...")
        break

print("=" * 30)

print(f"Ao todo temos {len(galera)} pessoas cadastradas")

media= soma/len(galera)
print(f"A media de idade é {media:5.2f} anos")

print("As mulheres cadastradas foram", end=" ")

for p in galera:

    if p["sexo"] == "F":
        print(f"{p['nome']}",end=" ")
print() 

print("lista das pessoas que estao acima da media")

for p in galera:
    if p["idade"] >=media:
        print("  ")
        for k,v in p.items():
            print(f"{k} = {v}", end=" ")
        print() 
print("<<<ENCERRADO>>>>")





