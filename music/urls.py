from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('favorites/', views.my_favorites, name='favorites'),
    path('add-favorite/<int:song_id>/', views.add_favorite, name='add_favorite'),
    path('remove-favorite/<int:song_id>/', views.remove_favorite, name='remove_favorite'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),     
    path('signup/', views.signup_view, name='signup'),   
]
