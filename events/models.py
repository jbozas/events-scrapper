from django.db import models


class Event(models.Model):
    datetime = models.DateTimeField(null=False)
    movie = models.ForeignKey(
        'movies.Movie', on_delete=models.CASCADE
    )
    cinema = models.ForeignKey(
        'cinemas.Cinema', on_delete=models.CASCADE
    )
