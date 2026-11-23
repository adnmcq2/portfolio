from django.db import models


class Bike(models.Model):

    CATEGORY_CHOICES = [
        ("road", "Road"),
        ("mountain", "Mountain"),
        ("hybrid", "Hybrid"),
        ("cruiser", "Cruiser"),
        ("other", "Other"),
    ]

    CONDITION_CHOICES = [
        ("excellent", "Excellent"),
        ("good", "Good"),
        ("fair", "Fair"),
        ("project", "Project Bike"),
    ]

    STATUS_CHOICES = [
        ("available", "Available"),
        ("reserved", "Reserved"),
        ("sold", "Sold"),
    ]

    manufacturer = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    year = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )

    frame_size = models.CharField(
        max_length=50,
        blank=True
    )

    condition = models.CharField(
        max_length=20,
        choices=CONDITION_CHOICES
    )

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    description = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="available"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.year or ''} {self.manufacturer} {self.model}".strip()


class BikePhoto(models.Model):

    bike = models.ForeignKey(
        Bike,
        on_delete=models.CASCADE,
        related_name="photos"
    )

    image = models.ImageField(
        upload_to="bikes/"
    )

    caption = models.CharField(
        max_length=200,
        blank=True
    )

    def __str__(self):
        return f"Photo of {self.bike}"
