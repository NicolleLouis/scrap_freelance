from scrap.models.bike import Bike


class BikeRepository:
    @staticmethod
    def get_or_create_by_name_and_brand_and_year(
            name,
            brand,
            year
    ):
        bike, _created = Bike.objects.get_or_create(
            name=name,
            brand=brand,
            year=year
        )
        return bike, _created

    @staticmethod
    def get_unscrapped_bikes():
        return list(Bike.objects.filter(is_scrapped=False))

    @staticmethod
    def get_bikes():
        return list(Bike.objects.all())
