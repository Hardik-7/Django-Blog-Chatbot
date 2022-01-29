
from django.contrib import admin
from blog.models import news
import requests
# Register your models here.
@admin.register(news)
class postAdmin(admin.ModelAdmin):
    list_display=['news_id','pub_date','title', 'author']
    list_filter = ('pub_date',)
    ordering=['news_id']
    search_fields = ('title','headline_1','news')
    
    