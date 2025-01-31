from bs4 import BeautifulSoup
import uuid

def main():
    with(open("smiu-sitemap.xml", "r") as f):
        soup = BeautifulSoup(f.read(), 'html.parser')
        urls = soup.find_all("url")

        allURLS = []
        for u in urls:
            allURLS.append(u.find("loc").text)

        with(open(str(uuid.uuid4()) + ".txt" , "w") as wf):
            wf.write(str(allURLS))

if __name__ == "__main__":
    main()