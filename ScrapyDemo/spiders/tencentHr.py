# -*- coding: utf-8 -*-
import scrapy
from scrapy import cmdline

from ScrapyDemo.items import TencentHrItem

class TencenthrSpider(scrapy.Spider):
    name = 'tencentHr'
    allowed_domains = ['hr.tencent.com']
    custom_settings = {
        'ITEM_PIPELINES':{
            'ScrapyDemo.pipelines.TencentHrPipeline':1
        }
    }
    start_urls = ['https://hr.tencent.com/position.php?start=0#a']


    def parse(self, response):
        node_list = response.xpath("//tr[@class='even']|//tr[@class='odd']")

        # itemList=[]
        for node in node_list:
            item = TencentHrItem()

            item['info']    =   node.xpath('./td[1]/a/text()').extract_first()
            item['type']    =   node.xpath('./td[2]/text()').extract_first()
            item['num']     =   node.xpath('./td[3]/text()').extract_first()
            item['address'] =   node.xpath('./td[4]/text()').extract_first()
            item['time']    =   node.xpath('./td[5]/text()').extract_first()

            # itemList.append(item)
            yield item


        url_next = response.xpath("//a[@id='next']/@href").extract_first()
        url_next_active = response.xpath("//a[@id='next']/@class").extract_first()   #noactive
        print(url_next)
        print(url_next_active)
        if url_next_active != 'noactive':
            url_next = 'https://hr.tencent.com/'+ url_next
            # itemList.append(scrapy.Request(url_next, callback=self.parse))
            yield scrapy.Request(url_next, callback=self.parse)


        # return itemList


if __name__ == '__main__':
    cmdline.execute("scrapy crawl tencentHr".split())