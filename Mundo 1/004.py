#faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informaçoes possiveis sobre ele

a=input("digite algo:")
print("O tipo primitivo desse valor é",type(a))
print("tem espaços?",a.isspace())
print('é um número?', a.isnumeric())
print('é alfabetico',a.isalpha())
print("é alfanumerico",a.isalnum())
print("está em maiusculas",a.isupper())
print("esta em minusculas",a.islower())
print("Está capitalizada?",a.istitle())
