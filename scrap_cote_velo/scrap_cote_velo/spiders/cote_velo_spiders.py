import scrapy


class CoteVeloSpider(scrapy.Spider):
    name = "cote_velo"
    start_urls = ['https://cote-velo.fr/estimer-mon-velo']

    def parse(self, response):
        filename = "cote_velo"
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
