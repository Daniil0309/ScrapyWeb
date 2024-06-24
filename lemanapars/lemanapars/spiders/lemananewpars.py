import scrapy


class LemananewparsSpider(scrapy.Spider):
    name = "lemananewpars"
    allowed_domains = ["https://novorossiysk.lemanapro.ru"]
    start_urls = ["https://novorossiysk.lemanapro.ru/catalogue/osveshchenie"]

    def parse(self, response):
        lighting = response.css('div.p155f0re_plp largeCard')
        for divan in divans:
            yield {'name': divan.css('div.cef202m_plp span::text').get(),
                   'price': divan.css('div.pY3d2 span::text').get(),
                   'url': divan.css('a').attrib['href']
                   }
