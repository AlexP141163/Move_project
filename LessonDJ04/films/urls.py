from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('films/', views.movies, name='films'),
    path('create_films/', views.create_films, name='add_films')
]