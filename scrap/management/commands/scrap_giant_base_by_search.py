import requests
from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand
from scrap.service.url import UrlService
from scrap.service.giant_scrapper import GiantScrapperService

# # Giant settings
# base_url = "https://www.giant-bicycles.com"
# brand = "Giant"

# Liv settings
base_url = "https://www.liv-cycling.com"
brand = "Liv"

# # Giant research terms
# research_terms = [
#     "Anthem",
#     "Argento",
#     "Contend",
#     "Defy",
#     "Dirt",
#     "Escape",
#     "Explore",
#     "Fathom",
#     "Full",
#     "Glory",
#     "Quick",
#     "Prime",
#     "Propel",
#     "Revel",
#     "Revolt",
#     "Road",
#     "Roam",
#     "Stance",
#     "Talon",
#     "TCR",
#     "TCX",
#     "Trance",
#     "Trinity",
#     "XTC",
#     "Advanced",
# ]

# Liv research terms
research_terms = [
    "Avail",
    "Enchant",
    "Envie",
    "Lust",
    "Obsess",
    "Rove",
    "Tempt",
    "Intrigue",
    "Bliss",
    "Embolden",
    "Hail",
    "Thrive",
    "Rove",
    "Pique",
    "Amiti",
    "Vall",
    "Enviliv",
    "Langma",
    "Advanced",
]


class Command(BaseCommand):
    help = 'Scrap giant base page'

    def handle(self, *args, **options):
        for research_term in research_terms:
            self.scrap_one_search_term(research_term)

    @staticmethod
    def scrap_one_bike(bike, category):
        GiantScrapperService.scrap_one_bike_from_general_page(
            bike=bike,
            base_url=base_url,
            category=category,
            brand=brand
        )

    def scrap_one_search_term(self, research_term):
        url = UrlService.giant_concatenate_page_and_research_term(base_url, research_term)
        request = requests.get(url)
        soup = BeautifulSoup(request.text, 'html.parser')
        list_bike = soup.find_all("div", {"class": "tile"})
        print(research_term)
        print(len(list_bike))
        for bike in list_bike:
            self.scrap_one_bike(bike, "Unknown")
