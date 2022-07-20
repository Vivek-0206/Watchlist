from django.urls import path
from .views import movie_list, movie_detail, add_movie, delete_movie, edit_movie

urlpatterns = [
    path('movies/', movie_list, name='movie_list'),
    path('movies/<int:pk>/', movie_detail, name='movie_detail'),
    path('movies/add_movie/', add_movie, name='add_movie'),
    path('movies/edit_movie/<int:pk>/', edit_movie, name='edit_movie'),
    path('movies/delete_movie/<int:pk>/', delete_movie, name='delete_movie'),
]
