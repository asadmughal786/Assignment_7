from django.urls import path
from . import views
urlpatterns = [
    path('signin/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]
