from django.db import models
from django.db import transaction, IntegrityError
import geopy.distance

class Address(models.Model):
    class Meta:
        app_label = 'app'
        db_table = 'address'

    street = models.CharField(max_length=500)
    postal_code = models.CharField(max_length=20)
    number = models.CharField(max_length=10)
    state = models.CharField(max_length=500)
    neighborhood = models.CharField(max_length=500)
    reference = models.CharField(max_length=500)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __init__(self, street, postal_code, number, state, neighborhood, reference, latitude, longitude, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.street = street
        self.postal_code = postal_code
        self.number = number
        self.state = state
        self.neighborhood = neighborhood
        self.reference = reference
        self.latitude = latitude
        self.longitude = longitude

    def save(self, *args, **kwargs):
        try:
            super().save()
            return True
        except IntegrityError:
            transaction.set_rollback(True)
            return False

    @classmethod
    def find_by_id(cls, _id: int):
        return cls.objects.get(pk=_id)

    @classmethod
    def find_all(cls, filters: dict):
        return cls.objects.all().filter(**filters)

    @staticmethod
    def calc_distance(origin: tuple, destination: tuple):
        """
        :param origin: a tuple with origin coordinates. Ex. (12.3456, 12.789)
        :param destination: a tuple with destination coordinates. Ex. (12.3456, 12.789)
        :return: distance between two coordinates in km
        """
        return geopy.distance.vicenty(origin, destination).km
