# Generated by Django 3.1.7 on 2021-04-18 20:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20210419_0223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 19, 2, 26, 17, 278036)),
        ),
    ]
