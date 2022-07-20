from django.http import JsonResponse
from .models import Movie
from django.views.decorators.csrf import csrf_exempt


def movie_list(request):
    movies = list(Movie.objects.filter().values())
    data = {
        'movies': movies
    }
    return JsonResponse(data)


def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    data = {
        "id": movie.id,
        "name": movie.name,
        "description": movie.description,
        "is_active": movie.is_active,
        "created_at": movie.created_at,
        "updated_at": movie.updated_at,
    }
    return JsonResponse(data)


@csrf_exempt
def add_movie(request):
    if request.method == 'POST':
        data = request.POST
        print('data: ', data)
        movie = Movie(
            name=data['name'], description=data['description'], is_active=data['is_active'])
        movie.save()
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'})


@csrf_exempt
def edit_movie(request, pk):
    if request.method == 'POST':
        data = request.POST
        movie = Movie.objects.get(pk=pk)
        movie.name = data['name']
        movie.description = data['description']
        movie.is_active = data['is_active']
        movie.save()
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'})


def delete_movie(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return JsonResponse({'status': 'ok'})
