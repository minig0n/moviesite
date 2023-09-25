from django.urls import path

from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.list_movies, name='index'), # adicione esta linha
    path('<int:movie_id>/', views.detail_movie, name='detail'), # adicione esta linha
]