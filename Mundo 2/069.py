#Crie um programa que leia a idade e o sexo de varias pessoas.A cada pessoa cadastrada, o programa deverá perguntar se o usuario quer continuar. No final mostre
#quantas pessoas tem mais de 18 anos
#quantos homens foram cadastradados
#quantas mulheres tem menos de 20 anos

quant_18=0
quant_homens=0
quant_mulheres=0

while True:
    idade = int(input('Digite a sua idade:'))
    sexo=input("[M\F]:").upper()

    if idade>=18:
        quant_18+=1 


    if sexo=="M":
        quant_homens +=1

    elif sexo =="F" and idade<=20:
           quant_mulheres +=1

    continuar=input("DESEJA CADASTRAR MAIS UMA PESSOA?(S/N)").upper()
    if continuar !="S":
        break

print(f"quantidade de pessoas de 18 anos {quant_18}")
print(f'Quantidade de Homens Cadastrados{quant_homens}')
print(f'{quant_mulheres} Mulheres com menos de 20 Anos')


