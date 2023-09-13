#Reescreva a funcao leiaint() que fizemos no desafio 4, incluindo agora a possibilidade da digitaçao de um numero de tipo invalido
#Aproveite e crie tambem uma funcao leiaFloat com a mesma funcionalidade


def leiaint(msg):
    while True:
        try:
            n=int(input(msg))
        except(ValueError,TypeError):
            print("ERRO: por favor, digite um numero inteiro valido")
        except(KeyboardInterrupt):
            print("entrada de dados interrompida!!")  
            return 0  
        else:
           return n         

def leiafloat(msg):
    while True:
        try:
            n=float(input(msg))
        except(ValueError,TypeError):
            print("ERRO!!digite um numero real ") 
        except(KeyboardInterrupt):
            print("entrada de dados interrompidas!")
            return 0
        else:
            return n       
            

num = leiaint("Digite um número: ")
print(f"Você acabou de digitar o número {num}")

num2= leiafloat("digite um numero real:")
print(f"voce acabou de digitar o numero {num2}")
