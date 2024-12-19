import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
from pick import pick

if  __name__ == "__main__":
    try:
        title = "Please choose which NDTV news you want to download: "
        options = ["Latest", "India", "Opinion", "Cities", "Auto", "India-AI", "Offbeat", "Science", "Feature", "People"]
        option, index = pick(options, title, indicator="=>", default_index=0)
        selected_option = option.lower()

        # start progress
        t = tqdm(unit="", desc=f'{option} headlines loading')
        
        # output_fileName = f'C:\\Users\\Chandu\\Downloads\\ndtv_{selected_option}_news.xlsx'
        output_fileName = f'ndtv_{selected_option}_news_copy.xlsx'
        index = 1
        articles = []

        while(True):
            url = f'http://www.ndtv.com/{selected_option}/page-{str(index)}'
            res = requests.get(url)

            if res.status_code == 200:
                pageArticles = { "Head Line":[], "Short Disc":[], "Posted By":[], "Link":[], "Image":[] }
                soup = BeautifulSoup(res.content, 'html.parser')
                articlesHtml = soup.find_all('div', "news_Itm")

                for link in articlesHtml:
                    if link.select('.newsHdng'):
                        pageArticles["Head Line"].append(link.select('.newsHdng')[0].get_text())
                        pageArticles["Short Disc"].append(link.select('.newsCont')[0].get_text())
                        pageArticles["Posted By"].append(link.select('.posted-by')[0].get_text())
                        pageArticles["Link"].append(link.select('.newsHdng')[0].select('a')[0]['href'])
                        pageArticles["Image"].append(link.select('.news_Itm-img')[0].select('img')[0]['src'])
                        #update progress
                        t.update()
                        # print(pageArticles)
                articles.append(pageArticles)
                index += 1
            else:
                # No More Pages present
                break

        if len(articles)>0:
            with pd.ExcelWriter(output_fileName) as xlsx_writer:
                for page in articles:
                    pageNo = articles.index(page) + 1
                    pd.DataFrame(page).to_excel(xlsx_writer, sheet_name=f'Page {pageNo}', index=False)
            # close progress
            t.close()
            print(f'{option} headlines successfully loaded in {output_fileName}')
        else:
            # close progress
            t.close()
            print(f'There are no {option} headlines to load OR something went wrong to load {option} headlines')

    except Exception as exp:
        # close progress
        t.close()
        print(f'Error: {str(exp)}')
    

        
        
    
    