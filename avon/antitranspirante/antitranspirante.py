# BIBLIOTECAS #
import attr
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import pandas as pd
from selenium.webdriver import ActionChains
#  #  #  #

options = Options()

# URL #
url = webdriver.Chrome(options=options)
url.get('https://www.avon.com.br/s/antitranspirante?map=term')
#  #  #  #

sleep(4)

dados_produtos = []

# ROLANDO PAGINA + VER MAIS #
carregar_mais = url.find_element_by_class_name('css-3aiv0')
ActionChains(url).scroll(0, 0, 0, 1600).perform()

for ver_mais in range(0,3):
   ver_mais = carregar_mais.click()
   sleep(2)
   ActionChains(url).scroll(0, 0, 0, 1500).perform()
   sleep(4)
#  #  #  #

# PASER HTML #
conteudo_pagina = url.page_source
soup = BeautifulSoup(conteudo_pagina, 'html.parser')
#  #  #  #

# TAG MAE #
antitranspirante = soup.findAll('div', attrs={'class':'css-1y7l0uq'})
#print(antitranspirante.prettify())
#  #  #  #

# RASPANDO TODOS OS PRODUTOS #
for produto in antitranspirante:

    nome_produto = produto.find('h3', attrs={'class': 'css-idyvfm'})
    preco_produto = produto.find('div', attrs={'class':'css-s1bw7y'})

    if preco_produto:
        preco_produto = produto.find('div', attrs={'class': 'css-s1bw7y'})
        preco_produto = preco_produto.text 
    else:
        preco_produto = produto.find('div', attrs={'class': 'css-1qtjchi'})
        preco_produto = preco_produto.text
    
    nome_produto = nome_produto.text
    #preco_produto = preco_produto.text

    print('Nome do produto: ', nome_produto)
    print('Preço do produto: ', preco_produto)
    print()

    dados_produtos.append([nome_produto, preco_produto])
#  #  #  #

# SALVANDO ARQUIVO #
dados = pd.DataFrame(dados_produtos, columns=['nome','preco'])
dados.to_csv('avon/antitranspirante/antitranspirante.csv', index=False)
#  #  #  #