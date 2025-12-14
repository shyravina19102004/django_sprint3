"""Views для приложения pages."""
from django.shortcuts import render


def about(request):
    """Отображает страницу 'О проекте'."""
    template = 'pages/about.html'
    return render(request, template)


def rules(request):
    """Отображает страницу 'Правила'."""
    template = 'pages/rules.html'
    return render(request, template)