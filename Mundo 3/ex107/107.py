#Crie um módulo chamado moeda.py que tenha as funções incorporadas 'aumentar()', 'diminuir()', 'dobro()' e 'metade()'.

#Faça também um programa que importe esse módulo e use algumas dessas funções.

#Obs.: por exemplo, o 'aumentar()' recebe o preço e uma porcentagem, e calcula.

#o 'diminuir()', mesma coisa.



from moeda import dobro,metade,aumentar,diminuir



input_usuario = float(input("Digite o preço: \n"))


print(f"A metade de {input_usuario} é {metade(input_usuario)}")
print(f"O dobro de {input_usuario} é {dobro(input_usuario)}")
print(f"Aumentando 10%, temos {aumentar(input_usuario, 10)}")
print(f"Diminuindo 10%, temos {diminuir(input_usuario, 10)}")