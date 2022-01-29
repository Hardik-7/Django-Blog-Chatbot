# Generated by Django 3.1.5 on 2021-04-02 15:57

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='head',
        ),
        migrations.AddField(
            model_name='news',
            name='author',
            field=models.CharField(default='Admin', max_length=50),
        ),
        migrations.AddField(
            model_name='news',
            name='author_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='news',
            name='footerline',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AddField(
            model_name='news',
            name='headline_1',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AddField(
            model_name='news',
            name='headline_2',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='news',
            name='news',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='thumbnail',
            field=models.ImageField(blank=True, default='', upload_to='news/images'),
        ),
    ]
