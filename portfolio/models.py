from django.db import models


class Album(models.Model):

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class Photo(models.Model):
    
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    album = models.OneToOneField(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.name