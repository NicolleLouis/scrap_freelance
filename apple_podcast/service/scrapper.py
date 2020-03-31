class ScrapperService:
    @staticmethod
    def get_number_of_pages(soup):
        selectedgenre = soup.find("div", {"id": "selectedgenre"})
        listpaginate = selectedgenre.find("ul", {"class": "list paginate"})
        return (len(listpaginate) - 1) if listpaginate else 1

    @staticmethod
    def get_list_podcasts(soup):
        selectedcontent = soup.find("div", {"id": "selectedcontent"})
        return selectedcontent.find_all('li')

    @staticmethod
    def get_url_and_name_from_li(li):
        a = li.find("a")
        url = a["href"]
        name = a.get_text()
        return url, name
