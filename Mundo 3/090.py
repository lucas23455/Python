#Faça um programa que leia nome e media de um aluno, guardando tambem a situaçao em um dicionario. No final,mostre o conteudo da estrutura na tela


aluno_media={}

nome=str(input("Nome:"))
media=float(input("MEDIA:"))


situaçao="Aprovado" if media>=6.0 else"Reprovado"

aluno_media["nome"]=nome
aluno_media["media"]=media
aluno_media["situaçao"]=situaçao


print("\ninformacoes do aluno:")
print("Nome:",aluno_media["nome"])
print("Media",aluno_media["media"])
print("situacao:",aluno_media["situaçao"])
