from django.db import models
from django.conf import settings

# Scrape data coming from websites
# The posts will contain images, urls and titles
# model - headline(title, image, url)


class Headline(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(null=True, blank=True)
    url = models.TextField()

    def __str__(self):
        return self.title