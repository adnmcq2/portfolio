from django.shortcuts import render, get_object_or_404
from .models import Bike
from decimal import Decimal, InvalidOperation

def bike_list(request):
    sort = request.GET.get("sort", "newest")
    manufacturer = request.GET.get("manufacturer", "")
    category = request.GET.get("category", "")
    condition = request.GET.get("condition", "")
    frame_size = request.GET.get("frame_size", "")

    min_price = request.GET.get("min_price", "")
    max_price = request.GET.get("max_price", "")

    sort_options = {
        "newest": "-created_at",
        "price_asc": "price",
        "price_desc": "-price",
        "year_asc": "year",
        "year_desc": "-year",
        "manufacturer": "manufacturer",
    }

    inventory = Bike.objects.filter(status="available")

    bikes = inventory.prefetch_related("photos")

    # Apply filters
    if manufacturer:
        bikes = bikes.filter(manufacturer=manufacturer)

    if category:
        bikes = bikes.filter(category=category)

    if condition:
        bikes = bikes.filter(condition=condition)

    if frame_size:
        bikes = bikes.filter(frame_size=frame_size)

    # Apply price filters
    for value, field in [
        (min_price, "price__gte"),
        (max_price, "price__lte"),
    ]:
        if value:
            try:
                price = Decimal(value)

                if price.is_finite() and 0 <= price <= Decimal("999999.99"):
                    bikes = bikes.filter(**{field: price})

            except InvalidOperation:
                pass

    # Apply sorting
    bikes = bikes.order_by(sort_options.get(sort, "-created_at"))

    # Generate dropdown options
    manufacturers = (
        inventory.order_by("manufacturer")
        .values_list("manufacturer", flat=True)
        .distinct()
    )

    frame_sizes = (
        inventory.exclude(frame_size="")
        .order_by("frame_size")
        .values_list("frame_size", flat=True)
        .distinct()
    )

    return render(request, "shop/bike_list.html", {

        "min_price": min_price,
        "max_price": max_price,


        "bikes": bikes,
        "sort": sort,
        "manufacturer": manufacturer,
        "category": category,
        "condition": condition,
        "frame_size": frame_size,

        "manufacturers": manufacturers,
        "frame_sizes": frame_sizes,
        "categories": Bike.CATEGORY_CHOICES,
        "conditions": Bike.CONDITION_CHOICES,
    })

def bike_detail(request, pk):
    bike = get_object_or_404(Bike, pk=pk)

    return render(request, "shop/bike_detail.html", {
        "bike": bike
    })