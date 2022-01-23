import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.de/Miele-Kaffeevollautomat-Two-Zubereitung-Reinigungsprogramme-Edelstahl-Kegelmahlwerk/dp/B0746Y4DXB/ref=sr_1_1_sspa?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3QUGWKJM7IGGV&keywords=kaffeevollautomat&qid=1638019131&sprefix=kaff%2Caps%2C191&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzREQzUU42MzIxMlhVJmVuY3J5cHRlZElkPUEwMjkzODQ2MzFLUDMySTFWWEJCSSZlbmNyeXB0ZWRBZElkPUEwOTg5NjQzMlI3NjBZQzJMMTJOWSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="

response = requests.get(url)
doc = BeautifulSoup(response.content, "html5lib")

d = doc.findAll('td', attrs={'class': "a-span12",
                                })

print(d)