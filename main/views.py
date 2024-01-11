from django.http import HttpResponse
from django.shortcuts import render
from django.template import context

# Create your views here.
def index(request):
    context: dict[str, str] = {
        'title': 'Home',
        'content': 'Главная страница магазина - Home',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'is_authenticated': False
    }

    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse('About page')