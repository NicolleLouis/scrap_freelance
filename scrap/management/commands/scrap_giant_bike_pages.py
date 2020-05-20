import requests
from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand
from scrap.service.url import UrlService
from scrap.repository.bike import BikeRepository


class Command(BaseCommand):
    help = 'Scrap giant base page'

    def handle(self, *args, **options):
        unscrapped_bikes = BikeRepository.get_unscrapped_bikes()
        unscrapped_bike = unscrapped_bikes[0]
        print(unscrapped_bike.page_url)
        request = requests.get(unscrapped_bike.page_url)
        soup = BeautifulSoup(request.text, 'html.parser')
        tiles = soup.find_all("div", {"class": "tile"})
        print(len(tiles))
