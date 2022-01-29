from django.db.models.expressions import OrderBy
from django.shortcuts import render,HttpResponse
from .models import Questions, contact
from django.contrib import messages
from .models import FAQ
from django.db.models import Q 

import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from autocorrect import spell
def home(request):
  
    
  return render(request, 'home.html')
#def searchMatch(mystring, item):
  #if  mystring in item.keyword_1.lower() or mystring in item.keyword_2.lower() or mystring in item.keyword_3.lower():
   # return True
 # else:
   # return False
    

def search(request):
  
  from .models import FAQ
  import operator 
  from functools import reduce
 
  word_list=request.GET['query']
  word_list=word_list.lower()
  tokens = nltk.word_tokenize(word_list)

#remove stop words & punc
  stop = set(stopwords.words('english') + list(string.punctuation))
  words = [w for w in tokens if w not in stop]
  #mystring1 = " ".join(words)
  mystring=' '.join(map(str, words))
  print(mystring)
  
  if word_list:
        query_list = word_list.split()
        allquery =FAQ.objects.filter(
                 reduce(operator.and_, 
                        (Q(keyword_1__icontains=q) for q in query_list)) |
                 reduce(operator.and_,
                        (Q(keyword_2__icontains=q) for q in query_list)) |
                 reduce(operator.and_, 
                        (Q(keyword_3__icontains=q) for q in query_list)) |
                 reduce(operator.and_, 
                        (Q(keyword_4__icontains=q) for q in query_list)) 
                 #reduce(operator.and_, 
                        #(Q(keyword_5__icontains=q) for q in query_list))
             )

    
  #ans = FAQ.objects.filter(Q(keyword_1__icontains=query) | Q(keyword_2__icontains=query) | Q(keyword_3__icontains=query) | Q(keyword_4__icontains=query) | Q(keyword_5__icontains=query))
  #if query.count()==0:
  
#SELECT * FROM blog_table WHERE content LIKE '%first_word%' AND content LIKE '%second_word%' AND content LIKE '%third_word%'
  params={'allquery': allquery}
  
    # If not searched, return default posts
   
  return render(request, 'home.html', params)





  
 # return render(request, 'homes.html')

#def news(request):
 # return render(request, 'news.html')

def Contact(request):
  if request.method == "POST":
    name=request.POST.get('name')
    email=request.POST.get('email')
    phone=request.POST.get('phone')
    desc=request.POST.get('dec')
    obj=contact(name=name,email=email,phone=phone,desc=desc)
    obj.save()
    messages.success(request, name)
  return render(request, 'contact.html')