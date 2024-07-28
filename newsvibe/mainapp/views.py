from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import article
from django.shortcuts import get_object_or_404
from .scrapper import scrape_main
import random
def home(request):
    articles = article.objects.all()
    return render(request, "home.html",{'n':articles})

def load_news(request):
    news_url =  "https://www.thehindu.com/news/"
    articles = scrape_main(news_url)
    news2_url = "https://www.newscientist.com/subject/technology/"
    articles2 = scrape_main(news2_url)
    for arti in articles:
        if arti is None: continue
        ar = article.objects.create(
            title = arti['title'],
            description = arti['description'],
            thumbnail_link = arti['thumbnail_link'],
            link = arti['link']
        )
        ar.save()
    for arti in articles2:
        if arti is None: continue
        ar = article.objects.create(
            title = arti['title'],
            description = arti['description'],
            thumbnail_link = arti['thumbnail_link'],
            link = arti['link']
        )
        ar.save()
    return redirect('home')

def news(request,pk):
    arti = get_object_or_404(article,pk=pk)
    return render(request,"news.html",{"arti":arti})
# Create your views here.
