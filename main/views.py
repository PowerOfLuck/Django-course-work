from django.http import HttpResponse
from django.shortcuts import render
from django.template import context

# Create your views here.
def index(request):
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели - Home',
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст о том почему наш магазин такой ужасный и почему весь товар китайский брак'
    }

    return render(request, 'main/about.html', context)