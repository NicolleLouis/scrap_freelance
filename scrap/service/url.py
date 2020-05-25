class UrlService:
    @staticmethod
    def concatenate_page_and_category(base_url, category):
        return "{}/fr/{}".format(base_url, category)
