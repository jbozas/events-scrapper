from django.db import models


class Cinema(models.Model):

    name = models.CharField(max_length=100)
    location = models.CharField(null=True, max_length=200)
    description = models.CharField(null=True, max_length=400)
