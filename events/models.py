import datetime

from django.db import models


class Event(models.Model):
    datetime = models.DateTimeField(null=False)
    movie = models.ForeignKey(
        'movies.Movie', on_delete=models.CASCADE
    )
    cinema = models.ForeignKey(
        'cinemas.Cinema', on_delete=models.CASCADE
    )

    @property
    def get_data(self):
        return {
            'id': self.pk,
            'movie': self.movie.get_data,
            'datetime': self.datetime,
            'cinema': self.cinema.name
        }

    @property
    def old(self):
        """
        Returns True if the event has passed.
        False if it's a future event.
        """
        return datetime.datetime.now() < self.datetime

    @property
    def time(self):
        return f"{self.datetime.hour}:{self.datetime.minute}"

    @property
    def scheduled(self) -> str:
        return f"<a href='{self.movie.image}'>{self.time}</a>"
