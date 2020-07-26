from datetime import datetime
from django.db import models
from .address import Address
from .order import Order
from .seller import Seller
from django.db import transaction, IntegrityError


class Route(models.Model):
    class Meta:
        app_label = 'app'
        db_table = 'route'

    created_at = models.DateTimeField(default=datetime.now, blank=False)
    collected_at = models.DateTimeField(blank=True)
    status = models.CharField(max_length=500)

    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    deliveryman = models.ForeignKey(Seller, on_delete=models.DO_NOTHING)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)

    def __init__(self, created_at, collect_at, status, order, deliveryman, address, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.created_at = created_at
        self.collect_at = collect_at
        self.status = status
        self.order = order
        self.deliveryman = deliveryman
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
