from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import MovieForm
from .models import Movie


def movies(request):
    return render(request, 'movie_list.html', {'movies': Movie.objects.all()})


def movie_detail(request, movie_id=None):
    return render(request, 'movie_detail.html', {'movie': Movie.objects.get(id=movie_id)})


def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies_list')  # Replace 'movies_list' with the URL name for the movie list page
    else:
        form = MovieForm()

    return render(request, 'movie_add.html', {'form': form})
