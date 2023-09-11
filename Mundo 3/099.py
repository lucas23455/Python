#Faça um programa que tenha uma funcao chamada maior(), que receba varios paramentros com valores inteiros

#Seu programa tem que analisar todos os valores e dizer qual deles é o maior

cont = 0  # Inicializa a variável cont fora da função

def maior(*num):
    global cont  # Indica que a variável cont global será usada
    maior_valor = max(num)
    cont += len(num)  # Adiciona a quantidade de números passados à variável cont
    print(f"O maior valor é: {maior_valor} e foram informados {cont} números")

# Chamando a função com vários valores inteiros

maior(10, 5, 27, 3, 8)
maior(20, 40, 61, 8)
maior(0)
maior(6)

