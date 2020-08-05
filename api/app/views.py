from django.shortcuts import render
from rest_framework import generics
from .models.product import Product
from .models.seller import Seller
from .models.route import Route
from .models.order import Order
from .models.stock import Stock
from .serializers import ProductSerializer, SellerSerializer, RouteSerializer, OrderSerializer, StockSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SellerListView(generics.ListCreateAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer


class SellerView(generics.ListCreateAPIView):
    queryset = Seller.find_by_id(_id)
    serializer_class = SellerSerializer


class RouteListView(generics.ListCreateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class RouteView(generics.ListCreateAPIView):
    queryset = Route.find_by_id(_id)
    serializer_class = RouteSerializer


class OrderListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderView(generics.ListCreateAPIView):
    queryset = Order.find_by_id(_id)
    serializer_class = OrderSerializer


class StockListView(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
