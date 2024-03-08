from django.urls import path
from .views import login, logout, register, profile

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
]