import scrapy
from urllib.parse import urljoin


class BricolageSpider(scrapy.Spider):
    name = 'mr_bricolage'
    start_urls = [
        'https://mr-bricolage.bg/bg/Instrumenti/Avto-i-veloaksesoari/Veloaksesoari/c/006008012?q=%3Arelevance&page=0&priceValue=',
        'https://mr-bricolage.bg/bg/Instrumenti/Avto-i-veloaksesoari/Veloaksesoari/c/006008012?q=%3Arelevance&page=1&priceValue=',
        'https://mr-bricolage.bg/bg/Instrumenti/Avto-i-veloaksesoari/Veloaksesoari/c/006008012?q=%3Arelevance&page=2&priceValue=',
    ]

    def parse(self, response):
        urls = response.css('div.product > div > a::attr(href)').extract()
        for url in urls:
            url = urljoin('https://mr-bricolage.bg', url)
            yield scrapy.Request(url=url, callback=self.parse_details)

    def parse_details(self, response):
        yield {
            'name': response.css('div.col-md-6 > h1::text').extract()[0],
            'price': response.css('p.price::text').re(r'\d+,\d+'),
            'image': response.css('div.owl-carousel > div > img::attr(src)').extract(),
            'characteristics': {
                (response.css('td::text').re(r'\w+')[0], response.css('td::text').re(r'\w+')[1]),
                (response.css('td::text').re(r'\w+')[2], response.css('td::text').re(r'\w+')[3]),
                (response.css('td::text').re(r'\w+')[4], response.css('td::text').re(r'\w+')[5]),
            },

        }