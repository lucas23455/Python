#Crie um codigo em python que teste se o site pudim esta acessivel pelo computador usado

import urllib
import urllib.request


try:
   site=urllib.request.URLopener("http://www.pudim.com.br") 
except urllib.error.URLErro:
    print("deu erro!! o site nn ta acessivel")   
else:
    print("tudo ok")      

