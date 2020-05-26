import requests
from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand
from scrap.repository.bike import BikeRepository


class Command(BaseCommand):
    help = 'Scrap giant base page'

    def handle(self, *args, **options):
        number_unscrapped_bikes = len(BikeRepository.get_unscrapped_bikes())
        number_bikes = len(BikeRepository.get_bikes())

        print("Total number bikes: {}".format(number_bikes))
        print("Total number unscrapped bikes: {}".format(number_unscrapped_bikes))
