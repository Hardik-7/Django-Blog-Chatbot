# Generated by Django 3.1.7 on 2021-04-11 11:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_news_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 11, 16, 38, 26, 607515)),
        ),
    ]