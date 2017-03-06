from django.db import models
from django_images.models import Image


class Brand(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return str(self.title)


class BrandImage(Image):
    brand = models.ForeignKey(Brand, related_name='images')
