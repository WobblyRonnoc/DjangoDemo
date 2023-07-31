from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movies, name='movie_list'),
    path('movies/<int:pk>/', views.movie_detail, name='movie_detail'),
]
