# Generated by Django 3.2.3 on 2021-05-31 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210531_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
