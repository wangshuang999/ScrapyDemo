# -*- coding: utf-8 -*-
import json

import scrapy

from ScrapyDemo.items import DouyuItem


class DouyuSpider(scrapy.Spider):
    """
    下载斗鱼主播信息，
    下载器返回数据为json格式，需下载主播【图片】
    """
    name = 'douyu'
    allowed_domains = ['douyucdn.cn']
    custom_settings = {
        "ITEM_PIPELINES":{"ScrapyDemo.pipelines.DouyuPipeline":1},
        "IMAGES_STORE"  :   "D:\\CodeStudy\\Python\\ScrapyDemo\\ScrapyDemo\\data\\images\\"
    }

    limit = 10
    offset = 0
    url = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=" + str(limit) +"&offset=" + str(offset)
    start_urls = [url]




    # # one  直接使用ImagesPipeline父类的实现,对应的子类DouyuPipeline只声明不实现
    # # 注意点：
    # #     图片链接field必须命名为    image_urls    item['image_urls']
    # #     链接必须为列表形式         item['image_urls'] = [data['vertical_src']]
    # def parse(self, response):
    #     data_list = json.loads(response.body)['data']
    #
    #     item_list = []
    #     for data in data_list:
    #         item = DouyuItem()
    #         item['name'] = data['nickname']
    #         item['image_urls'] = [data['vertical_src']]
    #
    #         item_list.append(item)
    #     if len(data_list) == self.limit:
    #         self.offset += self.limit
    #         # 遇到问题   DEBUG: Filtered offsite request to 'bbs.zol.com.cn': <GET http://bbs.zol.com.cn/dcbbs/d14_134253.html>
    #         # 官方对这个的解释，是你要request的地址和allow_domain里面的冲突，从而被过滤掉。可以停用过滤功能。
    #         # yield Request(url, callback=self.parse_item, dont_filter=True)
    #         item_list.append(scrapy.Request("http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=" + str(self.limit)
    #                                         +"&offset=" + str(self.offset), callback=self.parse, dont_filter=True))
    #
    #     return item_list




    # two 改写ImagesPipeline  的 get_media_requests方法
    # 使用yield生成器
    def parse(self, response):
        data_list = json.loads(response.body)['data']

        for data in data_list:
            item = DouyuItem()
            item['name'] = data['nickname']
            item['src_link'] = data['vertical_src']
            item['image_urls'] = ''

            yield item

        if len(data_list) == self.limit:
            self.offset += self.limit
            yield scrapy.Request("http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=" + str(self.limit)
                           + "&offset=" + str(self.offset), callback=self.parse, dont_filter=True)   #不去重
