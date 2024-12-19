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
            # articlesHtml = soup.find_all('h2', "newsHdng")
            articlesHtml = soup.find_all('div', "news_Itm")
            # print(articlesHtml)
            # print(articlesHtml[2].select('.newsHdng')[0].get_text())
            # print(articlesHtml[2].select('.newsHdng')[0].select('a')[0]['href'])
            # print(articlesHtml[2].select('.news_Itm-img')[0].select('img')[0]['src'])
            # print(articlesHtml[2].select('.newsCont')[0].get_text())
            # print(articlesHtml[2].select('.posted-by')[0].get_text())
            for post in articlesHtml:
            #     pageArticles.append(link.get_text())
                # print(post.select('.newsHdng'))
                tempArticle = []
                if post.select('.newsHdng'):
                    tempArticle.append(post.select('.newsHdng')[0].get_text())
                    tempArticle.append(post.select('.newsHdng')[0].select('a')[0]['href'])
                    tempArticle.append(post.select('.news_Itm-img')[0].select('img')[0]['src'])
                    tempArticle.append(post.select('.newsCont')[0].get_text())
                    tempArticle.append(post.select('.posted-by')[0].get_text())
                    pageArticles.append(tempArticle)

            articles.append(pageArticles)
            index += 1
        else:
            # No More Pages present
            break
    # return articles
    # print(articles)

    with open('ndtv_latest_copy.txt', 'w') as fw:
        for page in articles:
            fw.write(f'Articles in Page:{articles.index(page)+1}\n')
            for article in page:
                fw.write(f'{page.index(article)+1}  {article}\n')
            fw.write("\n")

    
if  __name__ == "__main__":
    get_latest()
    

        
        
    
    