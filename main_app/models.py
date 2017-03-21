from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Treasure(models.Model):
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=6,decimal_places=2)
    material = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    img_url = models.ImageField(upload_to='treasure_images',default='media/default.png')

    def __str__(self):
        return str(self.name)