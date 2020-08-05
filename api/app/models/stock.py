from django.db import models
from .address import Address
from .seller import Seller
from .product import Product
from django.db import transaction, IntegrityError
from typing import Optional
from datetime import datetime


class Stock(models.Model):
    class Meta:
        app_label = 'app'
        db_table = 'stock'

    total = models.IntegerField()

    seller = models.ForeignKey(Seller, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    collect_at_start = models.DateTimeField(blank=True)
    collect_at_end = models.DateTimeField(blank=True)

    def __init__(self, seller, product, total, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.seller = seller
        self.product = product
        self.total = total

    def save(self, *args, **kwargs):
        try:
            super().save()
            return True
        except IntegrityError:
            transaction.set_rollback(True)
            return False

    @classmethod
    def update_stock(cls, filters: dict, total: int, collect_at_start: Optional[datetime] = None,
                     collect_at_end: Optional[datetime] = None):
        stock = cls.objects.first().filter(**filters)
        stock.total = total
        if collect_at_start:
            stock.collect_at_start = collect_at_start
        if collect_at_end:
            stock.collect_at_end = collect_at_end
        stock.save()

    @classmethod
    def find_by_products(cls, product_id: int, origin: tuple):
        stocks = cls.objects.all().filter(cls.product.id == product_id)
        sellers = []
        for stock in stocks:
            sellers.append({
                "seller": stock["seller"],
                "price": stock["product"]["price"],
                "distance": Address.calc_distance((stock["seller"].address.latitude, stock["seller"].address.longitude),
                                                  origin)
            })
        return sorted(sellers, key=lambda k: k['distance'])
