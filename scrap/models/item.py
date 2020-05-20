from django.db import models
from import_export.admin import ImportExportModelAdmin


class Item(models.Model):
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
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return "{}, finished = {}".format(self.name, self.is_finished)


class ItemAdmin(ImportExportModelAdmin):
    list_display = (
        "is_scrapped",
        "page_url",
        "picture_url",
        "brand",
        "name",
        "year",
        "category",
        "is_finished",
    )
