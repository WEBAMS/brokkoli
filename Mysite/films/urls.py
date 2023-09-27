from django.urls import path
from . import views

urlpatterns = [
    path('', views.FilmsView.as_view()),
    path('<slug:slug>/', views.FilmDetail.as_view())
]