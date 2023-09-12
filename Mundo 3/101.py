#Crie um programa que tenha uma funcao chamada voto() que vai receber como paramentro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto negado,opcional ou obrigatorio nas eleicoes


def voto(ano_nascimento):
    from datetime import date
    idade = date.today().year - ano_nascimento

    if idade < 16:
        return f"Você tem {idade} anos: Voto Negado"
    elif 16 <= idade <= 18 or idade >= 70:
        return f"Você tem {idade} anos: Voto Opcional"
    else:
        return f"Você tem {idade} anos: Voto Obrigatório"


ano_nascimento = int(input("Ano de nascimento: "))
print("="*30)

resultado = voto(ano_nascimento)
print(resultado)
