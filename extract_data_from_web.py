from bs4 import BeautifulSoup
from urllib.request import urlopen
url = "https://books.toscrape.com/"
html=urlopen(url)
soup =BeautifulSoup(html,"html.parser")
type(soup)
al_links=soup.findAll('h3')
str_cells=str(al_links)
clear_text=BeautifulSoup(str_cells,"html.parser").get_text()
print(clear_text)

