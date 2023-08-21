#Refaça o desafio 35 dos triangulos, acrecentando o recurso de mostrar que tipo de triangulo será formado
#equilatero:todos os lados iguais
#isosceles:dois lados iguais
#escaleno:todos os lados diferentes

r1=float(input("digite a 1°reta:"))
r2=float(input("digite a 2°reta:"))
r3=float(input("digite a 3°reta:"))

if r1< r2 +r3 and r2<r1+r3 and r3<r1+r2:
    print ("é possivel formar um triangulo")
    if r1 == r2 == r3:
        print("equilatero")
    elif r1!=r2 != r1!=r3 !=r1:
        print("escaleno!!")
    else:
        print("isoceles!")
else :
    print ("não é possível formar um triângulo.")