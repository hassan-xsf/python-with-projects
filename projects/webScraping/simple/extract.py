import requests
from fake_useragent import UserAgent
from concurrent.futures import ThreadPoolExecutor , as_completed
import uuid
from bs4 import BeautifulSoup
from openpyxl import Workbook

MAX_PAGES = 50

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
        response = session.get(f"{url}?page={page}" , headers=headers)
        response.raise_for_status()
        if(response.status_code != 200):
            return print(f"There was an error: Error Code: {response.status_code}")
        
        if not response.content:
            return print("Invalid content found")
        soup = BeautifulSoup(response.content, 'html.parser')
        
        listings = soup.find_all("li" , attrs={"aria-label": "Listing"})
        data = []
        for listing in listings:
            title = listing.find("a").get("title")
            link = listing.find("a").get("href")
            price = listing.find("div", attrs={"aria-label": "Price"}).find("span").text
            location = listing.find("span", attrs={"aria-label": "Location"}).text
            product = {
                "title" : title,
                "link"  : f"https://www.olx.com.pk{link}",
                "price" : price,
                "location" : location,
                "page": page
            }
            data.append(product)

        return data
    except requests.exceptions.RequestException as e:
        print(f"Request failed for {url}: {e}")

if __name__ == "__main__": 
    with ThreadPoolExecutor(max_workers=MAX_PAGES) as executor:
        uFutures = [executor.submit(scrapWeb, scrapURL, i) for i in range(MAX_PAGES)]
        wb = Workbook()
        ws = wb.active
        ws.append(["title" , "link" , "price" , "location" , "page"])
        for future in as_completed(uFutures):
            try:
                result = future.result()
                for r in result:
                    ws.append([r["title"] , r["link"] , r["price"] , r["location"] , r["page"]])
            except Exception as e:
                print(f"Error occurred: {e}")
        wb.save(f"olx_{uuid.uuid4()}.xlsx")