import requests
from bs4 import BeautifulSoup

def get_latest():
    index = 1
    articles = []
    while(True):
        url = 'http://www.ndtv.com/latest/page-'+str(index)
        res = requests.get(url)
        if res.status_code == 200:
            # print(url, res)
            pageArticles = []
            soup = BeautifulSoup(res.content, 'html.parser')
            articlesHtml = soup.find_all('h2', "newsHdng")
            for link in articlesHtml:
                pageArticles.append(link.get_text())

            articles.append(pageArticles)
            index += 1
        else:
            # No More Pages present
            break
    # return articles
    # print(articles)

    with open('ndtv_latest.txt', 'w') as fw:
        for page in articles:
            fw.write(f'Articles in Page:{articles.index(page)+1}\n')
            for article in page:
                fw.write(f'{page.index(article)+1}  {article}\n')
            fw.write("\n")

    
if  __name__ == "__main__":
    get_latest()
    

        
        
    
    