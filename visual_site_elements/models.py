from django.db import models
from sorl.thumbnail import ImageField


class BrandImage(models.Model):
    title = models.CharField(max_length=200)
    image = ImageField(upload_to='images/brand_images')

    def __str__(self):
        return str(self.title)


class SliderImageThumb(models.Model):
    title = models.CharField(max_length=200)
    image = ImageField(upload_to='images/slider_images/random_thumbs')

    def __str__(self):
        return str(self.title)


class SliderImage(models.Model):
    title = models.CharField(max_length=200)
    image = ImageField(upload_to='images/slider_images')

    def __str__(self):
        return str(self.title)

