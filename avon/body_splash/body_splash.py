# BIBLIOTECAS #
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
url.get('https://www.avon.com.br/s/body%20splash?map=term')
#  #  #  #

sleep(4)

dados_produtos = []

# ROLANDO PAGINA + VER MAIS #
ActionChains(url).scroll(0, 0, 0, 1000).perform()
sleep(3)

carregar_mais = url.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div[3]/div[2]/div/a')
carregar_mais.click()

sleep(2)
#  #  #  #

# PARSER HTML #
conteudo_pagina = url.page_source
soup = BeautifulSoup(conteudo_pagina, 'html.parser')
#  #  #  #

# TAG MAE #
body_splash = soup.findAll('div', attrs={'class': 'css-1y7l0uq'})
#print(produtos.prettify())
#  #  #  #

# RASPANDO TODOS OS PRODUTOS #
for produto in body_splash:

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
dados.to_csv('avon/body_splash/bodysplash.csv', index=False)
#  #  #  #
