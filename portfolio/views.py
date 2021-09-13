from django.shortcuts import render

def gallery(request):

    return render(request, 'portfolio/gallery.html')

def viewPhoto(request, pk):

    return render(request, 'portfolio/photo.html')