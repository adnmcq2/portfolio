from django.contrib import admin
from .models import ServiceCategory, RepairService


class RepairServiceInline(admin.TabularInline):
    model = RepairService

    fields = (
        "name",
        "price",
        "price_type",
        "parts_included",
        "display_order",
        "active",
    )

    extra = 1


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "display_order",
        "active",
    )

    list_editable = (
        "display_order",
        "active",
    )

    search_fields = ("name",)

    inlines = [RepairServiceInline]


@admin.register(RepairService)
class RepairServiceAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "category",
        "display_price",
        "price",
        "price_type",
        "parts_included",
        "display_order",
        "active",
    )

    list_filter = (
        "category",
        "price_type",
        "parts_included",
        "active",
    )

    list_editable = (
        "price",
        "price_type",
        "display_order",
        "active",
    )

    search_fields = (
        "name",
        "description",
    )