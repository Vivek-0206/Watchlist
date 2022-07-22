from django.urls import path
from .views import home_view, movie_list, movie_detail, add_movie, delete_movie, edit_movie, register, login, create_watchlist, delete_watchlist, get_user_watchlists

urlpatterns = [
    path('', home_view, name='api_home'),
    path('api/', home_view, name='api_home'),
    path('api/movies/', movie_list, name='movie_list'),
    path('api/movies/<int:pk>/', movie_detail, name='movie_detail'),
    path('api/movies/add_movie/', add_movie, name='add_movie'),
    path('api/movies/edit_movie/<int:pk>/', edit_movie, name='edit_movie'),
    path('api/movies/delete_movie/<int:pk>/',
         delete_movie, name='delete_movie'),

    path('api/register/', register, name='register'),
    path('api/login/', login, name='login'),
    # path('logout/', logout, name='logout'),

    path('api/create_watchlist/', create_watchlist, name='create_watchlist'),
    path('api/get_user_watchlists/', get_user_watchlists,
         name='get_user_watchlists'),
    path('api/delete_watchlist/<int:pk>/',
         delete_watchlist, name='delete_watchlist'),
]
