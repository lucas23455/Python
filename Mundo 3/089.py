#Crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta. No FINAL,mostre um boletim contendo a media de cada um e permita que o usuario possa mostrar as notas de cada aluno individualmente

# Função para calcular a média das notas
def calcular_media(notas):
    return sum(notas) / len(notas)

# Lista composta para armazenar os dados dos alunos
alunos = []

# Loop para coletar dados dos alunos
while True:
    nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
    
    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))
    
    alunos.append([nome, [nota1, nota2]])

# Mostra as médias e permite exibir as notas individuais
print("\nBoletim:")
for aluno in alunos:
    nome = aluno[0]
    notas = aluno[1]
    media = calcular_media(notas)
    print(f"{nome}: Média = {media:.2f}")

    mostrar_notas = input("Deseja ver as notas deste aluno? (s/n): ")
    if mostrar_notas.lower() == 's':
        print(f"Notas de {nome}: {notas}")
