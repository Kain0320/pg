import requests
from bs4 import BeautifulSoup

def download_url_and_get_all_hrefs(url):
    try:
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Chyba: Server vrátil kód {response.status_code}")
            return []

        soup = BeautifulSoup(response.content, 'html.parser')
        
       
        hrefs = [a.get('href') for a in soup.find_all('a', href=True)]
    
        return hrefs
    
    except Exception as e:
        print(f"Chyba při zpracování stránky: {e}")
        return []
if __name__ == "__main__":
    url = "https://www.jcu.cz"
    print(f"Stahuji odkazy z URL: {url}")
    links = download_url_and_get_all_hrefs(url)
    if links:
        print("Nalezené odkazy:")
        for link in links:
            print(link)
    else:
        print("Žádné odkazy nebyly nalezeny.")




