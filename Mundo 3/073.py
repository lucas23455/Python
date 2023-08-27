#Crie um tupla preenchida com 20 primeiros colocados da tabela do campenato brasileiro de futebol,ordem da colocaçao.Depois mostre

#apenas os 5 primeiros colocados
#os ultimo dos 4 colocados da tabela
#uma lista com os times em ordem alfabetica
#em que posiçao na tabela está o time do gremio

time=("botafogo","palmeiras","flamengo","fluminence","gremio","atletico-PR","bragantino","fortaleza","cuiabá","sao paulo","atletico-MG","cruzeiro","corinthians","internacional","goias","bahia","santos","vasco","santos","vasco","coritiba","america-MG")
primeiros_colocados=time[:5]
print(f"os 5 primeiros colocados:{primeiros_colocados}")
print("--------------------")
ultimos_quatro_colocados=time[-4:]
print(f"os ultimos 4 colocados:{ultimos_quatro_colocados}")
print("---------------------")
ordem_alfabetica=sorted(time)
print(f"{ordem_alfabetica}")
print("---------------------")
achar_posicao=time.index("gremio")
print(f"a posicao gremio esta:{achar_posicao}")