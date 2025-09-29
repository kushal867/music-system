from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Song, Favorite


# Home page - show all songs
def home(request):
    songs = Song.objects.all().order_by('-uploaded_at')
    return render(request, 'home.html', {'songs': songs})


# Add a song to favorites
@login_required
def add_favorite(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    Favorite.objects.get_or_create(user=request.user, song=song)
    return redirect('my_favorites')


# Show user favorites
@login_required
def my_favorites(request):
    favorites = Favorite.objects.filter(user=request.user).select_related('song')
    return render(request, 'favorites.html', {'favorites': favorites})


# Remove from favorites
@login_required
def remove_favorite(request, song_id):
    fav = Favorite.objects.filter(user=request.user, song_id=song_id)
    if fav.exists():
        fav.delete()
    return redirect('my_favorites')


# ✅ Custom Logout
@login_required
def logout_view(request):
    logout(request)
    return redirect('home')
