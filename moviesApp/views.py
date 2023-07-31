from django.shortcuts import render, get_object_or_404
from .models import Movie


def movies(request):
    return render(request, 'movie_list.html', {'movies': Movie.objects.all()})


def movie_detail(request, pk=None):
    movie = get_object_or_404(Movie, id=pk)
    return render(request, 'movie_detail.html', {'movie': movie})
