from scrap.repository.bike import BikeRepository


class GiantScrapperService:
    @staticmethod
    def scrap_one_bike_from_general_page(
            bike,
            base_url,
            category="Unknown",
            brand="Unknown",
    ):
        if "bike-summary" in bike["class"]:
            caption = bike.find("div", {"class": "caption"})
            name = caption.find("h3").text
            year = int(caption.find("h4").text)
            bike_db, _created = BikeRepository.get_or_create_by_name_and_brand_and_year(
                name=name,
                brand=brand,
                year=year
            )
            bike_db.page_url = "{}{}".format(
                base_url,
                bike.find("article").find("picture").find("a")["href"]
            )
            bike_db.picture_url = bike.find("article"). \
                find("picture").find("a").find("img")["src"]
            bike_db.category = category
            bike_db.save()
