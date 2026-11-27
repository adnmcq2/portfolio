from django.contrib import admin
from django.utils.html import format_html

from .models import MediaImage, SiteSettings


@admin.register(MediaImage)
class MediaImageAdmin(admin.ModelAdmin):

    list_display = (
        "thumbnail",
        "title",
        "credit",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "title",
        "alt_text",
        "caption",
        "credit",
    )

    list_filter = ("created_at",)

    readonly_fields = (
        "image_preview",
        "created_at",
        "updated_at",
    )

    fields = (
        "title",
        "image",
        "image_preview",
        "alt_text",
        "caption",
        "credit",
        "created_at",
        "updated_at",
    )

    @admin.display(description="Thumbnail")
    def thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width:100px; '
                'height:75px; object-fit:contain;">',
                obj.image.url
            )
        return "No image"

    @admin.display(description="Image preview")
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-width:500px; '
                'max-height:400px; object-fit:contain;">',
                obj.image.url
            )
        return "No image uploaded"


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):

    fields = (
        "site_title",
        "tagline",
        "header_image",
        "contact_email",
    )

    autocomplete_fields = ("header_image",)

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False