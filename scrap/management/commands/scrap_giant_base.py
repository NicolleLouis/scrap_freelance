import requests
from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand
from scrap.service.url import UrlService
from scrap.repository.bike import BikeRepository

base_url = "https://www.giant-bicycles.com/fr"
brand = "Giant"
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

    def scrap_one_bike(self, bike, category):
        caption = bike.find("div", {"class": "caption"})
        name = caption.find("h3").text
        year = int(caption.find("h4").text)
        bike_db, _created = BikeRepository.get_or_create_by_name_and_brand_and_year(
            name=name,
            brand=brand,
            year=year
        )
        bike_db.page_url = "https://www.giant-bicycles.com{}" \
            .format(bike.find("article").find("picture").find("a")["href"])
        bike_db.picture_url = bike.find("article"). \
            find("picture").find("a").find("img")["src"]
        bike_db.category = category
        bike_db.save()

    def scrap_one_category(self, category):
        url = UrlService.concatenate_page_and_category(base_url, category)
        request = requests.get(url)
        soup = BeautifulSoup(request.text, 'html.parser')
        list_bike = soup.find_all("div", {"class": "tile"})
        print(category)
        print(len(list_bike))
        for bike in list_bike:
            self.scrap_one_bike(bike, category)
