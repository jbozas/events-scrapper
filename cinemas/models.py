from django.db import models


class Cinema(models.Model):

    name = models.CharField(max_length=100)
    location = models.CharField(null=True, max_length=200)
    description = models.CharField(null=True, max_length=400)
    url = models.CharField(null=True, max_length=400)

    @property
    def html_name(self):
        return f"<a href='{self.url}'>{self.name}</a>"

    @property
    def information(self):
        return f"Location: <b>{self.location}</b>"
