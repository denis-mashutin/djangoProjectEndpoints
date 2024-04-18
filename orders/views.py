from django.shortcuts import render

from django.views.generic import ListView, DetailView
from orders.models import *


# Create your views here.
class OrderList(ListView):
    model = DeliveryOrder


class OrderDetail(DetailView):
    model = DeliveryOrder


def add_new(request):
    pass