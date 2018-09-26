# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

import os
import scrapy
from ScrapyDemo.settings import IMAGES_STORE
from scrapy.pipelines.images import ImagesPipeline


class ScrapydemoPipeline(object):

	#.json	.json1	.csv	.xml
    # def __init__(self):
    #     self.fo = open('../data/itcast.json', 'w', encoding='utf-8')
    #
    # # 处理爬虫parse方法返回的数据
    # def process_item(self, item, spider):
    #     content = json.dumps(dict(item), ensure_ascii=False) + ',\n'
    #     self.fo.write(content)
    #     return item
    #
    # def close_spider(self,spider):
    #     self.fo.close()
	def process_item(self, item, spider):
		return item



class TencentHrPipeline(object):

	# def open_spider(self, spider):
	# 	self.fo = open('../data/tencenHr.json', 'w', encoding='utf-8')
	#
	# def process_item(self, item, spider):
	# 	content = json.dumps(dict(item), ensure_ascii=False) + ",\n"
	# 	self.fo.write(content)
	# 	return item
	#
	# def close_spider(self, spider):
	# 	self.fo.close()
	def process_item(self, item, spider):
		return item


class DouyuPipeline(ImagesPipeline):


	def item_completed(self, results, item, info):
		# item
		# {'image_urls': '',
		#  'name': '林芊又丶',
		#  'src_link': 'https://rpic.douyucdn.cn/asrpic/180921/5012670_1618.jpg/dy1'}

		# results
		# [(True, {'url': 'https://rpic.douyucdn.cn/asrpic/180921/1864921_1612.jpg/dy1',
		#          'path': 'full/00469ddb863994ef57b358b2e5920bb05dc25afb.jpg',
		#          'checksum': '6f2743655747a08e09080dbec44d56d0'})]
		image_path = [x['path'] for ok, x in results if ok][0]
		name = item['name']

		image_dir = IMAGES_STORE + 'douyu'+os.sep
		if not os.path.exists(image_dir):
			os.mkdir(image_dir)

		os.rename(IMAGES_STORE + image_path,    image_dir + name + '.jpg')
		return item

	# one
	# pass


	# two
	def get_media_requests(self, item, info):
		src_link = item['src_link']
		# yield scrapy.Request(src_link)
		return scrapy.Request(src_link)















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