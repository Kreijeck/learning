import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.cdkeys.com/de_de/cyberpunk-2077-gog-pc")

doc = BeautifulSoup(r.text, "html.parser")

d = doc.find(id="product-price-3419")

print(d)

r = requests.get("https://www.amazon.de/dp/B07TY2KB7R/ref=cm_sw_r_wa_apa_fabc_RUj7FbND7795W?_encoding=UTF8&psc=1")

doc = BeautifulSoup(r.text, "html.parser")

#d = doc.find(id="priceblock_ourprice_row")
d = doc

print(d)



