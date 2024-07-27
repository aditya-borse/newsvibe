from django.shortcuts import render
from django.http import HttpResponse
from .models import article
from django.shortcuts import get_object_or_404
def home(request):
    n=7
    n_range = range(n)
    articles = article.objects.all()
    return render(request, "home.html",{'n':articles})

def news(request,pk):
    arti = get_object_or_404(article,pk=pk)
    return render(request,"news.html",{"arti":arti})
# Create your views here.
