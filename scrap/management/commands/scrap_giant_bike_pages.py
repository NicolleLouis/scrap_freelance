import requests
from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand
from scrap.service.url import UrlService
from scrap.repository.bike import BikeRepository


class Command(BaseCommand):
    help = 'Scrap giant base page'

    def handle(self, *args, **options):
        ready_to_scrap_bikes = 0
        unscrapped_bikes = BikeRepository.get_unscrapped_bikes()
        for unscrapped_bike in unscrapped_bikes:
            request = requests.get(unscrapped_bike.page_url)
            soup = BeautifulSoup(request.text, 'html.parser')
            self.remove_unwanted_div(soup)

            # Find if the product is alone or not
            if soup.find("div", {"id": "productsContainer"}) is not None:
                self.manage_multiple_bike_pages(soup, unscrapped_bike)
            else:
                ready_to_scrap_bikes += 1

        print("total number of bikes ready to be scrapped: {}".format(ready_to_scrap_bikes))

    @staticmethod
    def manage_multiple_bike_pages(soup, unscrapped_bike):
        brand = unscrapped_bike.brand
        year = unscrapped_bike.year
        category = unscrapped_bike.category
        tiles = soup.find_all("div", {"class": "tile"})
        unscrapped_bike.delete()
        for tile in tiles:
            name = tile.find("h3").text
            bike_db, _created = BikeRepository.get_or_create_by_name_and_brand_and_year(
                name=name,
                brand=brand,
                year=year
            )
            bike_db.page_url = "https://www.giant-bicycles.com{}" \
                .format(tile.find("article").find("picture").find("a")["href"])
            bike_db.category = category
            bike_db.save()

    @staticmethod
    def remove_unwanted_div(soup):
        # Delete similar products div element
        similar_product_div = soup.find("div", {"id": "similarproducts"})
        if similar_product_div is not None:
            similar_product_div.decompose()

        # Delete youmayalsolike div element
        youmayalsolike_product_div = soup.find("div", {"id": "youmayalsolike"})
        if youmayalsolike_product_div is not None:
            youmayalsolike_product_div.decompose()