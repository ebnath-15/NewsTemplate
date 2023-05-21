from django.contrib import admin

from news.models import Category, FlashNews, Slider

# Register your models here.

admin.site.register(Category)
admin.site.register(FlashNews)
admin.site.register(Slider)
