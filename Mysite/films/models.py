from django.db import models

class Genre(models.Model):
    '''жанры фильмов'''
    name = models.CharField('Название жанра', max_length=50)
    description = models.TextField('Описание', blank=True)
    url = models.SlugField(max_length=50, unique=True) # SlugField отвечает за адрес страницы, unique - уникальная

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

class Direction(models.Model):
    '''Режиссеры'''
    name = models.CharField('Фамилия и Имя', max_length=100)
    description = models.TextField('Биография', blank=True)
    image = models.ImageField('Фотография', upload_to='image/directions/%Y')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Режиссер'
        verbose_name_plural = 'Режиссеры'

class Film(models.Model):
    '''информация о фильме'''
    title = models.CharField('Название фильма', max_length = 100)
    imag = models.ImageField('Постер', upload_to='image/&Y')
    description = models.TextField(blank=True)
    date_publ = models.DateField('Дата выхода')
    directions = models.ManyToManyField(Direction, verbose_name='Режиссеры')
    genre = models.ManyToManyField(Genre, verbose_name='Жанры')
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.title}, {self.date_publ}'