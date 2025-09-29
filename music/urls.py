from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('favorites/', views.my_favorites, name='favorites'),
    path('add-favorite/<int:song_id>/', views.add_favorite, name='add_favorite'),
]