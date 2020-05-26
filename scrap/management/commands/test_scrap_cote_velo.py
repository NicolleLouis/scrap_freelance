import requests
from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand
from scrap.service.url import UrlService


class Command(BaseCommand):
    help = 'Scrap giant base page'

    def handle(self, *args, **options):
        url = "https://cote-velo.fr/resultat-de-l-estimation"
        request = requests.get(url)
        soup = BeautifulSoup(request.text, 'html.parser')
        print(soup)
