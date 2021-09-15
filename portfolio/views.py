from django.shortcuts import render, get_object_or_404
from .models import Album, Photo

def gallery(request):
    album = request.GET.get('album')
    if album == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(album__name__contains=album)

    albums = Album.objects.all()

    return render(request, 'portfolio/gallery.html', {'albums': albums, 'photos':photos})

def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)

    return render(request, 'portfolio/photo.html', {'photo':photo})