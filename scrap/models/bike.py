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
    price = models.IntegerField(
        null=True,
        blank=True
    )
    tailles = models.TextField(
        null=True,
        blank=True
    )
    coloris = models.TextField(
        null=True,
        blank=True
    )
    cadre = models.TextField(
        null=True,
        blank=True
    )
    fourche = models.TextField(
        null=True,
        blank=True
    )
    amortisseur = models.TextField(
        null=True,
        blank=True
    )
    cintre = models.TextField(
        null=True,
        blank=True
    )
    potence = models.TextField(
        null=True,
        blank=True
    )
    tige_de_selle = models.TextField(
        null=True,
        blank=True
    )
    selle = models.TextField(
        null=True,
        blank=True
    )
    pedales = models.TextField(
        null=True,
        blank=True
    )
    manettes = models.TextField(
        null=True,
        blank=True
    )
    derailleur_avant = models.TextField(
        null=True,
        blank=True
    )
    derailleur_arriere = models.TextField(
        null=True,
        blank=True
    )
    freins = models.TextField(
        null=True,
        blank=True
    )
    leviers_de_frein = models.TextField(
        null=True,
        blank=True
    )
    cassette = models.TextField(
        null=True,
        blank=True
    )
    chaine = models.TextField(
        null=True,
        blank=True
    )
    pedalier = models.TextField(
        null=True,
        blank=True
    )
    boitier_de_pedalier = models.TextField(
        null=True,
        blank=True
    )
    jantes = models.TextField(
        null=True,
        blank=True
    )
    moyeux = models.TextField(
        null=True,
        blank=True
    )
    rayons = models.TextField(
        null=True,
        blank=True
    )
    pneus = models.TextField(
        null=True,
        blank=True
    )
    extras = models.TextField(
        null=True,
        blank=True
    )
    poids = models.TextField(
        null=True,
        blank=True
    )
    moteur = models.TextField(
        null=True,
        blank=True
    )
    capteurs = models.TextField(
        null=True,
        blank=True
    )
    console = models.TextField(
        null=True,
        blank=True
    )
    batterie = models.TextField(
        null=True,
        blank=True
    )
    eclairage = models.TextField(
        null=True,
        blank=True
    )
    anti_vol = models.TextField(
        null=True,
        blank=True
    )
    porte_bagages = models.TextField(
        null=True,
        blank=True
    )
    consolle = models.TextField(
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
        "price",
        "category",
        "is_scrapped",
    )
