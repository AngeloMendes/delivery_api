from datetime import datetime
from django.db import models
from .address import Address
from .seller import Seller
from .product import Product
from django.db import transaction, IntegrityError


class Order(models.Model):
    class Meta:
        app_label = 'app'
        db_table = 'order'

    created_at = models.DateTimeField(default=datetime.now, blank=False)
    collect_at = models.DateTimeField(blank=True)
    delivery_at = models.DateTimeField(blank=True)
    status = models.CharField(max_length=500)

    seller = models.ForeignKey(Seller, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    origin_address = models.ForeignKey(Address, on_delete=models.DO_NOTHING, related_name='origin')
    destination_address = models.ForeignKey(Address, on_delete=models.DO_NOTHING, related_name='destination')

    def __init__(self, collect_at, delivery_at, status, seller, product, origin_address, destination_address, *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.collect_at = collect_at
        self.delivery_at = delivery_at
        self.status = status
        self.seller = seller
        self.product = product
        self.origin_address = origin_address
        self.destination_address = destination_address

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
