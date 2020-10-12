from __future__ import unicode_literals

from django.db import models

# Create your models here.


class MovieDetails(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "MovieDetails"
        verbose_name_plural = "MovieDetails"
