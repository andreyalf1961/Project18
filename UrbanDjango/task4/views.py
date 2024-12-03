from django.shortcuts import render


# Create your views here.
def platform(request):
    pagename = 'Главная страница'
    context = {'pagename': pagename}
    return render(request, 'fourth_task/platform.html', context)


def shop(request):
    pagename = 'Игры'
    games = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
    context = {'pagename': pagename, 'games': games}
    return render(request, 'fourth_task/games.html', context)


def cart(request):
    pagename = 'Корзина'
    context = {'pagename': pagename}
    return render(request, 'fourth_task/cart.html', context)
