#Faça um programa que tenha uma funcao chamada escreva(), que receba um texto qualquer como parametro e mostre uma mensagem cim tamanho adaptavel

def escreva(texto):
    #para adaptar o tamanho
    tamanho_linha = len(texto) + 4   #Adiciona 2 espaços de cada lado do texto e 2 traços
    print('-' * tamanho_linha)
    print(f'  {texto}')
    print('-' * tamanho_linha)

escreva("Ola mundo!")
escreva("biscoito ou bolacha")