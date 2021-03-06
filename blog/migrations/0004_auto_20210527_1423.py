# Generated by Django 3.2.3 on 2021-05-27 08:53

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogpost_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 27, 14, 22, 53, 580017)),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogpost',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
