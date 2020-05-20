from scrap.models.item import Item


class ItemRepository:
    @staticmethod
    def get_or_create_by_name(name):
        podcast, _created = Item.objects.get_or_create(
            name=name,
        )
        return podcast, _created

    @staticmethod
    def update_url(name, url):
        podcast, _created = ItemRepository.get_or_create_by_name(name)
        podcast.url = url
        podcast.save()
        return _created
