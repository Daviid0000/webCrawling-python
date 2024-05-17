from bs4 import BeautifulSoup
import requests
import pprint

URL = "https://www.netflix.com/ar/"

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")

etiqueta_A = soup.find_all("a")

textos = {}

for a in etiqueta_A:
    resto_de_url = a.get("href")
    
    urlFinal = URL + resto_de_url
    print(f"URL a la que se hará la petición: {urlFinal}")

    response2 = requests.get(urlFinal)

    soup2 = BeautifulSoup(response2.text, "html.parser")

    etiqueta_h1 = soup2.find_all("h1")
    etiqueta_p = soup2.find_all("p")

    texto_combinado = [str(tag) for tag in etiqueta_h1 + etiqueta_p]

    textos[urlFinal] = texto_combinado


pprint.pprint(textos)

