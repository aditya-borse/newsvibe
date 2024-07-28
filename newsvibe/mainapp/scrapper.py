import requests
from bs4 import BeautifulSoup
from .summarizer import summarize_text

def scrape_main_page(url):
    articles = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    if url == "https://www.thehindu.com/news/":
        for item in soup.find_all(class_='element'):
            
            asf = item.find('h3',class_='title')
            
            link = asf.find('a')['href']

            articles.append({
                'link' :link,
            })
    else:
        base_url = "https://www.newscientist.com"
        for item in soup.find_all('a',class_="CardLink"):
           
           link = item['href']
           abs_url = base_url+link
           articles.append({
               'link':abs_url,
           })
    return articles

def scrape_news_hindu(article_url):
    response = requests.get(article_url)
    soup = BeautifulSoup(response.text,'html.parser')
   
    title = soup.find('h1',class_='title').text
    description = soup.find('h2',class_='sub-title').text
    
    content = soup.find('div',class_="articlebodycontent col-xl-9 col-lg-12 col-md-12 col-sm-12 col-12")
    te="fail"
    if content == None:
        pass
    else:
        para = content.find_all('p')
        te = ' '.join([p.get_text()  for p in para])
        te = summarize_text(te)
        te = te['summary']
    thumbnail = soup.find('source')
    if thumbnail is None:
        thumbnail_link = "https://www.searchenginejournal.com/wp-content/uploads/2024/02/17-65cc9410738f7-sej.png"
    else: thumbnail_link = thumbnail['srcset'] 
    return{
            'title':title,
            'description':description,
            'thumbnail_link':thumbnail_link,
            'summary':te,
        }
     
def scrape_news_nt(article_url):
        response = requests.get(article_url)
        soup = BeautifulSoup(response.text,'html.parser')
        title_element = soup.find('h1',class_="ArticleHeader__Heading")
        title = title_element.text if title_element else "No title found"
        description_element = soup.find('p',class_="ArticleHeader__Copy")
        description = description_element.text if description_element else "No description found"
        thumbnail = soup.find('img',class_="Image")
        content = soup.find('section',class_="ArticleContent js-article-content")
        te = "fail"
        if content:
            para = content.find_all('p')
            te = ' '.join([p.get_text() for p in para])
            te = summarize_text(te)
            te =te['summary']
            # print(te)
        if thumbnail == None:
             thumbnail_link = "https://www.searchenginejournal.com/wp-content/uploads/2024/02/17-65cc9410738f7-sej.png"
        else:
            thumbnail_link = thumbnail['src'] 
        return{
            'title':title,
            'description':description,
            'thumbnail_link':thumbnail_link,
            'summary':te,
        }


def scrape_main(news_url):
    articles = scrape_main_page(news_url)
    if news_url ==  "https://www.thehindu.com/news/":
        for arti in articles:
            if arti == None: continue

            article_data  = scrape_news_hindu(arti['link'])
            arti.update(article_data)
    else:
        for arti in articles:
            if arti == None: continue

            article_data  = scrape_news_nt(arti['link'])
            arti.update(article_data)
    return articles
       
    # print(article_data)

# for article in articles:
#     print(article['title'], article['link'], article['description'], article['thumbnail_link'])
news_url = "https://www.thehindu.com/news/"
news2_url = "https://www.newscientist.com/subject/technology/"
scrape_main(news_url)

scrape_main(news2_url)