from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


def platform_tmpl(request):
    title = 'Главная'
    page = 'Главная страница'
    context = {
        'title': title,
        'page': page
    }
    return render(request, 'fourth_task/platform.html', context)


def cart_tmpl(request):
    title = 'Корзина'
    page = 'Корзина'
    context = {
        'title': title,
        'page': page
    }
    return render(request, 'fourth_task/cart.html', context)


def games_tmpl(request):
    title = 'Магазин'
    page = 'Игры'
    context = {
        'title': title,
        'page': page,
        'games': ['GTA 6', "Assassin's Creed: Shadows", 'God of War']
    }
    return render(request, 'fourth_task/games.html', context)