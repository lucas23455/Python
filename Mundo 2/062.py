#Melhore o desafio 061,perguntando para o usuario se ele quer mostrar mais alguns termos.O programa encerra quando ele disser que quer mostrar 0 termos
primeiro_termo = int(input("Digite o primeiro termo da P.A.: "))
razao = int(input("Digite a razão da P.A.: "))

termos_mostrados = 0

while True:
    if termos_mostrados == 0:
        quantidade_termos = 10
    else:
        quantidade_termos = int(input("Quantos termos você deseja mostrar a mais? (Digite 0 para encerrar): "))
    
    if quantidade_termos == 0:
        break
    
    print("Termos da P.A.:", end=" ")
    contador = 0
    
    while contador < quantidade_termos:
        termo = primeiro_termo + termos_mostrados * razao
        print(termo, end=" ")
        termos_mostrados += 1
        contador += 1
    
    print("\n")
    
print("Fim da execução.")
