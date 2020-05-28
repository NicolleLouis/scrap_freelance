import requests
from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand
from scrap.repository.bike import BikeRepository
from scrap.service.string_formatter import StringFormatterService

base_url = "https://www.giant-bicycles.com"
brand = "Giant"


class Command(BaseCommand):
    help = 'Scrap giant base page'

    def handle(self, *args, **options):
        unscrapped_bikes = BikeRepository.get_unscrapped_bikes()
        for unscrapped_bike in unscrapped_bikes:
            request = requests.get(unscrapped_bike.page_url)
            soup = BeautifulSoup(request.text, 'html.parser')
            print(unscrapped_bike.page_url)
            self.manage_simple_bike_page(soup, unscrapped_bike)

    def manage_simple_bike_page(self, soup, unscrapped_bike):
        table = soup.find("table")
        elements = table.find_all("tr")
        for element in elements:
            td = element.find_all("td")
            field = StringFormatterService.format_field(
                td[0].find("h4").text
            )
            value = td[1].text
            if not hasattr(
                    unscrapped_bike,
                    field
            ):
                print(field)
                raise SystemError
            setattr(
                unscrapped_bike,
                field,
                value
            )
        unscrapped_bike.is_scrapped = True
        unscrapped_bike.save()
