from django.shortcuts import render
import requests as r
from django.contrib import messages

# Create your views here.
def getNews(request):
    if request.method == "POST":
        keyword = request.POST.get('my-search')
    else:
        keyword = 'bikes'
    response = r.get(f'https://newsapi.org/v2/everything?q={keyword}&apiKey=ace489dd71b74e8f9cf8aeedf4c0a864')
    data = response.json()
    if data['status'] == 'ok':
        articles = data['articles']
    else:
        messages.warning(request, 'There is an issue with the news page. Sorry for any inconveniences.')
        articles=[]
    return render(request, 'news/news.html', context={'articles':articles})