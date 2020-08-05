from datetime import datetime
from django.db import models
from .address import Address
from .order import Order
from .seller import Seller
from django.db import transaction, IntegrityError
import requests
import os


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

    def calc_smart_route(self, origin: tuple, orders: list):
        """
        :param origin: CDD location
        :param orders: list of orders
        :return: list of orders sorted by distance, considering to get and delivery of products
        """
        delivery_time = 12  # minutes
        limit_time = 480  # similar to 8 hours
        distances = []

        for order in orders:
            if (order.origin_address.latitude, order.origin_address.longitude) != origin:
                collect_point = Address.calc_distance(origin,
                                                      (order.origin_address.latitude, order.origin_address.longitude))
                delivery_point = Address.calc_distance((order.origin_address.latitude, order.origin_address.longitude),
                                                       (order.destination_address.latitude,
                                                        order.destination_address.longitude))
                distances.append((order, collect_point))
                distances.append((order, collect_point + (delivery_point - collect_point)))
            else:
                distances.append((order, Address.calc_distance(origin, (
                    order.destination_address.latitude, order.destination_address.longitude))))
            order.status = "Em Rota"
            order.save()

            if delivery_time >= limit_time:
                break
            delivery_time += delivery_time
        return distances.sort(key=lambda x: x[1])

    def get_route_from_maps(self, orders_sorted: list):
        smart_route = []
        for order in orders_sorted:
            maps_instructions = requests.get(
                f"https://maps.googleapis.com/maps/api/directions/json?"
                f"waypoints=via:{order[0].origin_address.latitude}%2C{order[0].origin_address.longitude}"
                f"%7Cvia:{order[0].destination_address.latitude}%2C{order[0].destination_address.longitude}"
                f"&key={os.getenv('GOOGLE_API_KEY')}")
            smart_route.append({"order": order[0], "distance": order[1], "instructions": maps_instructions})
        return smart_route
