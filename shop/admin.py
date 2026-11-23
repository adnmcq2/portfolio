from django.contrib import admin
from .models import Bike, BikePhoto


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