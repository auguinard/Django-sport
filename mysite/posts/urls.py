from django.urls import path, include
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register, name='register'),
    path('online', views.online, name="online"),
]