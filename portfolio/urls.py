from django.urls import path
from . import views

#app_name = 'portfolio'

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),
]