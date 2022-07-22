from django.contrib import admin
from .models import Movie, User, Watchlist

admin.site.register(Movie)
admin.site.register(User)
admin.site.register(Watchlist)
