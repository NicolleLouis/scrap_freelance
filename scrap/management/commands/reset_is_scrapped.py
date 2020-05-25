import requests
from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand
from scrap.repository.bike import BikeRepository


class Command(BaseCommand):
    help = 'Scrap giant base page'

    def handle(self, *args, **options):
        bikes = BikeRepository.get_bikes()
        for bike in bikes:
            bike.is_scrapped = False
            bike.save()
