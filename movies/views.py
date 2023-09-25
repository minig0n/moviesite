from django.http import HttpResponse
from .temp_data import movie_data
from django.shortcuts import render

def detail_movie(request, movie_id):
    movie = movie_data[movie_id - 1]
    return HttpResponse(
        f'Detalhes do filme {movie["name"]} ({movie["release_year"]})')

def list_movies(request):
    context = {"movie_list": movie_data}
    return render(request, 'movies/index.html', context)


def detail_movie(request, movie_id):
    context = {'movie': movie_data[movie_id - 1]}
    return render(request, 'movies/detail.html', context)

