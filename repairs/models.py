from django.db import models


class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)

    description = models.TextField(blank=True)

    display_order = models.PositiveIntegerField(default=0)

    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order", "name"]
        verbose_name_plural = "Service Categories"

    def __str__(self):
        return self.name


class RepairService(models.Model):

    PRICE_TYPE_CHOICES = [
        ("fixed", "Fixed price"),
        ("starting", "Starting at"),
        ("hourly", "Hourly rate"),
        ("quote", "Contact for quote"),
        ("free", "Free"),
    ]

    category = models.ForeignKey(
        ServiceCategory,
        on_delete=models.PROTECT,
        related_name="services",
    )

    name = models.CharField(max_length=150)

    description = models.TextField(blank=True)

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True,
    )

    price_type = models.CharField(
        max_length=20,
        choices=PRICE_TYPE_CHOICES,
        default="fixed",
    )

    parts_included = models.BooleanField(default=False)

    display_order = models.PositiveIntegerField(default=0)

    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order", "name"]

    def __str__(self):
        return self.name

    @property
    def display_price(self):

        if self.price_type == "quote":
            return "Contact for quote"

        if self.price_type == "free":
            return "Free"

        if self.price is None:
            return "Contact for quote"

        if self.price_type == "starting":
            return f"From ${self.price:.2f}"

        if self.price_type == "hourly":
            return f"${self.price:.2f}/hr"

        return f"${self.price:.2f}"