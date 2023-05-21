from django.shortcuts import render
from django.views.generic import TemplateView

from news.models import Category, FlashNews, Slider


# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menus'] = Category.objects.filter(is_menu=True, is_active=True)
        context['flash_news'] = FlashNews.objects.last()
        context['slider'] = Slider.objects.last()
        return context