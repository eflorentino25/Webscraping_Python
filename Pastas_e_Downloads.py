import os
import requests
from bs4 import BeautifulSoup
import urllib.request
from urllib.error import HTTPError

#Funções 
def func_codw(url,nome):
    nomein = nome.rstrip()
    
    # v_codes = open(nomein,'w')
    # try:
    #     res = requests.get(url)
    # except requests.exceptions.RequestException as e:  # This is the correct syntax
    #     print(e)
    #     return
    # html_page = res.content
    # soup = BeautifulSoup(html_page, 'html.parser')
    # site = ''
    # text = soup.find_all('code')
    # for r in text:
    #     for e in r:
    #         try:
    #             v_codes.write(e)
    #         except UnicodeEncodeError:
    #             print(url + ' Fazer download na mão' )
    # v_codes.close()
    # nomein = 'd_' + nomein

    download(url,nomein)

def download(url,nome):
    tam = 0
    url = url.rstrip()
    try:
        urllib.request.urlretrieve(url,nome)
    except UnicodeEncodeError:
        tam =  tam + 1
    except HTTPError as e :
        print(e)
        print('para arquivo :' + str(url))

def nomemaker(url):           
    tam = 0
    for p in range(len(url) - 1 ,0,-1):
        a = url[p]
        if a != '/':
            tam  = tam + 1
        else:
            break

    nome_arq = str(url[len(str(url)) - tam:len(str(url))])
    return(nome_arq) 

fixo = 'D:\\Python\\Master'
caminho = fixo 
try:
    os.chdir(caminho)
except FileNotFoundError:
    os.mkdir(caminho)
    os.chdir(caminho)

#variaveis
nome_arq = ''
v_sites2 = open('linksfnew.txt','r')
tam = 0
nome_salv = ''
st = []

for site in v_sites2:
    st.append(site)

st.sort()
#Inicio do processamento
for site in st:
    nome_arq = str(site)
    nome_arq = nome_arq.rstrip()
    nome_arq = nome_arq[65:]
    tam = 0
    nome_arq =  nome_arq
    # criar as pastas com os nomes corretos
    # for p in range(len(nome_arq) - 1 ,0,-1):
    #     a = nome_arq[p]
    #     if '/' in nome_arq and  a != '/':
    #         tam  = tam + 1
    #     else:
    #         #tam  = tam + 1
    #         break
    nome_arq = str(nome_arq[0 : len(str(nome_arq))- tam])
    nome_arq = nome_arq.replace("/","\\")
    caminho = fixo + '\\'+ nome_arq
    # parte da criação de pastas 
    # try:
    #     os.chdir(caminho)
    # except FileNotFoundError:
    #     os.mkdir(caminho)
    #     os.chdir(caminho)            
    # except NotADirectoryError:
    #     os.mkdir(caminho)
    #     os.chdir(caminho)

# # Fazer  o download do código para dentro da pasta correta agora
    try:
        os.chdir(caminho)
    except FileNotFoundError:
        #fazer o download ou a cópia do código. Ou os dois?
        nome_salv =  nomemaker(site)
        site = site.replace("tree",'raw')
        site = site.rstrip()
        func_codw(site,nome_salv)
    except NotADirectoryError:
        tam = 1

v_sites2.close()
