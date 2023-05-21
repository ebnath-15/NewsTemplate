from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    is_menu = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class FlashNews(models.Model):
    title = models.CharField(max_length=250)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Slider(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='slider/')
    news_type = models.CharField(max_length=30, null=True, blank=True)
    news_desc = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
