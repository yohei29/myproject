from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from myproject.items import Headline

class NewsCrawlSpider(CrawlSpider):
    name = 'news_crawl'
    allowed_domains = ["news.yahoo.co.jp"]

    start_urls = (
        'http://news.yahoo.co.jp/',
    )

    rules = (
        Rule(LinkExtractor(allow=r'/pickup/\d+$'), callback='parse_topics'),
    )

    # 以下は、例のため、正常に動作しない
    # 複数のページをクローリングする場合
    # rules = (
    #     Rule(LinkExtractor(allow=r'/book/\d+$'), callback='parse_book'),
    #     Rule(LinkExtractor(allow=r'/news/\d+$'), callback='parse_news'),
    # )

    # クローリング開始ページから、遷移した先のページをクローリング
    # rules = (
    #     Rule(LinkExtractor(allow=r'/category/\w+$')),
    #     Rule(LinkExtractor(allow=r'/product/\w+$'), callback='parse_news'),
    # )

    # クローリング開始ページ、遷移した先のページの、両方をクローリング
    # rules = (
    #     Rule(LinkExtractor(allow=r'/category/\w+$'), callback='parse_news', follow=True),
    #     Rule(LinkExtractor(allow=r'/product/\w+$'), callback='parse_news'),
    # )

    def parse_topicks(self, response):
        item = Headline()
        item['title'] = response.css('.newsTitle ::text').extract_first()
        item['body'] = response.css('.hbody').xpath('string()').extract_first()

        yield item