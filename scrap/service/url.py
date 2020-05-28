class UrlService:
    @staticmethod
    def giant_concatenate_page_and_category(base_url, category):
        return "{}/fr/{}".format(base_url, category)

    @staticmethod
    def giant_concatenate_page_and_research_term(base_url, research_term):
        return "{}/fr/search?keyword={}".format(base_url, research_term)

    @staticmethod
    def bouticycle_concatenate_page_and_category_and_year_and_pagination(
            base_url,
            category,
            year,
            pagination,
    ):
        return "{}/{}?annee_velo={}&debut_velo={}".format(
            base_url,
            category,
            year,
            pagination,
        )

    @staticmethod
    def bouticycle_concatenate_bike_page(
            base_url,
            bike_url
    ):
        return "{}/{}".format(base_url, bike_url)

    @staticmethod
    def bouticycle_format_picture_url(picture_url):
        return "https:{}".format(picture_url)
