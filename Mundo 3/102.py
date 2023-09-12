#Crie um programa que tenha uma funcao fatorial() que receba dois parametros: o primeiro que indica o numero a calcular eo outro chamada show, que será um valor logico (opcional) indicando se será mostrando ou nao na tela o processo de calculo de fatorial

def fatorial(numero, show=False):
    """
    Função que calcula o fatorial de um número.

    :param numero: O número para o qual calcular o fatorial.
    :param show: Um valor lógico indicando se o processo deve ser mostrado na tela (padrão é False).
    :return: O resultado do fatorial.
    """


def fatorial(n, show=False):
    """
    Função que calcula o fatorial de um número.

    :param n: O número para o qual calcular o fatorial.
    :param show: Um valor lógico indicando se o processo deve ser mostrado na tela (padrão é False).
    :return: O resultado do fatorial.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end=" ")
            if c > 1:
                print(" x ", end="")
            else:
                print(" = ", end=" ")
        f *= c
    return f

print(fatorial(5, show=True))
help(fatorial)
