from django.db import models
from import_export.admin import ImportExportModelAdmin


class Bike(models.Model):
    id = models.AutoField(primary_key=True)
    is_scrapped = models.BooleanField(default=False)
    page_url = models.TextField(
        null=True,
        blank=True
    )
    picture_url = models.TextField(
        null=True,
        blank=True
    )
    brand = models.TextField(
        null=True,
        blank=True
    )
    name = models.TextField(
        null=True,
        blank=True
    )
    year = models.IntegerField(
        null=True,
        blank=True
    )
    category = models.TextField(
        null=True,
        blank=True
    )

    def __str__(self):
        return "{}, finished = {}".format(self.name, self.is_scrapped)


class BikeAdmin(ImportExportModelAdmin):
    list_display = (
        "name",
        "brand",
        "year",
        "category",
    )
