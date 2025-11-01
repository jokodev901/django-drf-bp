from django.db import models


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Artist(BaseModel):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Album(BaseModel):
    name = models.CharField(max_length=255)
    # Primary "author" artist for the album, a full list of artists can be aggregated from tracks on the album
    primary_artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Genre(BaseModel):
    name = models.CharField(max_length=255)
    # create a sub-genre model?

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Track(BaseModel):
    name = models.CharField(max_length=255)
    number = models.IntegerField() # Track number on associated album
    duration_ms = models.IntegerField() # Track duration in milliseconds
    artist = models.ManyToManyField(Artist, related_name='tracks')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
        constraints = [models.UniqueConstraint(fields=['number', 'album'], name='uniq_album_track_number')] # Add condition=Q(deleted=None) if implementing soft delete

    def __str__(self):
        return self.name

