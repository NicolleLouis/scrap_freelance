from apple_podcast.models.podcast import Podcast


class PodcastRepository:
    @staticmethod
    def get_or_create_by_name(name):
        podcast, _created = Podcast.objects.get_or_create(
            name=name,
        )
        return podcast, _created

    @staticmethod
    def update_url(name, url):
        podcast, _created = PodcastRepository.get_or_create_by_name(name)
        podcast.url = url
        podcast.save()
        return _created
