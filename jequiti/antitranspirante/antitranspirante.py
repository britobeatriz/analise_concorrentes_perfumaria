# BIBLIOTECAS #
import attr
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import pandas as pd
#  #  #  #

options = Options()

# URL #
url = webdriver.Chrome(options=options)
url.get('https://www.jequiti.com.br/busca?ft=antitranspirante#1')
#  #  #  #

# PARSER HTML #
conteudo_pagina = url.page_source
soup = BeautifulSoup(conteudo_pagina, 'html.parser')
#  #  #  #

sleep(4)

dados_produtos =[]

# TAG MAE #
antitranspirante = soup.findAll('article', attrs={'class':'x-shelf__item has--category js--shelf-item'})
#print(body_splash.prettify())
#  #  #  #

# RASPANDO TODOS OS PRODUTOS #
for produto in antitranspirante:

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
dados.to_csv('jequiti/antitranspirante/antitranspirante.csv', index=False)
#  #  #  #