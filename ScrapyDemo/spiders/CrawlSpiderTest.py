# -*- coding: utf-8 -*-
import scrapy
from scrapy import cmdline
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ScrapyDemo.items import CrawlSpiderTestItem


class CrawlspidertestSpider(CrawlSpider):
    name = 'CrawlSpiderTest'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/tag/编程?start=0&type=T']

    custom_settings = {
        'ITEM_PIPELINES':{'ScrapyDemo.pipelines.CrawlSpiderTestPipeline':100},
        # 'COOKIES_ENABLED':True
        'DOWNLOAD_DELAY ':3,
        'CONCURRENT_REQUESTS':3,
        'CONCURRENT_REQUESTS_PER_DOMAIN':3,
        'DOWNLOADER_MIDDLEWARES':{'ScrapyDemo.middlewares.ProxyMiddleWare':125}
        }


    rules = (
        # 分页     \?正则匹配匹配中转义
        Rule(LinkExtractor(allow=r'https://book.douban.com/tag/编程\?start=\d+&type=T')),
        # 分页中详细信息页
        Rule( LinkExtractor( allow = r'https://book.douban.com/subject/\d+/$' ), callback = 'parse_item'),
    )

    def parse_item(self, response):
        item = CrawlSpiderTestItem()
        item['saler'] = response.xpath("//h1/span/text()").extract_first()
        item['info'] = response.xpath( "//div[@id='link-report']//div[@class='intro']/p/text()" ).extract_first()
        return item



if __name__ == '__main__':
    cmdline.execute("scrapy crawl CrawlSpiderTest".split())
