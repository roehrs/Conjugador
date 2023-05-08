import requests
from bs4 import BeautifulSoup

# URL do site
base = 'https://conjugacao.reverso.net/conjugacao-ingles-verbo-'
verb = input("Qual o verbo a ser pesquisado: ")
url = base + verb + '.html'
tense = input("Qual o tempo verbal: ")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68"}


# Faz a requisição para a página
response = requests.get(url, headers=headers)

# Cria o objeto BeautifulSoup
site = BeautifulSoup(response.text, 'html.parser')

pesquisa = site.find_all('div', class_='blue-box-wrap')

i = 0
j = 0

while i < 12:
    if (pesquisa[i].contents[0].text) == tense:
        print(pesquisa[i].contents[0].text)
        while j < 6:
            print(pesquisa[i].contents[1].contents[j].text)
            j = j + 1
        break
    i = i + 1
