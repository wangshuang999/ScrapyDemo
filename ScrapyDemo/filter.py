#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# @Time : 2018/10/12 14:49 
# @Author : WangShuang 
# @Site :  
# @File : filter.py
# @Software: PyCharm
# @Description:  RFPDupeFilter     Reuqest Finger Point DupeFilter



from scrapy.dupefilter import RFPDupeFilter
class DupeFilter(RFPDupeFilter):
	"""A dupe filter that considers the URL"""
	def __init__(self, path=None):
		self.urls_seen = set()
		RFPDupeFilter.__init__(self, path)

	def request_seen(self, request):
		if request.url in self.urls_seen:
			return True
		else:
			self.urls_seen.add(request.url)



if __name__ == '__main__':
	print( 'main' )