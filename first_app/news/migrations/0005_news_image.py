# Generated by Django 4.0.6 on 2022-11-14 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_likes_news_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='news_images/'),
        ),
    ]