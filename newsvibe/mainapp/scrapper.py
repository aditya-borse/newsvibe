import requests
from bs4 import BeautifulSoup

def scrape_main_page(url):
    articles = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for item in soup.find_all(class_='element'):
        
        asf = item.find('h3',class_='title')
        
        link = asf.find('a')['href']

        articles.append({
            'link' :link,
        })
        
    return articles

def scrape_news(article_url):
    response = requests.get(article_url)
    soup = BeautifulSoup(response.text,'html.parser')
    title = soup.find('h1',class_='title').text
    description = soup.find('h2',class_='sub-title').text
    thumbnail = soup.find('img',class_='lead-img')
    if thumbnail is None:
        thumbnail_link = "https://www.searchenginejournal.com/wp-content/uploads/2024/02/17-65cc9410738f7-sej.png"
    else: thumbnail_link = thumbnail['src'] 
    return {
        'title' : title, 
        'description':description,
        'thumbnail_link':thumbnail_link,
    }




def scrape_main(news_url):
    articles = scrape_main_page(news_url)
    for arti in articles:
        if arti == None: continue

        article_data  = scrape_news(arti['link'])
        arti.update(article_data)

    return articles
       
    # print(article_data)

# for article in articles:
#     print(article['title'], article['link'], article['description'], article['thumbnail_link'])
news_url = "https://www.thehindu.com/news/"
scrape_main(news_url)