import email
from django.http import JsonResponse
from .models import Movie, User, Watchlist
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
        "name": movie.name,
        "description": movie.description,
        "is_active": movie.is_active,
        "updated_at": movie.updated_at,
    }
    return JsonResponse(data)


@csrf_exempt
def add_movie(request):
    if request.method == 'POST':
        data = request.POST
        user = User.objects.filter(email=data['email'])
        if user.exists():
            if User.check_password(user, data['password']):
                movie = Movie(
                    name=data['name'], description=data['description'], is_active=data['is_active'])
                movie.save()
                return JsonResponse({'status': 'Movie Added'})
            else:
                return JsonResponse({'status': 'error check the credentials'})
        else:
            return JsonResponse({'status': 'error check the credentials'})
    return JsonResponse({'status': 'error'})


@csrf_exempt
def edit_movie(request, pk):
    if request.method == 'POST':
        data = request.POST
        user = User.objects.filter(email=data['email'])
        if user.exists():
            if User.check_password(user, data['password']):
                movie = Movie.objects.get(pk=pk)
                movie.name = data['name']
                movie.description = data['description']
                movie.is_active = data['is_active']
                movie.save()
                return JsonResponse({'status': 'Movie Updated'})
            else:
                return JsonResponse({'status': 'error check the credentials'})
        else:
            return JsonResponse({'status': 'error check the credentials'})
    return JsonResponse({'status': 'error'})


@csrf_exempt
def delete_movie(request, pk):
    if request.method == 'POST':
        data = request.POST
        user = User.objects.filter(email=data['email'])
        if user.exists():
            if User.check_password(user, data['password']):
                movie = Movie.objects.get(pk=pk).exists()
                if movie:
                    movie.is_deleted = True
                    return JsonResponse({'status': 'Movie Deleted'})
                else:
                    return JsonResponse({'status': 'Movie not found'})
            else:
                return JsonResponse({'status': 'error check the credentials'})
        else:
            return JsonResponse({'status': 'error check the credentials'})
    return JsonResponse({'status': 'error'})


@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = request.POST
        if User.objects.filter(email=data['email']).exists():
            return JsonResponse({'status': 'error user exists'})
        if data['password'] != data['confirm_password']:
            return JsonResponse({'status': 'error password mismatch'})

        user = User.objects.create_user(
            name=data['name'], email=data['email'], password=data['password'])
        return JsonResponse({'status': 'User Created', 'name': user.name, 'email': user.email})
    return JsonResponse({'status': 'error'})


@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = request.POST
        user = User.objects.filter(email=data['email'])
        if user.exists():
            if User.check_password(user, data['password']):
                return JsonResponse({'status': 'Login Successful', 'name': user.name, 'email': user.email})
            else:
                return JsonResponse({'status': 'error check the credentials'})
        else:
            return JsonResponse({'status': 'error check the credentials'})
    return JsonResponse({'status': 'error'})


@csrf_exempt
def create_watchlist(request):
    if request.method == 'POST':
        data = request.POST
        user = User.objects.filter(email=data['email'])
        if user.exists():
            if User.check_password(user, data['password']):
                movie = Movie.objects.filter(id=data['movie_id'])
                if movie.exists():
                    movie = Movie.objects.get(id=data['movie_id'])
                    watchlist = Watchlist.objects.filter(
                        user=user, movie=movie)
                    if watchlist.exists():
                        return JsonResponse({'status': 'Watchlist already exists'})
                    else:
                        watchlist = Watchlist(user=user, movie=movie)
                        watchlist.save()
                        return JsonResponse({'status': 'New watchlist created'})
                else:
                    return JsonResponse({'status': 'Movie not found'})
            else:
                return JsonResponse({'status': 'error check the credentials'})
        else:
            return JsonResponse({'status': 'error check the credentials'})
    return JsonResponse({'status': 'error'})


@csrf_exempt
def get_user_watchlists(request):
    if request.method == 'POST':
        data = request.POST
        user = User.objects.filter(email=data['email'])
        if user.exists():
            if User.check_password(user, data['password']):
                watchlist = list(Watchlist.objects.filter(user=user, is_deleted=False).values(
                    'movie__id', 'movie__name', 'movie__description', 'user__name'))

                user_watchlists = []
                for item in watchlist:
                    user_watchlists.append({
                        'id': item['movie__id'],
                        'movie_name': item['movie__name'],
                        'movie_description': item['movie__description'],
                        'user_name': item['user__name']
                    })
                return JsonResponse({'status': 'ok', 'user_watchlists': user_watchlists[::-1]})
            else:
                return JsonResponse({'status': 'error check the credentials'})
        else:
            return JsonResponse({'status': 'error check the credentials'})
    return JsonResponse({'status': 'error'})


@csrf_exempt
def delete_watchlist(request):
    if request.method == 'POST':
        data = request.POST
        user = User.objects.filter(email=data['email'])
        if user.exists():
            if User.check_password(user, data['password']):
                if Watchlist.objects.filter(id=data['movie_id']).exists():
                    watchlist = Watchlist.objects.get(id=data['movie_id'])
                    watchlist.is_deleted = True
                    return JsonResponse({'status': 'ok'})
                else:
                    return JsonResponse({'status': 'error watchlist not found'})
            else:
                return JsonResponse({'status': 'error check the credentials'})
        else:
            return JsonResponse({'status': 'error check the credentials'})
    return JsonResponse({'status': 'error'})
