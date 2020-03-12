import os


caminho = 'D:\\Python\\Master'
try:
    os.chdir(caminho)
except FileNotFoundError:
    os.mkdir(caminho)
    os.chdir(caminho)

v_sites =  open('nodup2.txt','w')
v_sites2 = open('linksfnew.txt','r')
lista2 = []
lista1 = []
nome_arq = ''

for url in v_sites2:
    lista2.append(url)

lista1 = list(dict.fromkeys(lista2))

for a in lista1:
    v_sites.write(a)

v_sites.close()

