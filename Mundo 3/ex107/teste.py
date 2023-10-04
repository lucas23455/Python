import moeda

p = float(input("digite o preço R$"))
print(f"a medade de {p}: {moeda.metade(p)}")
print(f"o dobro de {p}: {moeda.dobro(p)}")
print(f"aumentando 10%, temos R$ {moeda.aumentar(p,10)}")
print(f"diminuindo 30%, temos R$ {moeda.diminuir(p,30)}")
