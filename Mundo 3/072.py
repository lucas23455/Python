#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extensao, de zero até vinte

#seu programa deverá ler um numero pelo teclado(entre 0 e 20) e mostra-lo por extensao.

#guardados dentro da tupla
numeros_guardados=(
        'zero','um', 'dois', 'três', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
        'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
        'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    numero=int(input("digite um num entre 0 e 20:"))

    if 0<= numero <=20: 
        #Ao digitar o numero especifico, ele procurará na posicao em que se encontra na tupla
        numero_mostrado=numeros_guardados[numero]
        print(f"voce digitou o numero:{numero_mostrado}")
        op=input("quer continuar?[S/N]:").upper()
        if op != "S":
            print("TERMINANDO O PROGRAMA...")
            break
    else:
        print("numero invalido. Digite novamente.")