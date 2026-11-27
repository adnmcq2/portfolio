from django.contrib import admin
from .models import Bike, BikePhoto, Product, ProductPhoto


class BikePhotoInline(admin.TabularInline):
    model = BikePhoto
    extra = 1


@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    list_display = (
        "manufacturer",
        "model",
        "year",
        "category",
        "price",
        "status",
        "featured",
    )

    list_filter = (
        "category",
        "condition",
        "status",
        "featured",
    )

    list_editable = ("featured",)

    search_fields = (
        "manufacturer",
        "model",
        "description",
    )

    inlines = [BikePhotoInline]

class ProductPhotoInline(admin.TabularInline):

    model = ProductPhoto
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "manufacturer",
        "category",
        "condition",
        "price",
        "quantity",
        "stock_status",
        "featured",
        "active",
        "display_order",
    )

    list_editable = (
        "price",
        "quantity",
        "featured",
        "active",
        "display_order",
    )

    list_filter = (
        "category",
        "condition",
        "featured",
        "active",
    )

    search_fields = (
        "name",
        "manufacturer",
        "model",
        "description",
    )

    inlines = [ProductPhotoInline]