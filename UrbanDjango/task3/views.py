from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


def platform_tmpl(request):
    title = 'Главная'
    context = {'title': title}
    return render(request, 'third_task/platform.html', context)


def cart_tmpl(request):
    return render(request, 'third_task/cart.html')


def games_tmpl(request):
    context = {
        'game_1': 'GTA 6',
        'game_2': "Assassin's Creed: Shadows",
        'game_3': 'God of War'
    }
    return render(request, 'third_task/games.html', context)
