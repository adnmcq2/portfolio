from django.shortcuts import render
from django.db.models import Prefetch

from .models import ServiceCategory, RepairService
from shop.models import Product


def repair_list(request):

    services = RepairService.objects.filter(active=True)

    categories = ServiceCategory.objects.filter(
        active=True,
        services__active=True,
    ).distinct().prefetch_related(
        Prefetch("services", queryset=services)
    )

    products = Product.objects.filter(
        active=True
    ).prefetch_related("photos")

    selected_category = request.GET.get("category", "")

    if selected_category in dict(Product.CATEGORY_CHOICES):
        products = products.filter(category=selected_category)
    else:
        selected_category = ""

    context = {
        "categories": categories,
        "products": products,
        "product_categories": Product.CATEGORY_CHOICES,
        "selected_category": selected_category,
    }

    return render(request, "repairs/repair_list.html", context)