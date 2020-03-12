import requests
from bs4 import BeautifulSoup
import re
import os
 
# url = "https://softwarepublico.gov.br/gitlab/vlibras/vlibras/tree/master/commons/centos"
url = 'https://softwarepublico.gov.br/gitlab/vlibras/vlibras/tree/master'
#url = 'https://softwarepublico.gov.br/gitlab/vlibras/vlibras/blob/master/wikilibras/pybossa.sql'
os.chdir('D:\\Python\\Master')
 


class site_runner:
    
    lista_sites = []     
    lista_testados = []
   


    def __init__(self):
        self.url_init = []

    def func_find(self,url,first):
        url = url.rstrip()
        pula = 0
        lista_branch = []
        try:
            res = requests.get(url, verify=False)
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            print(url,'\n',e)
        try:
            if res:
                html_page = res.content
                pat = r'.*?\"(.*)".*'  
                soup = BeautifulSoup(html_page, 'html.parser')
                site = ''
                siteemstring = ''
                text = soup.find_all('span', {"class":"str-truncated"})
                for r in text:
                    for frase in r:
                        for abc in frase:
                            siteemstring = str(abc)    
                            if len(abc) >= 1: #and siteemstring[0:5] == 'https':
                                site = str(url) +  '/' + str(abc)
                                if "\n" not in site and site not in self.lista_sites:
                                    self.lista_sites.append(site)
                                    lista_branch.append(site)
                                    pula =+ 1
                                site = '' 
        except  UnboundLocalError:
            v_erros = open('Erros.txt','a')
            v_erros.write(url)
            v_erros.close()

        
        if pula <=0:
            return (0)


        for a in lista_branch:
            if a not in self.lista_testados:
                self.lista_testados.append(a)
                self.func_find(a,'0')            
        
        if  first  == 'X':
            v_sites = open('Tentativa_return.txt','a')
            self.lista_sites.sort()
            for a in self.lista_sites:
                v_sites.write(a)
                v_sites.write('\n')
            v_sites.close()
        else:
            return

v_erros = open('Erros.txt','w')
v_erros.write('\n')
v_erros.close()
v_sites =  open('Tentativa_return.txt','w')
v_sites.write('\n')
v_sites.close()
objx = site_runner()
objx.func_find(url,'X')

