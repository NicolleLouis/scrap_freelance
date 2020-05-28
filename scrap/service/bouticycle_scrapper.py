class BouticycleScrapperService:
    @staticmethod
    def contain_more_bike_link(soup):
        a = soup.find("a", {"id": "paginationVelo"})
        if a is not None:
            href = a["href"]
            return href.split("debut_velo=")[1]
        else:
            return False
