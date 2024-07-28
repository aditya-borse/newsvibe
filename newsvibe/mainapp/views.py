from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import article
from django.shortcuts import get_object_or_404
from .scrapper import scrape_main
from django.core.paginator import Paginator
def home(request):
    articles = article.objects.all()
    paginator = Paginator(articles,10)
    news_page = request.GET.get('page',1)
    page_obj = paginator.get_page(news_page)
    try :
        page_obj = paginator.page(news_page)
    except Exception as E:
        news_page =1
        page_obj = paginator.page(news_page)
    return render(request, "home.html",{'n':page_obj})

def load_news(request):
    news_url =  "https://www.thehindu.com/news/"
    articles = scrape_main(news_url)
    news2_url = "https://www.newscientist.com/subject/technology/"
    articles2 = scrape_main(news2_url)
   
    for arti in articles2:
        if arti is None: continue
        
        ar = article.objects.create(
            title = arti['title'],
            description = arti['description'],
            thumbnail_link = arti['thumbnail_link'],
            link = arti['link'],
            summary = arti['summary'],
            sentiment = arti['emotion']
            
        )
        ar.save()
    for arti in articles:
        if arti is None: continue
        ar = article.objects.create(
            title = arti['title'],
            description = arti['description'],
            thumbnail_link = arti['thumbnail_link'],
            link = arti['link'],
            summary = arti['summary'],
            sentiment = arti['emotion']
        )
        ar.save()
        print(arti['emotion'])
    return redirect('home')

def news(request,pk):
    arti = get_object_or_404(article,pk=pk)
    return render(request,"news.html",{"arti":arti})
# Create your views here.
