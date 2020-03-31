class UrlService:
    @staticmethod
    def concatenate_page_and_number(base_url, page_number):
        return "{}&page={}#page".format(base_url, page_number)

    @staticmethod
    def concatenate_page_and_letter(base_url, letter):
        return "{}?letter={}".format(base_url, letter)
