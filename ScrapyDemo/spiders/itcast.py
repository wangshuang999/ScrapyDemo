# -*- coding: utf-8 -*-
import scrapy

from ScrapyDemo.items import ItcastItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']

    # 不同的爬虫设置使用不同的管道进行处理
    # custom_settings = {
    #     'ITEM_PIPELINES':{'ScrapyDemo.pipelines.ScrapydemoPipeline': 300}
    # }

    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        # pass
        node_list = response.xpath("//div[@class='li_txt']")

        for node  in node_list:

            item = ItcastItem()
            name = node.xpath('./h3/text()').extract()
            level = node.xpath('./h4/text()').extract()
            info = node.xpath('./p/text()').extract()

            item['name'] = name[0]
            item['level'] = level[0]
            item['info'] = info[0]

            yield item

