from django.shortcuts import render
from django.views.generic.base import View
from .models import Film

class FilmsView(View):
    '''Список фильмов'''
    def get(self, request):
        films = Film.objects.all()
        return render(request, 'films/film.html', {'film_list': films})

class FilmDetail(View):
    '''Представление одного фильма'''
    def get(self, request, slug):
        film = Film.objects.get(url=slug)
        return render(request, 'films/film_detail.html', {'film': film})


