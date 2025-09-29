from django.shortcuts import render, redirect, get_object_or_404
from .models import Song, Favorite
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    songs = Song.objects.all()
    return render(request, 'home.html', {'songs': songs})

@login_required
def add_favorite(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    Favorite.objects.get_or_create(user=request.user, song=song)
    return redirect('home')

@login_required
def my_favorites(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'favorites.html', {'favorites': favorites})