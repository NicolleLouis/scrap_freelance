class UrlService:
    @staticmethod
    def concatenate_page_and_category(base_url, category):
        return "{}/fr/{}".format(base_url, category)

    @staticmethod
    def concatenate_page_and_research_term(base_url, research_term):
        return "{}/fr/search?keyword={}".format(base_url, research_term)
