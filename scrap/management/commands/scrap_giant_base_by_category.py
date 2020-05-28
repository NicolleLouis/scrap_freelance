import requests
from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand
from scrap.service.url import UrlService
from scrap.service.giant_scrapper import GiantScrapperService

# Giant settings
# base_url = "https://www.giant-bicycles.com"
# brand = "Giant"

# Liv settings
base_url = "https://www.liv-cycling.com"
brand = "Liv"

# Same list for liv and giant
categories = [
    "route",
    "ville",
    "chemin",
    "tout-terrain",
    "hybrid",
    "enfants"
]


class Command(BaseCommand):
    help = 'Scrap giant base page'

    def handle(self, *args, **options):
        for category in categories:
            self.scrap_one_category(category)

    @staticmethod
    def scrap_one_bike(bike, category):
        GiantScrapperService.scrap_one_bike_from_general_page(
            bike=bike,
            base_url=base_url,
            category=category,
            brand=brand
        )

    def scrap_one_category(self, category):
        url = UrlService.giant_concatenate_page_and_category(base_url, category)
        request = requests.get(url)
        soup = BeautifulSoup(request.text, 'html.parser')
        list_bike = soup.find_all("div", {"class": "tile"})
        print(research)
        print(len(list_bike))
        for bike in list_bike:
            self.scrap_one_bike(bike, category)
