from django.contrib import admin
from .models import Film, Genre, Direction

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_publ')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    list_display = ('name', )

