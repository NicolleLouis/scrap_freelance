import requests
from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand
from scrap.repository.bike import BikeRepository


class Command(BaseCommand):
    help = 'Scrap giant base page'

    def handle(self, *args, **options):
        unscrapped_bikes = BikeRepository.get_unscrapped_bikes()
        for unscrapped_bike in unscrapped_bikes:
            unscrapped_bike.delete()
