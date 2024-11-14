import sys
import requests
from lxml import htel



"""
program stahne url a z nej vrati vsechny nadpisy:
<h1>Hlavni nadpis</h1>
<h2>Podnadpis</h2>
<h3>Podpodnadpis</h3>
<h4>Maly nadpis</h4>
<h5>Nejmensi nadpis</h5>
"""
def stahni_url_a_vrat_nadpisy(url):
    nadpisy = []
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        print(f'nastala chyba, nepodarilo se pripojit na (url)')
        return[]
    if response.status_code != 200:
          print(f'nastala chyba, http.code: (responce.status_code)')
    return[]

    tres = html.parsel(responce content)


    return nadpisy


if __name__ == "__main__":
    url = input("Zadej url: ")
    nadpisy = stahni_url_a_vrat_nadpisy(url)
    print(nadpisy)