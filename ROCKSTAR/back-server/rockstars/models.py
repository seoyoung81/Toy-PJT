from django.db import models

# Create your models here.
class Band(models.Model):
    name = models.CharField(max_length=30)
    group_path = models.TextField()
    
    
class Album(models.Model):
    title = models.CharField(max_length=30)
    genre = models.CharField(max_length=30)
    album_path = models.TextField()
    tracks = models.IntegerField()
    bands = models.ForeignKey("Band", on_delete=models.CASCADE)

class Track(models.Model):
    album = models.ForeignKey("Album", on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    lyrics = models.TextField()
    running_time = models.TimeField()
    composer = models.CharField(max_length=30)
    lyricist = models.CharField(max_length=30)
    
class Community(models.Model):
    band = models.ForeignKey("Band", on_delete=models.CASCADE)
    contemt = models.TextField()