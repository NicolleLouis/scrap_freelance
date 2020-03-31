import requests
import string
from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand
from apple_podcast.service.scrapper import ScrapperService
from apple_podcast.service.url import UrlService
from apple_podcast.repository.podcast import PodcastRepository

base_url = "https://podcasts.apple.com/fr/genre/podcasts-arts-livres/id1482"


class Command(BaseCommand):
    help = 'Scrap https://podcasts.apple.com/fr/genre/podcasts-arts-livres/id1482'

    def handle(self, *args, **options):
        total_created = 0
        letters = string.ascii_uppercase
        letters += "*"
        for letter in letters:
            print(letter)
            total_created = self.scrap_one_letter(total_created, base_url, letter)

        print("fini c'est la fete")
        print("Number of new podcast: {}".format(total_created))

    def scrap_one_letter(self, total_created, base_url, letter):
        base_url = UrlService.concatenate_page_and_letter(base_url, letter)
        request_url = UrlService.concatenate_page_and_number(base_url, 1)
        request = requests.get(request_url)
        soup = BeautifulSoup(request.text, 'html.parser')
        number_of_page = ScrapperService.get_number_of_pages(soup)
        for page_number in range(number_of_page):
            print(page_number)
            total_created = self.scrap_one_page(page_number, total_created)
        return total_created

    def scrap_one_page(self, page_number, total_created):
        url = UrlService.concatenate_page_and_number(base_url, page_number + 1)
        request = requests.get(url)
        soup = BeautifulSoup(request.text, 'html.parser')
        list_podcasts = ScrapperService.get_list_podcasts(soup)
        for podcast in list_podcasts:
            url, name = ScrapperService.get_url_and_name_from_li(podcast)
            _created = PodcastRepository.update_url(name, url)
            if _created:
                total_created += 1
        return total_created