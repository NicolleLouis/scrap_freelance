from scrap.models.bike import Bike


class BikeRepository:
    @staticmethod
    def get_or_create_by_name_and_brand_and_year(
            name,
            brand,
            year
    ):
        podcast, _created = Bike.objects.get_or_create(
            name=name,
            brand=brand,
            year=year
        )
        return podcast, _created
