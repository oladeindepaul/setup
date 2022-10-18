from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length =50)
    last_name = models.CharField(max_length = 50)
    artiste_age = models.CharField(max_length = 30)

    def __str__(self):
        return f"{self.first_name + self.last_name + self.artiste_age}"

class Song(models.Model):
    artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length =100)
    release_date = models.DateField('date released')
    likes = models.CharField(max_length = 100)
    artist_id = models.CharField(max_length =100)

    def __str__(self):
        return f"{self.artiste, self.title,  self.release_date,  self.likes,  self.artiste_id}"


class Lyrics(models.Model):
    content = models.CharField(max_length =100)
    song_id = models.CharField(max_length =100)

    def __str__(self):
        return f"{self.content + self.song_id}"
