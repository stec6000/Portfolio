from django.shortcuts import render
from .models import Album, Photo

def gallery(request):

    albums = Album.objects.all()


    return render(request, 'portfolio/gallery.html', {'albums': albums})

def viewPhoto(request, pk):

    return render(request, 'portfolio/photo.html')