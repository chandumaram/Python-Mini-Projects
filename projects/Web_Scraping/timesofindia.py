import requests
from bs4 import BeautifulSoup
def timesofindia():
    # url = "https://timesofindia.indiatimes.com/home/headlines"
    url = "https://timesofindia.indiatimes.com/india"
    page_request = requests.get(url)
    data = page_request.content
    soup = BeautifulSoup(data,"html.parser")

    counter = 0
    for divtag in soup.find_all('div', {'class': 'headlines-list'}):
        for ultag in divtag.find_all('ul', {'class': 'clearfix'}):
            if (counter <= 10):
                for litag in ultag.find_all('li'):
                    counter = counter + 1
                    print(str(counter) + " - https://timesofindia.indiatimes.com" + litag.find('a')['href'])
                    #print(str(counter) + "." + litag.text + " - https://timesofindia.indiatimes.com" + litag.find('a')['href'])

if __name__ == "__main__":
    timesofindia()