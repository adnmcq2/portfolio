from django.shortcuts import render
from .models import Bike


def bike_list(request):
    bikes = Bike.objects.filter(status="available")

    return render(request, "shop/bike_list.html", {
        "bikes": bikes
    })