from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная страница',
    }
    return render(request, 'developer/index.html', context=data)


def about(request):
    data = {
        'title': 'О сайте',
    }
    return render(request, 'developer/about.html', context=data)