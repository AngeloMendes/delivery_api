from django.db import models


class Product(models.Model):
    class Meta:
        db_table = 'product'

    name = models.CharField(max_length=500)
    volume = models.TextField()
    image = models.TextField()
    risk = models.TextField()
    price = models.FloatField()

    def __init__(self, name, volume, image, risk, price, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.volume = volume
        self.image = image
        self.risk = risk
        self.price = price

    def __str__(self):
        return self.name

    @classmethod
    def find_by_id(cls, _id: int):
        return cls.objects.get(pk=_id)

    @classmethod
    def find_all(cls, filters: dict):
        return cls.objects.all().filter(**filters)
