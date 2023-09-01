#Crie um programa onde o usuario digite uma expressao qualquer que use parentes, seu aplicativo devera analisar se a expressao passada está com os parenteses abertos e fechados na ordem correta

expr=str(input("digite a expressao:"))
pilha=[]
for simb in expr:
    if simb == '(':
        pilha.append ('(')
    elif simb == ')':
        if len (pilha) >0:
            pilha.pop()
    else:
        pilha.append(')')
        break
if len(pilha)==0:
    print("sua expressao é valida")
else:
    print("sua expressao esta errada")    


