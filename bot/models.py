
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
from datetime import datetime    

now = timezone.now()

class contact(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=50)
  email = models.EmailField(max_length=50)
  phone = models.IntegerField()
  desc = models.CharField(max_length=200,null=True, blank=True)

  
class FAQ(models.Model):
  id=models.AutoField(primary_key=True)
  question=models.CharField(max_length=300,default='')
  
  question_type=models.CharField(max_length=50,default='')
  pub_date = models.DateTimeField(default=datetime.now())
  keyword_1=models.CharField(max_length=300, default="")
  keyword_2=models.CharField(max_length=300, default="")
  keyword_3=models.CharField(max_length=300, default="")
  keyword_4=models.CharField(max_length=300, default="",blank=True)
  keyword_5=models.CharField(max_length=300, default="",blank=True)
  
  Answer= RichTextUploadingField(default="")
  link=models.URLField(blank=True)

class Questions(models.Model):
  id=models.AutoField(primary_key=True)
  ask_query=models.CharField(max_length=300,default='')
  