from shop.models import Bike

from django.shortcuts import render


def home(request):
    featured_bikes = (
        Bike.objects
        .filter(featured=True, status="available")
        .prefetch_related("photos")
        .order_by("-created_at")[:3]
    )

    return render(request, "pages/home.html", {
        "featured_bikes": featured_bikes,
    })
