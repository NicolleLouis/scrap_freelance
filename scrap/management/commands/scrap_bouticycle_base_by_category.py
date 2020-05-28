import requests
from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand
from scrap.service.url import UrlService
from scrap.service.bouticycle_scrapper import BouticycleScrapperService
from scrap.service.string_formatter import StringFormatterService
from scrap.repository.bike import BikeRepository

# Constants
base_url = "https://bouticycle.com"
categories = [
    "-VTT-",
    "-Route-",
    "-Loisirs-",
    "-Enfants-",
    "-Pliant-",
    "-Electrique-",
    "-Tandem-",
    "-BMX-",
    "-Triathlon-70-",
]
years = list(range(2009, 2021))


class Command(BaseCommand):
    help = 'Scrap bouticycle base page'

    def handle(self, *args, **options):
        for category in categories:
            for year in years:
                print("category: {}".format(category))
                print("year: {}".format(year))
                self.change_page_within_year(
                    category,
                    year
                )

    @staticmethod
    def scrap_one_bike(bike_soup, category, year):
        name = bike_soup.find("h2", {"class": "fichevelo-titre"}).text
        brand = bike_soup.find("p", {"class": "fichevelo-subtitle"}) \
            .find("strong").text
        bike, _created = BikeRepository.get_or_create_by_name_and_brand_and_year(
            name=name,
            brand=brand,
            year=year
        )
        bike.page_url = UrlService.bouticycle_concatenate_bike_page(
            base_url=base_url,
            bike_url=bike_soup.find("a")["href"]
        )
        bike.picture_url = UrlService.bouticycle_format_picture_url(
            bike_soup.find("noscript").find("img")["src"]
        )
        bike.price = StringFormatterService.format_price(
            bike_soup.find("p", {"class": "fichevelo-price"}).text
        )
        bike.category = category
        bike.save()

    def scrap_one_page(self, soup, category, year):
        bikes = soup.find_all("li", {"class": "fichevelo-item"})
        for bike_soup in bikes:
            self.scrap_one_bike(bike_soup, category, year)

    def change_page_within_year(self, category, year):
        pagination = 0
        while pagination is not False:
            url = UrlService.bouticycle_concatenate_page_and_category_and_year_and_pagination(
                base_url=base_url,
                category=category,
                year=year,
                pagination=pagination
            )
            print(url)
            request = requests.get(url)
            soup = BeautifulSoup(request.text, 'html.parser')
            self.scrap_one_page(soup, category, year)

            # Change page
            pagination = BouticycleScrapperService.contain_more_bike_link(soup)
