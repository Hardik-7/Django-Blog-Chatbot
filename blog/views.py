from django.core import paginator
from django.shortcuts import render
import os
from blog.models import news
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse
from django.core.paginator import Paginator



def home(request):
    newspost = news.objects.all().order_by('-pub_date')
  
  
    


    #newspost  = news.objects.all().order_by('news_id')
    #paginator=Paginator(newspost,3)
    #page_number=request.GET.get('page')
    #page_obj=paginator.get_page(page_number)
    return render(request, 'home_blog.html',{'newspost':newspost})
    


def newspost(request, id):
    post = news.objects.filter(news_id=id)[0]
    return render(request, 'newspost.html', {'post': post})


def collagenews(request):
    url = "https://timesofindia.indiatimes.com/topic/GTU/news"

    r = requests.get(url)
    htmlContent = r.content
    soup = BeautifulSoup(htmlContent, 'html.parser')
    paras3 = soup.findAll('div', attrs={'class': 'content'})

    link_start = "https://timesofindia.indiatimes.com"
    paras = {}


    for data in paras3:
      title = data.find('span').text
      link = data.find('a')['href']
      description = data.find('p').text
      pubdate=data.find('span',attrs={'class': 'meta'}).text
      link = (link_start+link)
      paras[link] = title + ":" + description + ":" + pubdate 
    
    context = {
      "paras":paras,
    }
    return render(request, 'newscollage.html', context)
