from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import  LinkExtractor

from myproject.items import Restaurant

class TabelogSpoider(CrawlSpider):
    name = 'tabelog'
    allowed_domains = [
        "tabelog.com"
    ]
    start_urls = [
        'https://tabelog.com/tokyo/rstLst/lunch/?LstCosT=2&RdoCosTp=1'
    ]
    rules = [
        Rule(LinkExtractor(allow=r'/\w+/rstLst/lunch/\d/')),
        Rule(LinkExtractor(allow=r'/\w+/A\d+/A\d+/\d+/$'), callback='parse_restaurant'),
    ]

    def parse_restaurant(self, response):
        latitude, longitude = response.css('img.js-map-lazyload::attr("data-original")').re(r'markers=.*?%7C([\d.]+),([\d.]+)')

        item = Restaurant(
            name=response.css('.display-name').xpath('string()').extract_first().strip(),
            address=response.css('[class="rstinfo-table__address"]').xpath('string()').extract_first(),
            latitude = latitude,
            longitude = longitude,
            station = response.css('[class="linktree__parent-target-text"]').xpath('string()').extract_first(),
            score = response.css('[class="rdheader-rating__score-val-dtl"]').xpath('string()').extract_first(),
        )

        return item