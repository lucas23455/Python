#Faça um programa que tenha uma funcao notas() que pode receber varias notas de alunos e vai retornar um dionario com seguintes informacoes

#quantidade de notas
# a maior nota
# a menor nota
# a media da turma
#a situacao (opcional)

#adicione tambem as docstrings da funcao
def notas (*n , sit=False):
    r={}
    r["total"]= len(n)
    r["maior"]= max(n)
    r["menor"]= min(n)
    r["media"]= sum(n)/len(n)
     
    if sit:
        if r["media"]>=7:
            r["situaçao"]= "boa"
        elif r["media"]>=5:
            r["situaçao"]= "razoavel"    
        else:
            r["situaçao"]="pessima"

    return r


resp=notas(5.5,2.5,9,8.5, sit=True)
print(resp)