from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    n=2
    n_range = range(n)
    return render(request, "home.html",{'n':n_range})

def news(request,pk):
    return render(request,"news.html")
# Create your views here.
