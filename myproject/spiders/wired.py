from scrapy.spider import SitemapSpider

class WiredjpSpider(SitemapSpider):
    name = 'wiredjp'
    allowed_domain = ['wired.jp']

    sitemap_urls = [
        'https://wired.jp/sitemap.xml',
    ]

    sitemap_follow = [
        r'post-2018-',
    ]

    sitemap_rules = [
        (r'/2018/\d\d/\d\d/', 'parse_post')
    ]

    def parse_post(self, response):
        yield {
            'title':response.css('h1.post-title::text').extract_first(),
        }