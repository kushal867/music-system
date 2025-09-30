from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

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


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Logged in successfully 🎵")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # create user
            login(request, user)  # log in after signup
            messages.success(request, "Account created successfully 🎉")
            return redirect('home')
        else:
            messages.error(request, "Error creating account. Please try again.")
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})