import requests
from bs4 import BeautifulSoup
import re
import os

url = 'https://softwarepublico.gov.br/gitlab/vlibras/vlibras/tree/master'
os.chdir('D:\\Python\\Master')

class site_runner:
    
    lista_sites = []     
    lista_testados = []
   

    def __init__(self):
        self.url_init = []

    def func_find(self,url,first):
        url = url.rstrip()
        try:
            res = requests.get(url, verify=False)
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            print(url,'\n',e)
        html_page = res.content
        pat = r'.*?\"(.*)".*'  
        soup = BeautifulSoup(html_page, 'html.parser')
        site = ''
        pula = 0
        siteemstring = ''
        text = soup.find_all('span', {"class":"str-truncated"})
        lista_branch = []
        for r in text:
            for frase in r:
                for abc in frase:
                    siteemstring = str(abc)    
                    if len(abc) > 1: #and siteemstring[0:5] == 'https':
                        site = str(url) +  '/' + str(abc)
                        if "\n" not in site and site not in self.lista_sites:
                            self.lista_sites.append(site)
                            lista_branch.append(site)
                            pula =+ 1
                        site = ''     
        
        if pula <=0:
            return

        for a in lista_branch:
            if a not in self.lista_testados:
                self.lista_testados.append(a)
                self.func_find(a,'0')            

        if  first  == 'X':
            v_sites = open('Links_sites.txt','a')
            self.lista_sites.sort()
            for a in self.lista_sites:
                v_sites.write(a)
                v_sites.write('\n')
            v_sites.close()




v_sites =  open('Links_sites.txt','w')
v_sites.write('\n')
v_sites.close()
objx = site_runner()
objx.func_find(url,'X')
