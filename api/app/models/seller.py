from django.db import models
from .address import Address
from django.db import transaction, IntegrityError


class Seller(models.Model):
    class Meta:
        app_label = 'app'
        db_table = 'seller'

    name = models.CharField(max_length=500)
    document = models.CharField(max_length=500)
    score = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __init__(self, name, document, score, address, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.document = document
        self.score = score
        self.address = address

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