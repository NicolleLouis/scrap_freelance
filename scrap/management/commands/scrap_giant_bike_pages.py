import requests
from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand
from scrap.repository.bike import BikeRepository
from scrap.service.string_formatter import StringFormatterService


class Command(BaseCommand):
    help = 'Scrap giant base page'

    def handle(self, *args, **options):
        unscrapped_bikes = BikeRepository.get_unscrapped_bikes()
        for unscrapped_bike in unscrapped_bikes:
            request = requests.get(unscrapped_bike.page_url)
            soup = BeautifulSoup(request.text, 'html.parser')
            self.remove_unwanted_div(soup)

            # Find if the product is alone or not
            if soup.find("div", {"id": "productsContainer"}) is not None:
                self.manage_multiple_bike_pages(soup, unscrapped_bike)
            else:
                self.manage_simple_bike_page(soup, unscrapped_bike)

    @staticmethod
    def manage_simple_bike_page(soup, unscrapped_bike):
        price = soup.find(
            "meta",
            {"property": "product:price:amount"}
        )["content"]
        if price is not None and price.isnumeric():
            unscrapped_bike.price = int(price)
        specification = soup.find("div", {"id": "specifications"})
        tables = specification.find_all("table") if specification is not None else []
        for table in tables:
            elements = table.find_all("tr")
            for element in elements:
                field = element.find("th").text
                value = element.find("td").text
                setattr(
                    unscrapped_bike,
                    StringFormatterService.format_field(field),
                    value
                )
        unscrapped_bike.is_scrapped = True
        unscrapped_bike.save()

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
            bike_db.picture_url = tile \
                .find("article") \
                .find("picture") \
                .find("a") \
                .find("img")["src"]
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
