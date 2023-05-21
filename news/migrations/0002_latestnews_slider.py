# Generated by Django 4.2.1 on 2023-05-20 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LatestNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='latestNews/')),
                ('timestamp', models.TimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='slider/')),
                ('news_type', models.CharField(blank=True, max_length=30, null=True)),
                ('news_desc', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
