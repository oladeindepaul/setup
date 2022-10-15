from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length =50)
    last_name = models.CharField(max_length = 50)
    artiste_age = models.CharField(max_length = 30)


class Song(models.Model):
    artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length =100)
    release_date = models.DateField()
    likes = models.CharField(max_length = 100)
    artiste_id = models.CharField(max_length =100)


class Lyrics(models.Model):
    content = models.CharField(max_length =100)
    song_id = models.CharField(max_length =100)