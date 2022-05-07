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
url.get('https://www.jequiti.com.br/kits-e-presentes/kits/shampoo?PS=16#1')
#  #  #  #

# PARSER HTML #
conteudo_pagina = url.page_source
soup = BeautifulSoup(conteudo_pagina, 'html.parser')
#  #  #  #

sleep(4)
"""
carregar_mais = url.find_element_by_xpath('/html/body/main/section/div[5]/div[1]/div[2]/div[4]/button')
sleep(4)
ActionChains(url).scroll(0, 0, 0, 600).perform()
carregar_mais.click()
ActionChains(url).scroll(0, 0, 0, 700).perform()
"""
dados_produtos =[]

# TAG MAE #
#sabonete = soup.findAll('article', attrs={'class':'x-shelf__item has--category js--shelf-item'})
sabonete = soup.findAll('li', attrs={'layout':'342f4034-4259-4d43-b385-416ad871febf'})
#print(body_splash.prettify())
#  #  #  #

# RASPANDO TODOS OS PRODUTOS #
for produto in sabonete:

    nome_produto = produto.find('h2', attrs={'class': 'x-shelf__title'})
    preco_produto = produto.find('span', attrs={'class':'x-shelf__best-price'})

    nome_produto = nome_produto.text
    preco_produto = preco_produto.text
    
    print('Nome do produto: ', nome_produto)
    print('Preço do produto: ', preco_produto)
    print()

    dados_produtos.append([nome_produto, preco_produto])
#  #  #  #

# SALVANDO ARQUIVO #
dados = pd.DataFrame(dados_produtos, columns=['nome','preco'])
dados.to_csv('jequiti/shampoo/shampoo4.csv', index=False)
#  #  #  #