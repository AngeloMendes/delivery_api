from django.db import models


# Create your models here.

class Product(models.Model):
    class Meta:
        db_table = 'product'

    name = models.CharField(max_length=500)
    volume = models.FloatField()
    image = models.TextField()

    def __init__(self, name, volume, image, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.volume = volume
        self.image = image

    def __str__(self):
        return self.name
