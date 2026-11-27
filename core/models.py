from django.db import models


class MediaImage(models.Model):

    title = models.CharField(max_length=200)

    image = models.ImageField(upload_to="library/")

    alt_text = models.CharField(
        max_length=250,
        blank=True
    )

    caption = models.TextField(blank=True)

    credit = models.CharField(
        max_length=200,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Media Image"
        verbose_name_plural = "Media Library"

    def __str__(self):
        return self.title



class SiteSettings(models.Model):

    site_title = models.CharField(
        max_length=100,
        default="Wednesday Cycles"
    )

    tagline = models.CharField(
        max_length=200,
        default="Used bikes • Repairs • Washington, DC"
    )

    header_image = models.ForeignKey(
        MediaImage,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="site_headers"
    )

    contact_email = models.EmailField(blank=True)

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return self.site_title