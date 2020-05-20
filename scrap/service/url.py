class UrlService:
    @staticmethod
    def concatenate_page_and_category(base_url, category):
        return "{}/{}".format(base_url, category)
