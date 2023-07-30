from django.urls import path
from . import views

urlpatterns = [
    path('', views.movies, name='movie_index'),
    path('movies/', views.movies, name='movie_list'),
    path('movies/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('movies/add/', views.add_movie, name='add_movie'),
]
