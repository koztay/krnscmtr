from django.db import models


class Brand(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return str(self.title)


class BrandImage(models.Model):
    brand = models.ForeignKey(Brand, related_name='images')
