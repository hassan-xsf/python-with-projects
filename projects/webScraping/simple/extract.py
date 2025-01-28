import requests
from fake_useragent import UserAgent
from concurrent.futures import ThreadPoolExecutor
import uuid
from bs4 import BeautifulSoup

MAX_PAGES = 1

# scrapURL = "https://czone.com.pk/laptops-pakistan-ppt.74.aspx"

scrapURL = "https://www.olx.com.pk/mobiles_c1411"
session = requests.Session()
headers = {
    'User-Agent': UserAgent().random,
    'Referer': 'https://www.google.com/',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Accept-Encoding': 'gzip, deflate, br'
}


def scrapWeb(url, page = 0):
    try:
        name = f"{uuid.uuid4()}_page_{page}"
        response = session.get(f"{url}?page={page}" , headers=headers)
        response.raise_for_status()
        if(response.status_code != 200):
            return print(f"There was an error: Error Code: {response.status_code}")
        soup = BeautifulSoup(response.content, 'html.parser')
        
        with(open(name + ".html" , "wb") as f):
            f.write(response.content)

        with(open(name + ".txt" , "w") as f):
            print(soup.get_text())
            f.write(soup.get_text())


    except requests.exceptions.RequestException as e:
        print(f"Request failed for {url}: {e}")

if __name__ == "__main__": 
    with ThreadPoolExecutor(max_workers=MAX_PAGES) as executor:
        futures = [executor.submit(scrapWeb, scrapURL, i) for i in range(MAX_PAGES)]

        