# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class ScrapydemoPipeline(object):

	#.json	.json1	.csv	.xml
    def __init__(self):
        self.fo = open('../data/itcast.json', 'w', encoding='utf-8')

    # 处理爬虫parse方法返回的数据
    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + ',\n'
        self.fo.write(content)
        return item

    def close_spider(self,spider):
        self.fo.close()




class TencentHrPipeline(object):

	def open_spider(self, spider):
		self.fo = open('../data/tencenHr.json', 'w', encoding='utf-8')

	def process_item(self, item, spider):
		content = json.dumps(dict(item), ensure_ascii=False) + ",\n"
		self.fo.write(content)
		return item

	def close_spider(self, spider):
		self.fo.close()


class ScrapydemoPipelineDemo(object):

    #针对不同爬虫不同处理
    def process_item(self, item, spider):
		#
        # #one
        # if isinstance(item, ItcastItem):
        #     pass
        # else:
        #     pass
		#
		#
        # # two
        # if spider.name == ItcastSpider.name:
			# pass

        return item