from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from .models import *

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


def index(request):
    posts = Main.objects.all()
    return render(request, 'main/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})


def about(request):
    return render(request, 'main/about.html', {'menu': menu, 'title': 'О сайте'})


def categories(request, pageid):
    if (request.GET):
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{pageid}</p>")


def archive(request, year):
    if int(year) > 2022:
        return redirect('Home', permanent=False)

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def pageNotFound(requset, exception):

    return HttpResponseNotFound(f'<h1>Страница не найдена</h1>')
