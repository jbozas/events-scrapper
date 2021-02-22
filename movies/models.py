from django.db import models


class Movie(models.Model):
    """
    Class in charge of storing the movie information
    scrapped from cinemas.
    """

    title = models.CharField(max_length=200, unique=True)
    director = models.CharField(max_length=200, blank=True)
    image = models.ImageField(blank=True)
    preview = models.CharField(max_length=200, blank=True)
    trailer = models.CharField(max_length=200, blank=True)

    @property
    def get_data(self):
        return {
            'title': self.title,
            'image': self.image,
        }
