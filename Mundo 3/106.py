#Faça um minisistema que utilize o interactive help do python.O usuario vai digitar o comando e o manual vai aparecer. Quando o usuario digitar a palavra "fim",o programa se encerrara
#use cores
c = (
    "\033[m",      # 0 - sem cores
    "\033[0;30;41m",  # 1 - vermelho
    "\033[0;30;42m",  # 2 - verde
    "\033[0;30;43m",  # 3 - amarelo
)

def ajuda(com):
    titulo(f"Acessando manual do comando '{com}'", 2)
    help(com)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(f"{c[cor]}")
    print("=" * tam)
    print(f"  {msg}")
    print("=" * tam)
    print(c[0])

comando = " "
while True:
    titulo("Sistema de ajuda pyHELP", 1)  # Use a cor 1 para vermelho, por exemplo
    comando = str(input("Funcao ou biblioteca > "))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)
titulo("Até logo!", 1)
