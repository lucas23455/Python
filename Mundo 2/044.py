#elabore um programa que calcule o valor a ser pago por produto,considerando o seu preço normal e condicao de pagamento


preco = float(input("O valor do produto R$"))

print("[1] A vista no dinheiro/cheque")
print("[2] A vista no cartao")
print("[3] Pagar 2x no cartao")
print("[4] Pagar 3x ou mais no cartao")

op = int(input("Qual opcao deseja pagar? "))

if op == 1:
    desconto = preco * (10 / 100)
    preco_final = preco - desconto
    print("\033[1;32mVocê escolheu a opcao a vista no dinheiro/cheque\033[m")
    print(f"O valor do produto foi {preco}, então terá o desconto de 10% será de {preco_final}")
elif op == 2:
    desconto = preco * (5 / 100)
    preco_final = preco - desconto
    print("\033[1;31mVocê escolheu pagar no cartao\033[m")
    print(f"O valor do produto foi {preco}, então o desconto de 5% será de R${preco_final}")
elif op == 3:
    print("Voce escolheu pagar 2X no cartao")
    duas_vezes = preco / 2
    print(f"O seu preço parcelado em 2X será {duas_vezes}")
elif op == 4:
    print("\033[1;34mVocê escolheu dividir em parcelas\033[m")
    parcelas = int(input('Quantidade de Parcelas? '))
    preco_final = preco / parcelas
    juros = (preco * 2) / 100
    total = juros + preco_final
    total_final=total*parcelas
    print(f"Você dividiu a parcela em {parcelas}X")
    print(f"Terá que pagar por mês R${preco_final:.2f}")
    print(f"E o total mais o juros será de R${total:.2f}")
    print(f"totalizando com o preço de R$ {total_final}")
else:
    print('\nOpção inválida')
