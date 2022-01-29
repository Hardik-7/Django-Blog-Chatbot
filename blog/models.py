from typing import DefaultDict
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import datetime
# Create your models here

class news(models.Model):
    news_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    author=models.CharField(max_length=50, default="Admin")
    author_link=models.URLField(blank=True)
    pub_date = models.DateTimeField(default=datetime.now())
    thumbnail = models.ImageField(upload_to='news_images/', default="",blank=True)
    headline_1= models.CharField(max_length=500, default="",blank=True)
    news = RichTextUploadingField()
    headline_2= models.CharField(max_length=500, default="",blank=True)
    footerline=models.CharField(max_length=500, default="",blank=True)

    

    def __str__(self):
        return self.title
