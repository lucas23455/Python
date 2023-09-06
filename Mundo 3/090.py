#Faça um programa que leia nome e media de um aluno, guardando tambem a situaçao em um dicionario. No final,mostre o conteudo da estrutura na tela

#criando um dicionario vazio
aluno_media={}

aluno_media["nome"]=str(input("Seu nome:"))

aluno_media["media"]=float(input(f"A media do {aluno_media['nome']}:"))


if aluno_media["media"] >=7:
    aluno_media["situacao"]= "aprovado"

elif 5<= aluno_media["media"] <7:
    aluno_media["situacao"]= "recuperacao"

else:
    aluno_media["situacao"]= "reprovado"


print("="*30)
print("informacoes do aluno:")
print(aluno_media)

for k,v in aluno_media.items():
    print(f"{k}: {v}")