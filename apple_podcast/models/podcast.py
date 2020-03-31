from django.db import models
from import_export.admin import ImportExportModelAdmin


class Podcast(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.TextField(
        null=True,
        blank=True
    )
    name = models.TextField(
        null=True,
        blank=True
    )
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return "{}, finished = {}".format(self.name, self.is_finished)


class PodcastAdmin(ImportExportModelAdmin):
    list_display = (
        "name",
        "url",
        "is_finished"
    )
